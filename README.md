# QR Code Generator

This is a Python script to generate a QR code using the `qrcode` library. The generated QR code will encode a given URL and save it as an image file.

## Features
- Generates a QR code for a specified URL
- Customizable QR code properties (size, border, error correction level)
- Saves the QR code as an image file

## Prerequisites
Make sure you have Python installed on your system. You also need to install the `qrcode` library if you haven't already.

### Installation
```sh
pip install qrcode[pil]
```

## Usage
1. Clone this repository or create a Python script with the provided code.
2. Run the script to generate the QR code.
3. The QR code image will be saved as `advanced.png`.

### Code
```python
import qrcode as qr

qrCode = qr.QRCode(
  version = 1,
  error_correction = qr.constants.ERROR_CORRECT_L,
  box_size = 20,
  border = 2,
)

qrCode.add_data("https://precious-nasturtium-b1b271.netlify.app/")
qrCode.make(fit = True)

img = qrCode.make_image(
  fill_color = "black",
  back_color = "white"
)

img.save("advanced.png")
```

## Output
The script will generate a QR code and save it as `advanced.png`. You can scan the QR code using any QR scanner to visit the encoded URL.

## License
This project is open-source and free to use.

