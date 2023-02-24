import qrcode

features = qrcode.QRCode(version=1, box_size = 38, border = 2 )
features.add_data('https://www.instagram.com/qr/dreammmate')
features.make(fit= True)
generate_image = features.make_image(fill_color="Pink" , back_color="White")
generate_image.save('Insta.png')

features = qrcode.QRCode(version=1, box_size = 38, border = 2 )
features.add_data("https://www.linkedin.com/in/manasi-rane-539a99220/")
features.make(fit= True)
generate_image2 = features.make_image(fill_color="Blue" , back_color="White")
generate_image2.save('linkedinpage.png')

features = qrcode.QRCode(version=1, box_size = 40, border = 5 )
features.add_data('https://github.com/mannasiii')
features.make(fit= True)
generate_image3 = features.make_image(fill_color="Black" , back_color="White")
generate_image3.save('Github.png')

