File Compression and Decompression Tool
Overview
This Python-based graphical application provides functionality for file compression and decompression. The tool allows users to compress multiple files into a ZIP archive and decompress existing ZIP archives. It includes features like password protection for compressed files and detailed file metadata display.

Features
1. File Compression
Compress multiple files into a ZIP archive.
Option to password-protect the ZIP archive.
Supports both regular and AES-encrypted ZIP compression.
2. File Decompression
Decompress ZIP archives.
Handles password-protected ZIP archives securely.
3. File Details Display
Displays metadata of files selected for compression or decompression, including:
File name
File size
Creation and modification dates
MD5 and SHA1 hashes
File extension
4. User Interface
Built with Tkinter for simplicity and usability.
Includes:
A scrolled text widget for output and feedback.
Stylish buttons using Tkinter's ttk module.
Code Structure
Main Components
File Metadata Formatting

format_file_details(file_path)
Gathers and formats file details.
calculate_hash(file_path, hash_alg)
Calculates MD5 or SHA1 hashes for files.
Compression Logic

compression_action(output_text)
Handles file selection, password input, and ZIP creation.
Supports AES encryption via the pyzipper library.
Decompression Logic

decompression_action(output_text)
Handles file selection and extraction.
Manages password-protected archives.
Graphical User Interface

Developed with Tkinter and ttk.
Buttons for compression, decompression, clearing output, and exiting.
Scrolled text widget for output messages.
Utility Functions

clear_output(output_text)
Clears the output display.
logout(output_text)
Displays a logout message and exits the application.
Banners
The application includes ASCII art banners for:

Main interface.
Creator credits.
File details section.
Exit message.
Usage
Running the Application
Ensure Python 3.x and required libraries are installed:
pip install pyzipper
Run the script using:
python finalcode.py
Interaction
Compress Files
Click the "Compression" button.
Select files and configure options (e.g., password protection).
Decompress Files
Click the "Decompression" button.
Select a ZIP archive and provide a password if required.
Clear Output
Click "Clear Output" to reset the output text area.
Exit Application
Click "Exit" to close the application.
Dependencies
Python 3.x
Libraries:
tkinter (built-in)
pyzipper
hashlib
os
time
datetime
Enhancements
Potential enhancements include:

Adding support for additional archive formats.
Improving password strength validation.
Including error recovery mechanisms for failed operations.
Enjoy using the File Compression and Decompression Tool!
