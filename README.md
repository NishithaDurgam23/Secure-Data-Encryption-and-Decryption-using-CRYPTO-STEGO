🔐 Secure-Data-Encryption-and-Decryption-using-CRYPTO-STEGO

## 🧩 Overview

**Crypto-Steganography** is a Python-based tool that combines the power of **cryptography** and **steganography** to provide a secure and discreet method of hiding sensitive information within image files. The tool first **encrypts a message using RSA encryption**, then **embeds the encrypted data into an image file** using steganographic techniques—making the presence of the message undetectable to the naked eye or casual inspection.

This dual-layer security model is ideal for privacy-focused communications, cybersecurity training, and exploring secure data transmission techniques.

---

## 📘 Introduction

In the digital era, data confidentiality and privacy are more critical than ever. While cryptography protects data by converting it into unreadable ciphertext, steganography hides the very existence of the data. This project merges both techniques to offer a powerful solution for:

- Concealing encrypted messages inside common image formats
- Protecting data against interception and unauthorized access
- Demonstrating applied cybersecurity concepts in a practical project

---

## ⚠️ Disclaimer

> This project is intended for **educational** and **research purposes** only.  
> The misuse of this tool for unethical or illegal activities is strictly prohibited.  
> The author assumes **no responsibility** for any misuse or damage caused.

---

## ⚙️ Prerequisites

- Python 3.6 or higher
- Install required dependencies:

pip install -r requirements.txt
Dependencies Include:

cryptography – for RSA encryption/decryption

Pillow – for image processing and manipulation

🚀 Installation & Setup
Clone the repository:

bash
git clone https://github.com/NishithaDurgam23/crypto-stegno.git
cd crypto-stegno
Install the necessary packages:

bash
pip install -r requirements.txt
🛠️ Usage
🔒 Embed an Encrypted Message in an Image
bash
Copy
Edit
python embed.py --image input.png --message "Secret Message" --output output.png --key yourpassword
🔓 Extract and Decrypt the Message
bash
Copy
Edit
python extract.py --image output.png --key yourpassword
Ensure you use the same key for encryption and decryption. If the key is incorrect, the message will not be retrievable.

🧪 Project Components Explained
1. embed.py
Accepts an input image, a plaintext message, and a secret key.

Encrypts the message using RSA encryption.

Embeds the encrypted data into the image's pixel data.

Outputs a new image file with the hidden message.

2. extract.py
Accepts the image containing the hidden message and the decryption key.

Extracts the encrypted payload from the image.

Decrypts the message and displays the original content.

3. encryption_utils.py (Optional module, if separated)
Handles encryption and decryption functions securely using the Fernet or AES cipher.

📈 Future Enhancements
🔐 Support for RSA or hybrid cryptographic algorithms

🖼️ Compatibility with additional image formats (BMP, TIFF)

🧠 Anti-steganalysis techniques for added security

🖥️ GUI using PyQt or Tkinter for user-friendly interaction

🧾 Logging and error handling enhancements


## 📄 License
This project is licensed under the MIT License.
You are free to use, modify, and distribute the code with proper attribution.

---
📬 Contact
Developed by Nishitha Durgam
Feel free to reach out via:

Email: nishithadurgam@gmail.com 
