from ctypes import cdll, c_char_p, c_void_p, c_uint, c_bool
import os

pyjpeg_path = os.path.join( os.path.dirname( __file__ ), '_pyjpeg.so' )

pyjpeglib = cdll.LoadLibrary( pyjpeg_path )

pyjpeglib.pyjpeg_write_file.argtypes = [c_char_p, c_void_p, c_uint, c_uint, c_uint, c_uint, c_uint]
pyjpeglib.pyjpeg_write_file.restype = c_bool

def write_file( filename, data, width, height, stride=None, components=3, quality=80):
	if quality < 0 or quality > 100:
		raise ValueError("quality must be between zero and 100")

	if stride is None:
		stride = components * width

	if not isinstance(data, str):
		raise TypeError("data must be str")

	if isinstance(data, str) and len(data) != stride * height:
		raise ValueError("data length is not stride * height")

	if stride < width * components:
		raise ValueError("stride too small")

	success = pyjpeglib.pyjpeg_write_file(filename, data, width, height, stride, components, quality)

	if not success:
		raise IOError('could not open file to write: %r' % filename)