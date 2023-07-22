import qrcode

class myQR:
    def __init__(self, size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size,border=padding)

    def createQR(self, fileName: str, fg: str, bg: str):
        userInp: str = input('Enter the content You want QR : ')

        try:
            self.qr.add_data(userInp)
            qrImage = self.qr.make_image(fill_color = fg, back_color = bg)
            qrImage.save(fileName)
            print(f'The QR Image successfully Generated and Saved in the name of {fileName}')

        except ValueError as e:
            print(f"Error : {e}")


if __name__ == '__main__':
    qrc = myQR(size=30, padding=2)
    qrc.createQR(
        'qrcode.png',
        'black',  # white color for foreground
        'white'   # black color for background
    )