import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, simpledialog
import os
import hashlib
import pyzipper
import time
from datetime import datetime

import zipfile

import tkinter as tk
from tkinter import ttk


#### Web Fuzzing 
main_banner = """
+========================+
|╔═╗┌─┐┌┬┐┌─┐┬─┐┌─┐┌─┐┌─┐|
|║  │ ││││├─┘├┬┘├┤ └─┐└─┐|
|╚═╝└─┘┴ ┴┴  ┴└─└─┘└─┘└─┘|
+========================+
"""
    
creator_banner = """
+============================+
|░█▀▄░█▀▀░█▀▀░█░█░█▀▀░░░░░█▀▄|
|░█▀▄░▀▀█░█░░░░█░░▀▀█░▄▄▄░█▀▄|
|░▀▀░░▀▀▀░▀▀▀░░▀░░▀▀▀░░░░░▀▀░|
+============================+
"""


Details_banner = """
.-------------------.
|╔╦╗┌─┐┌┬┐┌─┐┬┬  ┌─┐|
| ║║├┤  │ ├─┤││  └─┐|
|═╩╝└─┘ ┴ ┴ ┴┴┴─┘└─┘|
'-------------------'
"""

thanks_banner1 = """
.--------------------------.
|╔╦╗┬ ┬┌─┐┌┐┌┬┌─  ╦ ╦┌─┐┬ ┬|
| ║ ├─┤├─┤│││├┴┐  ╚╦╝│ ││ │|
| ╩ ┴ ┴┴ ┴┘└┘┴ ┴   ╩ └─┘└─┘|
'--------------------------'
"""


def clear_output(output_text):
    output_text.delete('1.0', tk.END)

def logout(output_text):
    output_text.delete('1.0', tk.END)
    output_text.tag_configure("center", justify="center")

    # Display the banner first
    output_text.insert(tk.END, "\n\n", "center")
    output_text.insert(tk.END, thanks_banner1, "center")
    output_text.insert(tk.END, "\n\n", "center")

    # Display the counter
    count = 3
    while count > 0:
        output_text.insert(tk.END, str(count) + " ", "center")
        output_text.update()  # Update the text widget to display the counter immediately
        count -= 1
        time.sleep(1)  # Wait for 1 second before the next count

    # Display the closing message
    output_text.insert(tk.END, "\n\n", "center")
    output_text.insert(tk.END, "Exiting... Bye Bye", "center")
    output_text.update()  # Update the text widget to display the closing message
    time.sleep(2)  # Wait for 2 seconds before exiting
    exit()


def format_file_details(file_path):
    details = {}
    details['File Name'] = os.path.basename(file_path)
    details['File Size'] = os.path.getsize(file_path)
    details['Created'] = time.ctime(os.path.getctime(file_path))
    details['Modified'] = time.ctime(os.path.getmtime(file_path))
    details['MD5 Hash'] = calculate_hash(file_path, hashlib.md5())
    details['SHA1 Hash'] = calculate_hash(file_path, hashlib.sha1())
    details['Extension'] = os.path.splitext(file_path)[1]
    details['File Path'] = file_path
    return details

def calculate_hash(file_path, hash_alg):
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            hash_alg.update(chunk)
    return hash_alg.hexdigest()

def display_file_details(output_text, files):
    output_text.delete('1.0', tk.END)
    output_text.tag_configure("center", justify="center")
    output_text.insert(tk.END, "\n\n", "center")
    output_text.insert(tk.END, Details_banner, "center")


    total_size = sum(os.path.getsize(f) for f in files)
    
    output_text.tag_configure("center", justify="center")
    output_text.insert(tk.END, f"\nTotal Combined Size: {total_size} bytes\n\n", "center")

    for file_path in files:
        details = format_file_details(file_path)
        output_text.insert(tk.END, "File Details:\n")
        for key, value in details.items():
            output_text.insert(tk.END, f"- {key}: {value}\n")
        # output_text.insert(tk.END, "\n")
        output_text.insert(tk.END, "\n" + "______________________________________________________________________________________________________________________________________________________________________" + "\n")



