import qrcode as qr
img = qr.make("https://www.linkedin.com/in/rashmi-rautela-3912b6247/") #make() function to generate a QR code and saves it as an image file
img.save("Linkedin_Rashmi.png")