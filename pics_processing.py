import pytesseract
from PIL import Image

image = Image.open('ID_number.jpg')
code = pytesseract.image_to_string(image)

print code
def text_create(name, msg):
    desktop_path = "/home/liu/test/"  
    full_path = desktop_path + name + '.txt' 
    file = open(full_path, 'w')
    file.write(msg)   
    
 
text_create('ID_number_result', code)

