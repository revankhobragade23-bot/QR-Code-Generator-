import qrcode

data = "https://www.example.com"

qr = qrcode.make(data)

qr.save("example_qr.png")

print("QR code Generator")