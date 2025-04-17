import cv2

def decode_qr_code(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()

    # Detect and decode
    data, vertices_array, _ = detector.detectAndDecode(img)
    if vertices_array is not None:
        print(f"Decoded Data: {data}")
    else:
        print("No QR Code detected.")

# Example usage
if __name__ == "__main__":
    decode_qr_code("example_qr.png")
