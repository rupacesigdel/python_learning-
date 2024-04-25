import qrcode

qr= qrcode.make("https://github.com/rupacesigdel")

qr.save("qr.jpg")