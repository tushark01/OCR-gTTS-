import pytesseract
import cv2
import os
from gtts import gTTS

#? Taking image as input
args = {
	"image": "test2.jpg",
}
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#^ Tesseract OCR Engine

imtext = pytesseract.image_to_string(image)
language = 'en'

#~ Google Text to speech API

myobj = gTTS(text=imtext, lang=language, slow=False)
  
#!Saving the converted audio in a mp3 file named
#* welcome 
myobj.save("welcome3.mp3")
  
#&Playing the converted file
os.system("welcome3.mp3")