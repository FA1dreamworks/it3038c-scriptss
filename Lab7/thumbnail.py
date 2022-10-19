from PIL import Image
def tnails():
    try:
        image = Image.open('bmw.jpeg')
        image.thumbnail((120,120))
        image.save('Lab7/thumbnailBmw.jpeg')
        thumbBmw = Image.open('Lab7/thumbnailBmw.jpeg')
        thumbBmw.show()
    except IOError:
        pass
tnails()    

