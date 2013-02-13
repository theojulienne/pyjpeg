#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <jpeglib.h>
#include <stdbool.h>
#include <assert.h>

bool pyjpeg_write_file( const char *filename, const uint8_t *data, uint32_t width, uint32_t height, uint32_t stride, uint32_t components, uint32_t quality ) {
    struct jpeg_compress_struct cinfo;
    struct jpeg_error_mgr jerr;
    
    FILE *outfile = fopen( filename, "wb" );
    
    if ( outfile == NULL ) {
        return false;
    }
    
    // use the standard libjpeg error handler
    cinfo.err = jpeg_std_error( &jerr );
    
    jpeg_create_compress( &cinfo );
    
    jpeg_stdio_dest( &cinfo, outfile );
    
    // write the image header
    cinfo.image_width = width;
    cinfo.image_height = height;
    cinfo.input_components = components;
    cinfo.in_color_space = JCS_RGB;
    jpeg_set_defaults( &cinfo );
    cinfo.num_components = 3;
    //cinfo.data_precision = 4;
    cinfo.dct_method = JDCT_FLOAT;
    jpeg_set_quality( &cinfo, quality, true );
    
    // start compression
    jpeg_start_compress( &cinfo, true );
    
    {
        JSAMPROW row_pointer;
        
        while ( cinfo.next_scanline < cinfo.image_height ) {
            row_pointer = (JSAMPROW)&data[cinfo.next_scanline * stride];
            jpeg_write_scanlines( &cinfo, &row_pointer, 1 );
        }
    }
    
    jpeg_finish_compress( &cinfo );
    jpeg_destroy_compress( &cinfo );
    fclose( outfile );
    
    return true;
}
