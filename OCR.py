import pytesseract
from PIL import Image

# Load the image from which text needs to be extracted
img = Image.open('invoice.png')

# Use pytesseract to extract text
text = pytesseract.image_to_string(img)

print("Extracted Text: ", text)
