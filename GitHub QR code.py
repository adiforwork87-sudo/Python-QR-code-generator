# QR Code For GitHub profile 

import qrcode

qr = qrcode.QRCode(box_size = 6,
                   border = 4)

qr.add_data("https://github.com/adiforwork87-sudo")
img = qr.make_image(fill_color = "blue", back_color = "yellow")
img.save("GitHub QR Code.png")

