Here is how you can run a plugin in python using Pillow. 


Firstly, download an image you like off the internet and save it to your designated file. IN this case, it was the IT3038c-scriptss directory. 

In VScode, I dragged and dropped the image I downloaded into that directory. 

I have created a seperate folder for this plugin DO NOT DRAG THE IMAGE INTO THE SEPERATE FOLDER, IT WILL NOT RUN AND WILL GIVE YOU AN ERROR!!!


For this lab, I have chosen to run PIllow and have the image to be blurred, created a thumbnail, and added some filters to the image itself. 


Lets start off with the blurring of the picture:

    You will need to import the image and image filters from PIL, Like so: 
         ![image](https://user-images.githubusercontent.com/111783701/196596157-1da818e8-23ea-411d-b70c-803d4b8201b8.png)

    Then you will open the image using ---> whatever you named your function = Image.open('what ever you named you image.jpeg')
    
    This will open the original photo and then you can show it by your function.show()
    
   AFter that you can add the blur by putting in ---> newFunction name = function.filter(ImageFilter.BLUR)
   
   This will then blur you image. 
   
   Show and save by doing this: 
    ![image](https://user-images.githubusercontent.com/111783701/196596650-d8c4ba03-0ea8-4699-84aa-7d3f902bf0a0.png)
That is how you blur you image. 



For thumbnail. It is quite the same by importing the image and filters. however you will need to add the following to create a thumbnail:

      def tnails():
      try:
        size your image by image.thumbnail((size,size))
        your code to open,show, and save the image
        
        except IOError:
          pass
       tnails()
        
       
For the filter. It is also very similar to Blurring the image. 

In this case you will need to do the same as blur, but before opening the image you need to import the filters from Pillow:

![image](https://user-images.githubusercontent.com/111783701/196597254-74b45a73-e837-47b3-9981-481dca4b4d06.png)

There are more filters available, I just chose these. 

And that's it, that is how you use the plugins from Pillow. 
 
      
