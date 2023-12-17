import pyqrcode
url='https://github.com/mohamedarsath1101/voice_assistant/tree/main/voice%20assistant'
scan=pyqrcode.create(url)
scan.svg('Qr.svg',scale=10)