def display_decompress_file_details(output_text, files):
    output_text.delete('1.0', tk.END)
    output_text.tag_configure("center", justify="center")
    output_text.insert(tk.END, "\n\n", "center")
    output_text.insert(tk.END, Details_banner, "center")


    total_size = os.path.getsize(files)
    
    output_text.tag_configure("center", justify="center")
    output_text.insert(tk.END, f"\nFile Size: {total_size} bytes\n\n", "center")


    details = format_file_details(files)
    output_text.insert(tk.END, "File Details:\n")
    for key, value in details.items():
        output_text.insert(tk.END, f"- {key}: {value}\n")
    # output_text.insert(tk.END, "\n")
    output_text.insert(tk.END, "\n" + "____________________________________________________________________________________________________________________________________________________________________" + "\n")



def is_strong_password(password):
    import re
    if len(password) < 8:
        return False
    if not (re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'\d', password)):
        return False
    return True


# def compression_action(output_text):
#     files = filedialog.askopenfilenames(title="Select Files for Compression")
#     if not files:
#         return
#     clear_output(output_text)
#     display_file_details(output_text, files)
#     proceed = messagebox.askyesno("Proceed?", "Do you want to proceed with the selected files?")
#     if not proceed:
#         compression_action(output_text)
#         return
#     protect = messagebox.askyesno("Password Protect?", "Do you want to protect the zip file with a password?")
#     if protect:
#         while True:
#             password = simpledialog.askstring("Password", "Enter password for zip file:", show='*')
#             if password is None:
#                 return
#             if not is_strong_password(password):
#                 messagebox.showerror("Weak Password", "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.")
#             else:
#                 break
#     else:
#         password = None
#     default_name = "compressed_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".zip"
#     zip_name = simpledialog.askstring("Zip File Name", f"Enter zip file name (default: {default_name}):")
#     if not zip_name:
#         zip_name = default_name
#     zip_path = filedialog.asksaveasfilename(defaultextension=".zip", initialfile=zip_name)
#     if not zip_path:
#         return
#     try:
#         with pyzipper.AESZipFile(zip_path, 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zipf:
#             if password:
#                 zipf.setpassword(password.encode())
#                 zipf.setencryption(pyzipper.WZ_AES, nbits=256)
#             for file in files:
#                 zipf.write(file, os.path.basename(file))
#         zip_size = os.path.getsize(zip_path)
#         success_message = f"Zip file created successfully:\n- Name: {os.path.basename(zip_path)}\n- Path: {zip_path}\n- Size: {zip_size} bytes\n"
#         output_text.insert(tk.END, f"\n{success_message}")
#         # Display success message as an alert
#         messagebox.showinfo("Success", success_message)
#     except Exception as e:
#         messagebox.showerror("Error", f"An error occurred: {e}")


