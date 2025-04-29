import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

from read_file_logic import read_file

# Basically borrowed the style from project 2
class DocumentScannerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Document Scanner Tool')
        self.root.geometry('800x600')
        self.root.configure(bg='#2c3e50')

        # Initialize file content variable
        self.file_content = None

        # Load Document Button
        self.button_load = tk.Button(self.root, text='Load Document',
                                     command=self.load_document,
                                     font=('Helvetica', 12),
                                     bg='#3498db', fg='white',
                                     padx=10, pady=5)
        self.button_load.pack(pady=10)

        # Check for Plagiarism Button
        self.button_plagiarism = tk.Button(self.root, text='Check for Plagiarism',
                                           command=self.check_plagiarism,
                                           font=('Helvetica', 12),
                                           bg='#3498db', fg='white',
                                           padx=10, pady=5)
        self.button_plagiarism.pack(pady=10)

        # Huffman Code Compression Section
        self.label_huffman = tk.Label(self.root, text='Huffman Codes and Compression:',
                                      font=('Helvetica', 12, 'bold'),
                                      bg='#2c3e50', fg='white')
        self.label_huffman.pack(pady=10)

        self.text_huffman = scrolledtext.ScrolledText(self.root, wrap=tk.WORD,
                                                      width=60, height=10,
                                                      font=('Helvetica', 10))
        self.text_huffman.pack(pady=10)

    # Function that handles loading file
    def load_document(self):
        document = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
        if document:
            self.file_content = read_file(document) # Line using imported function
            if self.file_content is not None:
                messagebox.showinfo("Success", "Document loaded successfully!")
            else:
                messagebox.showerror("Error", "Failed to load the document.")

    def check_plagiarism(self):
        if self.file_content:
            # Implement plagiarism checking logic here
            messagebox.showinfo("Plagiarism Check", "Plagiarism check completed.")
        else:
            messagebox.showwarning("Warning", "No document loaded.")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    gui = DocumentScannerGUI()
    gui.run()
