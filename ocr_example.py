from PIL import Image
import pytesseract

# Tesseract'ın yüklü olduğu yolu belirtin (macOS ve Linux için gerekli değilse bu satırı kaldırabilirsiniz)
# pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

img_path = 'images/photo7.jpeg'
img = Image.open(img_path)

text = pytesseract.image_to_string(img)

print(text)
