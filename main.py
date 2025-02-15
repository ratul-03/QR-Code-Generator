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
