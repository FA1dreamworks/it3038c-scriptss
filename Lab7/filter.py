from doctest import DocTestFailure
from PIL import Image, ImageFilter

from PIL.ImageFilter import (
   CONTOUR, DETAIL, EDGE_ENHANCE
)

bmw = Image.open('bmw.jpeg')
bmw2= bmw.filter(DETAIL)
bmw2.save('Lab7/BmwFilter.jpeg')
bmw2.show()