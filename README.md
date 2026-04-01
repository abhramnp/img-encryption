# img-encryption
# 🖼️ Image Encryption & Decryption Tool

A simple Python-based GUI application to encrypt and decrypt image files using an XOR-based algorithm. This tool provides an easy way to protect image data with a numeric key and restore it when needed.

---

## 🚀 Features

- 🔐 Encrypt any image file using XOR encryption  
- 🔓 Decrypt `.enc` files back into images  
- 🖥️ User-friendly GUI built with Tkinter  
- 📂 Supports multiple image formats (PNG, JPG, JPEG, BMP, GIF)  
- ⚡ Fast byte-level encryption and decryption  
- ✅ Validation to ensure correct decryption  

---

## 🧠 How It Works

This project uses a simple XOR encryption technique, where each byte of the image is modified using a numeric key.

- Encryption: Each byte of the image is XORed with the key  
- Decryption: The same XOR operation restores the original image  

Since XOR is reversible, the same key must be used for both encryption and decryption.

---

## 🛠️ Technologies Used

- Python  
- Tkinter (GUI)  
- Pillow (PIL)  
- OS module  

---

## 📂 Project Structure
  project/
  │── main.py
  │── *.enc
  │── *_decrypted.jpg


---

## ▶️ How to Run

1. Clone the repository:

 - git clone https://github.com/your-username/image-encryption-tool.git
 - cd image-encryption-tool

2. Install Dependencies

   pip install pillow

3.Run the application 
  
   python main.py

---

📌 Usage

🔐 Encrypt an Image
Click "Select Image"
Choose an image file
Enter a numeric key
Click "Encrypt Image"
File will be saved as .enc

🔓 Decrypt an Image
Click "Select Encrypted File"
Choose a .enc file
Enter the same key
Click "Decrypt File"
Image will be saved as .jpg

---

⚠️ Important Notes
Key must be a numeric value (0–255)
Using the wrong key will produce a corrupted image
Decryption is validated using image verification
Original file is not modified

---

💡 Future Improvements
Add AES encryption
Improve UI/UX
Add drag-and-drop support
Batch processing support

---

👨‍💻 Author

Abhiram N P
