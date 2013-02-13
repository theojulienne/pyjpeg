from ctypes import cdll, c_void_p
import os

pyjpeg_path = os.path.join( os.path.dirname( __file__ ), '_pyjpeg.so' )

pyjpeglib = cdll.LoadLibrary( pyjpeg_path )

def write_file( filename, data, width, height, stride, components, quality=80 ):
	print pyjpeglib