def compression_action(output_text):
    files = filedialog.askopenfilenames(title="Select Files for Compression")
    if not files:
        return
    clear_output(output_text)
    display_file_details(output_text, files)
    proceed = messagebox.askyesno("Proceed?", "Do you want to proceed with the selected files?")
    if not proceed:
        compression_action(output_text)
        return
    protect = messagebox.askyesno("Password Protect?", "Do you want to protect the zip file with a password?")
    
    if protect:
        while True:
            password = simpledialog.askstring("Password", "Enter password for zip file:", show='*')
            if password is None:
                return
            if not is_strong_password(password):
                messagebox.showerror("Weak Password", "Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.")
            else:
                break
    else:
        password = None

    default_name = "compressed_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".zip"
    zip_name = simpledialog.askstring("Zip File Name", f"Enter zip file name (default: {default_name}):")
    if not zip_name:
        zip_name = default_name
    zip_path = filedialog.asksaveasfilename(defaultextension=".zip", initialfile=zip_name)
    if not zip_path:
        return
    
    try:
        if protect:
            # Create a password-protected zip file
            with pyzipper.AESZipFile(zip_path, 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zipf:
                if password:
                    zipf.setpassword(password.encode())
                    zipf.setencryption(pyzipper.WZ_AES, nbits=256)
                for file in files:
                    zipf.write(file, os.path.basename(file))
        else:
            # Create a regular zip file
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for file in files:
                    zipf.write(file, os.path.basename(file))
        
        zip_size = os.path.getsize(zip_path)
        success_message = f"Zip file created successfully:\n- Name: {os.path.basename(zip_path)}\n- Path: {zip_path}\n- Size: {zip_size} bytes\n"
        output_text.insert(tk.END, f"\n{success_message}")
        # Display success message as an alert
        messagebox.showinfo("Success", success_message)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")



def decompression_action(output_text):
    zip_file = filedialog.askopenfilename(title="Select Zip File for Decompression", filetypes=[("Zip Files", "*.zip")])
    if not zip_file:
        return
    clear_output(output_text)
    display_decompress_file_details(output_text, zip_file)


    proceed = messagebox.askyesno("Proceed?", "Do you want to proceed with the selected zip file?")
    if not proceed:
        decompression_action(output_text)
        return
    is_encrypted = False
    with pyzipper.AESZipFile(zip_file) as zf:
        try:
            zf.testzip()
        except RuntimeError:
            is_encrypted = True
    if is_encrypted:
        password = simpledialog.askstring("Password", "Enter password for zip file:", show='*')
        if password is None:
            return
    else:
        password = None
    extract_path = filedialog.askdirectory(title="Select Extraction Folder")
    if not extract_path:
        return
    try:
        with pyzipper.AESZipFile(zip_file, 'r') as zipf:
            if password:
                zipf.pwd = password.encode()
            zipf.extractall(path=extract_path)
        success_message = f"\nZip file extracted successfully to:\n{extract_path}\n"
        output_text.insert(tk.END, success_message)
        # Display success message as an alert
        messagebox.showinfo("Success", success_message)
    except RuntimeError as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def main():
        # Display welcome message
    welcome_message = """\n\n\n\n\n

██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
                                                              
"""

    root = tk.Tk()
    root.title("File Compression and Decompression Tool")
    

    # output_frame = tk.Frame(root)
    # output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # output_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, bg="cyan4", fg="cyan1")
    # output_text.pack(fill=tk.BOTH, expand=True)


    output_frame = tk.Frame(root)
    output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    output_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, bg="cyan4", fg="white")
    output_text.pack(fill=tk.BOTH, expand=True, padx=(10, 0))  # Padding only on the left side



    output_text.tag_configure("center", justify="center")
    output_text.insert(tk.END, welcome_message, "center")
    output_text.tag_configure("center", justify="center")
    output_text.insert(tk.END, main_banner, "center")
    output_text.tag_configure("center", justify="center")
    output_text.insert(tk.END, creator_banner, "center")


    # button_frame = tk.Frame(root, bg="light sea green")
    # button_frame.pack(side=tk.LEFT, fill=tk.Y)


    # compression_button = tk.Button(button_frame, text="Compression", command=lambda: compression_action(output_text), width=25, bg="cyan4", fg="white")
    # compression_button.pack(pady=5)

    # decompression_button = tk.Button(button_frame, text="Decompression", command=lambda: decompression_action(output_text), width=25, bg="cyan4", fg="white")
    # decompression_button.pack(pady=5)

    # clear_button = tk.Button(button_frame, text="Clear Output", command=lambda: clear_output(output_text), width=25, bg="cyan4", fg="white")
    # clear_button.pack(pady=5)

    
    # Logout_button = tk.Button(button_frame, text="Logout", command=lambda: logout(output_text), width=25, bg="cyan4", fg="white")
    # Logout_button.pack(pady=5)

    # Button Frame
    button_frame = tk.Frame(root, bg="light sea green")
    button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=1, pady=1)

    # Style Configuration
    style = ttk.Style()
    style.configure(
        'Custom.TButton',
        background='light sea green',
        foreground='cyan4',
        font=('Courier', 16, 'bold'),
        padding=10,
        borderwidth=3,
        relief='flat'
    )
    style.map(
        'Custom.TButton',
        background=[('active', 'cyan4')],
        foreground=[('active', 'cyan1')]
    )

    # Stylish Buttons
    compression_button = ttk.Button(
        button_frame,
        text="Compression",
        command=lambda: compression_action(output_text),
        style='Custom.TButton'
    )
    compression_button.pack(pady=2, fill=tk.X)

    decompression_button = ttk.Button(
        button_frame,
        text="Decompression",
        command=lambda: decompression_action(output_text),
        style='Custom.TButton'
    )
    decompression_button.pack(pady=2, fill=tk.X)

    clear_button = ttk.Button(
        button_frame,
        text="Clear Output",
        command=lambda: clear_output(output_text),
        style='Custom.TButton'
    )
    clear_button.pack(pady=2, fill=tk.X)

    logout_button = ttk.Button(
        button_frame,
        text="Exit",
        command=lambda: logout(output_text),
        style='Custom.TButton'
    )
    logout_button.pack(pady=2, fill=tk.X)

 








    root.mainloop()

if __name__ == "__main__":
    main()

