import qrcode

def generate_qr_code_ascii(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=1)
    qr.add_data(text)
    qr.make(fit=True)
    
    qr_matrix = qr.get_matrix()

    qr_code_ascii = ""
    for row in qr_matrix: 
        qr_code_ascii += "".join(["██" if dark else "  " for dark in row]) + "\n"
    return qr_code_ascii

def main():
    text = input("Введите текст для генерации QR кода: ")
    qr_code_ascii = generate_qr_code_ascii(text)
    print(qr_code_ascii)

if __name__ == "__main__":
    main()
