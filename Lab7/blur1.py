from PIL import Image, ImageFilter

bmw = Image.open('bmw.jpeg')
bmw.show()

blurBmw = bmw.filter(ImageFilter.BLUR)
blurBmw.show()
blurBmw.save('Lab7/blurbmw.jpeg')