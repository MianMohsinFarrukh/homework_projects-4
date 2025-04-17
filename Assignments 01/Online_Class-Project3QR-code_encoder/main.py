from qr_utils import generate_qr_code, decode_qr_code

def main():
    print("QR Code Encoder/Decoder")
    print("1. Generate QR Code")
    print("2. Decode QR Code")
    choice = input("Enter your choice: ")

    if choice == '1':
        data = input("Enter the data to encode: ")
        filename = input("Enter the output filename (e.g., my_qr.png): ")
        generate_qr_code(data, filename)
    elif choice == '2':
        filename = input("Enter the filename to decode (e.g., my_qr.png): ")
        decode_qr_code(filename)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
