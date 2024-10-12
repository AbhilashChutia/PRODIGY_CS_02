import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np

ENCRYPTION_KEY = 255

def encrypt_image(input_image_path, output_image_path):
    try:
        img = Image.open(input_image_path)
        img = img.convert('RGB')  

        data = np.array(img)
        
        encrypted_data = np.bitwise_xor(data, ENCRYPTION_KEY)
        
        encrypted_img = Image.fromarray(encrypted_data.astype(np.uint8))
        
        encrypted_img.save(output_image_path)
        messagebox.showinfo("Success", f"Image encrypted and saved to {output_image_path}")
        
        display_images(img, encrypted_img)
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def decrypt_image(input_image_path, output_image_path):
    try:
        img = Image.open(input_image_path)
        img = img.convert('RGB')
        
        data = np.array(img)
        
        decrypted_data = np.bitwise_xor(data, ENCRYPTION_KEY)
        
        decrypted_img = Image.fromarray(decrypted_data.astype(np.uint8))
        
        decrypted_img.save(output_image_path)
        messagebox.showinfo("Success", f"Image decrypted and saved to {output_image_path}")
        
        display_images(img, decrypted_img)
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def select_file_encrypt():
    input_image_path = filedialog.askopenfilename(title="Select Image to Encrypt")
    if input_image_path:
        output_image_path = filedialog.asksaveasfilename(defaultextension=".jpg", title="Save Encrypted Image As")
        if output_image_path:
            encrypt_image(input_image_path, output_image_path)

def select_file_decrypt():
    input_image_path = filedialog.askopenfilename(title="Select Encrypted Image to Decrypt")
    if input_image_path:
        output_image_path = filedialog.asksaveasfilename(defaultextension=".jpg", title="Save Decrypted Image As")
        if output_image_path:
            decrypt_image(input_image_path, output_image_path)

def display_images(original_img, processed_img):
   
    original_img_resized = original_img.resize((200, 200))
    processed_img_resized = processed_img.resize((200, 200))
    
    
    original_photo = ImageTk.PhotoImage(original_img_resized)
    processed_photo = ImageTk.PhotoImage(processed_img_resized)
    
    original_label.config(image=original_photo, text="Original Image")
    original_label.image = original_photo  
    
    processed_label.config(image=processed_photo, text="Processed Image")
    processed_label.image = processed_photo 

    root.geometry("600x400")

root = tk.Tk()
root.title("Image Encryption/Decryption")

root.geometry("500x100")

encrypt_button = tk.Button(root, text="Encrypt Image", command=select_file_encrypt, width=25)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt Image", command=select_file_decrypt, width=25)
decrypt_button.pack(pady=10)

original_label = tk.Label(root, text="", width=200, height=200)
original_label.pack(side=tk.LEFT, padx=20, pady=10)

processed_label = tk.Label(root, text="", width=200, height=200)
processed_label.pack(side=tk.RIGHT, padx=20, pady=10)

root.mainloop()
