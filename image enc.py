import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, UnidentifiedImageError

def encrypt_image(image_path, key):
    """Encrypt an image using XOR."""
    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()

        # Encrypt the data using XOR
        encrypted_data = bytearray([(byte ^ key) for byte in image_data])

        # Save the encrypted data
        encrypted_file_path = os.path.splitext(image_path)[0] + ".enc"
        with open(encrypted_file_path, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        return encrypted_file_path
    except Exception as e:
        messagebox.showerror("Error", f"Failed to encrypt image: {e}")
        return None


def decrypt_image(encrypted_file_path, key):
    """Decrypt an encrypted image file."""
    try:
        with open(encrypted_file_path, "rb") as encrypted_file:
            encrypted_data = encrypted_file.read()

        # Decrypt the data using XOR
        decrypted_data = bytearray([(byte ^ key) for byte in encrypted_data])

        # Save the decrypted data
        decrypted_file_path = os.path.splitext(encrypted_file_path)[0] + "_decrypted.jpg"
        with open(decrypted_file_path, "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)

        # Validate the decrypted file
        try:
            Image.open(decrypted_file_path).verify()
        except UnidentifiedImageError:
            os.remove(decrypted_file_path)
            raise ValueError("Decryption failed. The key might be incorrect or the file is corrupted.")

        return decrypted_file_path
    except Exception as e:
        messagebox.showerror("Error", f"Failed to decrypt image: {e}")
        return None


def select_image():
    """Open a file dialog to select an image file."""
    global selected_image_file
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )
    if file_path:
        selected_image_file = file_path
        img_label.config(text=f"Selected Image: {os.path.basename(file_path)}", foreground="green")
    else:
        selected_image_file = None
        img_label.config(text="No image selected.", foreground="red")


def select_encrypted_file():
    """Open a file dialog to select an encrypted .enc file."""
    global selected_encrypted_file
    file_path = filedialog.askopenfilename(filetypes=[("Encrypted Files", "*.enc")])
    if file_path:
        selected_encrypted_file = file_path
        encrypted_label.config(text=f"Selected Encrypted File: {os.path.basename(file_path)}", foreground="green")
    else:
        selected_encrypted_file = None
        encrypted_label.config(text="No encrypted file selected.", foreground="red")


def perform_encryption():
    """Handle the encryption process."""
    if not selected_image_file:
        messagebox.showerror("Error", "Please select an image first.")
        return

    key = key_entry.get()
    if not key.isdigit():
        messagebox.showerror("Error", "Key must be a numeric value.")
        return

    key = int(key) % 256
    encrypted_path = encrypt_image(selected_image_file, key)
    if encrypted_path:
        messagebox.showinfo("Success", f"Image encrypted successfully!\nSaved as: {encrypted_path}")


def perform_decryption():
    """Handle the decryption process."""
    if not selected_encrypted_file:
        messagebox.showerror("Error", "Please select an encrypted file first.")
        return

    key = key_entry.get()
    if not key.isdigit():
        messagebox.showerror("Error", "Key must be a numeric value.")
        return

    key = int(key) % 256
    decrypted_path = decrypt_image(selected_encrypted_file, key)
    if decrypted_path:
        messagebox.showinfo("Success", f"Image decrypted successfully!\nSaved as: {decrypted_path}")


# Tkinter GUI Setup
app = tk.Tk()
app.title("Image Encryption & Decryption")
app.geometry("600x450")
app.resizable(False, False)

# Header
header = tk.Label(app, text="Image Encryption & Decryption", font=("Helvetica", 16, "bold"))
header.pack(pady=20)

# File Selection
selected_image_file = None
img_label = tk.Label(app, text="No image selected.", wraplength=500, foreground="red")
img_label.pack(pady=10)

select_image_button = tk.Button(app, text="Select Image", command=select_image, font=("Helvetica", 12))
select_image_button.pack(pady=5)

# Encrypted File Selection
selected_encrypted_file = None
encrypted_label = tk.Label(app, text="No encrypted file selected.", wraplength=500, foreground="red")
encrypted_label.pack(pady=10)

select_encrypted_button = tk.Button(app, text="Select Encrypted File", command=select_encrypted_file, font=("Helvetica", 12))
select_encrypted_button.pack(pady=5)

# Key Entry
key_frame = tk.Frame(app)
key_frame.pack(pady=15)

key_label = tk.Label(key_frame, text="Enter Numeric Key:", font=("Helvetica", 12))
key_label.pack(side=tk.LEFT, padx=10)

key_entry = tk.Entry(key_frame, width=20, font=("Helvetica", 12))
key_entry.pack(side=tk.LEFT, padx=10)

# Action Buttons
button_frame = tk.Frame(app)
button_frame.pack(pady=20)

encrypt_button = tk.Button(button_frame, text="Encrypt Image", command=perform_encryption, font=("Helvetica", 12))
encrypt_button.pack(side=tk.LEFT, padx=20)

decrypt_button = tk.Button(button_frame, text="Decrypt File", command=perform_decryption, font=("Helvetica", 12))
decrypt_button.pack(side=tk.LEFT, padx=20)

# Footer
footer = tk.Label(app, text="Ensure to use the same key for decryption as used for encryption.", font=("Helvetica", 10, "italic"))
footer.pack(side=tk.BOTTOM, pady=10)

# Run the application
app.mainloop()
