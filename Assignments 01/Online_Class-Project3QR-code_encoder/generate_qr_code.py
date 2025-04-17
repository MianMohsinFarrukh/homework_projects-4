import qrcode

def generate_qr_code(data, output_file):
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate and save the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"QR Code saved as {output_file}")

# Example usage
if __name__ == "__main__":
    generate_qr_code("https://example.com", "example_qr.png")
