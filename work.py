from PIL import Image

img = Image.open("logo.png")

# Crop to content (removes empty/transparent space)
bbox = img.getbbox()
cropped = img.crop(bbox)

cropped.save("logo_cropped.png")