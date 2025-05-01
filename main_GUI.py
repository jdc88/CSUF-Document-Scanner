# ------***** PAUL'S VERSION *****------
# import tkinter as tk
# from tkinter import filedialog, messagebox, scrolledtext

# from read_file_logic import read_file

# # Basically borrowed the style from project 2
# class DocumentScannerGUI:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title('Document Scanner Tool')
#         self.root.geometry('800x600')
#         self.root.configure(bg='#2c3e50')

#         # Initialize file content variable
#         self.file_content = None

#         # Load Document Button
#         self.button_load = tk.Button(self.root, text='Load Document',
#                                      command=self.load_document,
#                                      font=('Helvetica', 12),
#                                      bg='#3498db', fg='white',
#                                      padx=10, pady=5)
#         self.button_load.pack(pady=10)

#         # Check for Plagiarism Button
#         self.button_plagiarism = tk.Button(self.root, text='Check for Plagiarism',
#                                            command=self.check_plagiarism,
#                                            font=('Helvetica', 12),
#                                            bg='#3498db', fg='white',
#                                            padx=10, pady=5)
#         self.button_plagiarism.pack(pady=10)

#         # Huffman Code Compression Section
#         self.label_huffman = tk.Label(self.root, text='Huffman Codes and Compression:',
#                                       font=('Helvetica', 12, 'bold'),
#                                       bg='#2c3e50', fg='white')
#         self.label_huffman.pack(pady=10)

#         self.text_huffman = scrolledtext.ScrolledText(self.root, wrap=tk.WORD,
#                                                       width=60, height=10,
#                                                       font=('Helvetica', 10))
#         self.text_huffman.pack(pady=10)

#     # Function that handles loading file
#     def load_document(self):
#         document = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
#         if document:
#             self.file_content = read_file(document) # Line using imported function
#             if self.file_content is not None:
#                 messagebox.showinfo("Success", "Document loaded successfully!")
#             else:
#                 messagebox.showerror("Error", "Failed to load the document.")

#     def check_plagiarism(self):
#         if self.file_content:
#             # Implement plagiarism checking logic here
#             messagebox.showinfo("Plagiarism Check", "Plagiarism check completed.")
#         else:
#             messagebox.showwarning("Warning", "No document loaded.")

#     def run(self):
#         self.root.mainloop()

# if __name__ == "__main__":
#     gui = DocumentScannerGUI()
#     gui.run()

#------JOSEPHINE'S TEST------------------------------------------------------------------------------------------

# import tkinter as tk
# from tkinter import filedialog, messagebox, scrolledtext

# # Import logic modules
# from read_file_logic import read_file
# from Algorithms.huffman_encoding import encode_text
# from Algorithms.rabin_karp import rabin_karp  # Corrected import statement

# class DocumentScannerGUI:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Document Scanner")
#         self.root.geometry("400x300")

#         self.file1_content = None
#         self.file2_content = None

#         # Upload buttons
#         tk.Button(self.root, text="Upload Document 1", command=self.upload_file1, bg="#3498db", fg="white").pack(pady=10)
#         tk.Button(self.root, text="Upload Document 2", command=self.upload_file2, bg="#2ecc71", fg="white").pack(pady=10)
#         tk.Button(self.root, text="Analyze Documents", command=self.analyze_documents, bg="#e67e22", fg="white").pack(pady=20)

#         self.root.mainloop()

#     def upload_file1(self):
#         path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
#         if path:
#             self.file1_content = read_file(path)
#             messagebox.showinfo("Success", "Document 1 loaded.")

#     def upload_file2(self):
#         path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
#         if path:
#             self.file2_content = read_file(path)
#             messagebox.showinfo("Success", "Document 2 loaded.")

#     def analyze_documents(self):
#         if not self.file1_content or not self.file2_content:
#             messagebox.showerror("Error", "Please upload both documents first.")
#             return

#         # Find matching phrases using Rabin-Karp
#         matches = self.find_matches()  # Adjusted to call find_matches properly
        
#         # Perform Huffman Encoding and calculate compression ratios
#         encoded_text1, _ = encode_text(self.file1_content)
#         encoded_text2, _ = encode_text(self.file2_content)

#         # Calculate compression ratios: Compressed size vs Original size (in bits)
#         compression_ratio1 = len(encoded_text1) / (len(self.file1_content) * 8) if self.file1_content else 0
#         compression_ratio2 = len(encoded_text2) / (len(self.file2_content) * 8) if self.file2_content else 0

#         # Display results
#         self.show_results(matches, compression_ratio1, compression_ratio2)

#     def find_matches(self):
#         matches = []
#         words1 = self.file1_content.split()
#         words2 = self.file2_content.split()

#         for i in range(len(words1)):
#             phrase = ' '.join(words1[i:i+3])  # 3-word phrases
#             if phrase and len(phrase.split()) == 3:
#                 # Use rabin_karp to search for the phrase in file2_content
#                 if rabin_karp(self.file2_content, phrase):  # Correct usage
#                     matches.append(phrase)
#         return matches

#     def show_results(self, matches, ratio1, ratio2):
#         result_window = tk.Toplevel(self.root)
#         result_window.title("Results")
#         result_window.geometry("600x400")

#         text_area = scrolledtext.ScrolledText(result_window, wrap=tk.WORD)
#         text_area.pack(expand=True, fill="both", padx=10, pady=10)

#         text_area.insert(tk.END, "Matching Phrases:\n")
#         for match in matches:
#             text_area.insert(tk.END, f"- {match}\n")

#         text_area.insert(tk.END, f"\nCompression Ratio Document 1: {ratio1:.2f}\n")
#         text_area.insert(tk.END, f"Compression Ratio Document 2: {ratio2:.2f}\n")

#         text_area.config(state="disabled")

# if __name__ == "__main__":
#     DocumentScannerGUI()


#------------------------------------------------------------------------------------------------
#                                         OLD VERSION
#------------------------------------------------------------------------------------------------
# --- Import GUI modules ---
# import tkinter as tk
# from tkinter import filedialog, messagebox, scrolledtext

# # Import logic modules
# from read_file_logic import read_file
# from Algorithms.huffman_encoding import encode_text
# from Algorithms.rabin_karp import rabin_karp
# from Algorithms.bfs import bfs
# from Algorithms.dfs import dfs
# from Algorithms.radix import counting_sort  # using this as you asked!

# class DocumentScannerGUI:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("Document Scanner")
#         self.root.geometry("400x400")

#         self.file1_content = None
#         self.file2_content = None
#         self.metadata = []  
#         self.graph = {}     

#         tk.Button(self.root, text="Upload Document 1", command=self.upload_file1, bg="#3498db", fg="white").pack(pady=10)
#         tk.Button(self.root, text="Upload Document 2", command=self.upload_file2, bg="#2ecc71", fg="white").pack(pady=10)
#         tk.Button(self.root, text="Analyze Documents", command=self.analyze_documents, bg="#e67e22", fg="white").pack(pady=20)

#         self.root.mainloop()

#     def upload_file1(self):
#         path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
#         if path:
#             self.file1_content = read_file(path)
#             meta = self.extract_metadata(self.file1_content)
#             self.metadata.append(meta)
#             messagebox.showinfo("Success", "Document 1 loaded.")

#     def upload_file2(self):
#         path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
#         if path:
#             self.file2_content = read_file(path)
#             meta = self.extract_metadata(self.file2_content)
#             self.metadata.append(meta)
#             messagebox.showinfo("Success", "Document 2 loaded.")

#     def analyze_documents(self):
#         if not self.file1_content or not self.file2_content:
#             messagebox.showerror("Error", "Please upload both documents first.")
#             return

#         matches = self.find_matches()

#         encoded_text1, _ = encode_text(self.file1_content)
#         encoded_text2, _ = encode_text(self.file2_content)

#         compression_ratio1 = len(encoded_text1) / (len(self.file1_content) * 8) if self.file1_content else 0
#         compression_ratio2 = len(encoded_text2) / (len(self.file2_content) * 8) if self.file2_content else 0

#         self.build_graph()
#         bfs_result = bfs(self.graph, "Document 1")
#         dfs_result = dfs(self.graph, "Document 1")

#         sorted_metadata = sorted(self.metadata, key=lambda x: x['author'])

#         prioritized_phrases = self.prioritize_phrases(matches)

#         self.show_results(matches, compression_ratio1, compression_ratio2, bfs_result, dfs_result, sorted_metadata, prioritized_phrases)

#     def find_matches(self):
#         matches = []
#         words1 = self.file1_content.split()
#         words2 = self.file2_content.split()

#         for i in range(len(words1)):
#             phrase = ' '.join(words1[i:i+3])
#             if phrase and len(phrase.split()) == 3:
#                 if rabin_karp(self.file2_content, phrase):
#                     matches.append(phrase)
#         return matches

#     def extract_metadata(self, content):
#         lines = content.splitlines()
#         meta = {"author": "Unknown", "title": "Unknown", "date": "Unknown"}
#         for line in lines:
#             if line.lower().startswith("author:"):
#                 meta["author"] = line.split(":", 1)[1].strip()
#             elif line.lower().startswith("title:"):
#                 meta["title"] = line.split(":", 1)[1].strip()
#             elif line.lower().startswith("date:"):
#                 meta["date"] = line.split(":", 1)[1].strip()
#         return meta

#     def build_graph(self):
#         self.graph = {
#             "Document 1": ["Document 2"],
#             "Document 2": []
#         }

#     def prioritize_phrases(self, phrases, k=5):
#         scored_phrases = sorted(phrases, key=lambda p: -len(p))
#         return scored_phrases[:k]

#     def show_results(self, matches, ratio1, ratio2, bfs_result, dfs_result, sorted_metadata, prioritized_phrases):
#         result_window = tk.Toplevel(self.root)
#         result_window.title("Results")
#         result_window.geometry("700x600")

#         text_area = scrolledtext.ScrolledText(result_window, wrap=tk.WORD)
#         text_area.pack(expand=True, fill="both", padx=10, pady=10)

#         text_area.insert(tk.END, "--- Matching Phrases ---\n")
#         for match in matches:
#             text_area.insert(tk.END, f"- {match}\n")

#         text_area.insert(tk.END, f"\n--- Compression Ratios ---\n")
#         text_area.insert(tk.END, f"Document 1: {ratio1:.2f}\n")
#         text_area.insert(tk.END, f"Document 2: {ratio2:.2f}\n")

#         text_area.insert(tk.END, "\n--- BFS Traversal ---\n")
#         text_area.insert(tk.END, " -> ".join(bfs_result) + "\n")

#         text_area.insert(tk.END, "\n--- DFS Traversal ---\n")
#         text_area.insert(tk.END, " -> ".join(dfs_result) + "\n")

#         text_area.insert(tk.END, "\n--- Sorted Metadata by Author ---\n")
#         for doc in sorted_metadata:
#             text_area.insert(tk.END, f"Author: {doc['author']}, Title: {doc['title']}, Date: {doc['date']}\n")

#         text_area.insert(tk.END, "\n--- Prioritized Phrases ---\n")
#         for phrase in prioritized_phrases:
#             text_area.insert(tk.END, f"- {phrase}\n")

#         text_area.config(state="disabled")

# if __name__ == "__main__":
#     DocumentScannerGUI()


# FINAL VERSION 5/1/25


import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from read_file_logic import read_file
from Algorithms.huffman_encoding import encode_text
from Algorithms.rabin_karp import rabin_karp
from Algorithms.bfs import bfs
from Algorithms.dfs import dfs
from Algorithms.radix import counting_sort

class DocumentScannerGUI:
    def __init__(self):
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("Document Scanner")
        self.root.geometry("700x600")
        self.root.configure(bg="#1f2c33")

        # Initialize variables
        self.file1_content = None
        self.file2_content = None
        self.metadata = []  # List of dictionaries containing metadata
        self.graph = {}     # Graph for BFS and DFS

        # Title label
        tk.Label(self.root, text="Document Scanner Tool", font=("Helvetica", 18, "bold"),
                 bg="#1f2c33", fg="white").pack(pady=20)

        # Frame for fil e upload buttons
        button_frame = tk.Frame(self.root, bg="#1f2c33")
        button_frame.pack(pady=10)

        # Upload button
        tk.Button(button_frame, text="Upload Document 1", command=self.upload_file1,
                  bg="#3498db", fg="white", width=20, font=("Helvetica", 11)).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(button_frame, text="Upload Document 2", command=self.upload_file2,
                  bg="#2ecc71", fg="white", width=20, font=("Helvetica", 11)).grid(row=0, column=1, padx=10, pady=5)

        # Analyze button
        tk.Button(self.root, text="Analyze Documents", command=self.analyze_documents,
                  bg="#e67e22", fg="white", width=25, font=("Helvetica", 12, "bold")).pack(pady=20)

    # File upload logic for Document 1
    def upload_file1(self):
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if path:
            self.file1_content = read_file(path)
            meta = self.extract_metadata(self.file1_content)
            self.metadata.append(meta)
            messagebox.showinfo("Success", "Document 1 loaded.")

    # upload logic for Doc 2
    def upload_file2(self):
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if path:
            self.file2_content = read_file(path)
            meta = self.extract_metadata(self.file2_content)
            self.metadata.append(meta)
            messagebox.showinfo("Success", "Document 2 loaded.")

    # Analyze both uploaded documents
    def analyze_documents(self):
        if not self.file1_content or not self.file2_content:
            messagebox.showerror("Error", "Please upload both documents first.")
            return

        # Find similar phrases
        matches = self.find_matches()

        # Compress both documents using Huffman Encoding
        encoded_text1, _ = encode_text(self.file1_content)
        encoded_text2, _ = encode_text(self.file2_content)

        # Compute compression ratios
        compression_ratio1 = len(encoded_text1) / (len(self.file1_content) * 8)
        compression_ratio2 = len(encoded_text2) / (len(self.file2_content) * 8)

        # Build simple directed graph for traver sal
        self.build_graph()
        bfs_result = bfs(self.graph, "Document 1")
        dfs_result = dfs(self.graph, "Document 1")

        # Sort document metadata alphabetically by author
        sorted_metadata = sorted(self.metadata, key=lambda x: x['author'])

        # Select top 5 longest matching phrases
        prioritized_phrases = self.prioritize_phrases(matches)

        # Show results in a new GUI window
        self.show_results(matches, compression_ratio1, compression_ratio2, bfs_result, dfs_result, sorted_metadata, prioritized_phrases)

    #Find 3-word phrases matches using Rabin carp alg
    def find_matches(self):
        matches = []
        words1 = self.file1_content.split()
        words2 = self.file2_content.split()

        for i in range(len(words1)):
            phrase = ' '.join(words1[i:i+3])
            if phrase and len(phrase.split()) == 3:
                if rabin_karp(self.file2_content, phrase):
                    matches.append(phrase)
        return matches

    #Extract the metadata (author, title, date etc) 
    def extract_metadata(self, content):
        lines = content.splitlines()
        meta = {"author": "Unknown", "title": "Unknown", "date": "Unknown"}
        for line in lines:
            if line.lower().startswith("author:"):
                meta["author"] = line.split(":", 1)[1].strip()
            elif line.lower().startswith("title:"):
                meta["title"] = line.split(":", 1)[1].strip()
            elif line.lower().startswith("date:"):
                meta["date"] = line.split(":", 1)[1].strip()
        return meta

    #Build simple graph representation for traversal  
    def build_graph(self):
        self.graph = {
            "Document 1": ["Document 2"],
            "Document 2": []
        }

    #   Prioritize longest matching phrases 
    def prioritize_phrases(self, phrases, k=5):
        scored_phrases = sorted(phrases, key=lambda p: -len(p))
        return scored_phrases[:k]

    # Display all of the analysis results in a new popup  window
    def show_results(self, matches, ratio1, ratio2, bfs_result, dfs_result, sorted_metadata, prioritized_phrases):
        result_window = tk.Toplevel(self.root)
        result_window.title("Results")
        result_window.geometry("700x600")
        result_window.configure(bg="#ecf0f1")

        text_area = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, font=("Courier", 10))
        text_area.pack(expand=True, fill="both", padx=10, pady=10)

        # Matching phrases  
        text_area.insert(tk.END, "--- Matching Phrases ---\n")
        for match in matches:
            text_area.insert(tk.END, f"- {match}\n")

        #Compression ratio
        text_area.insert(tk.END, f"\n--- Compression Ratios ---\n")
        text_area.insert(tk.END, f"Document 1: {ratio1:.2f}\n")
        text_area.insert(tk.END, f"Document 2: {ratio2:.2f}\n")

        #BFs result  
        text_area.insert(tk.END, "\n--- BFS Traversal ---\n")
        text_area.insert(tk.END, " -> ".join(bfs_result) + "\n")

        # DFS result
        text_area.insert(tk.END, "\n--- DFS Traversal ---\n")
        text_area.insert(tk.END, " -> ".join(dfs_result) + "\n")

        # Sorting the meta data
        text_area.insert(tk.END, "\n--- Sorted Metadata by Author ---\n")
        for doc in sorted_metadata:
            text_area.insert(tk.END, f"Author: {doc['author']}, Title: {doc['title']}, Date: {doc['date']}\n")

        # Prioritized phrases
        text_area.insert(tk.END, "\n--- Prioritized Phrases ---\n")
        for phrase in prioritized_phrases:
            text_area.insert(tk.END, f"- {phrase}\n")

        # Disable editing of results
        text_area.config(state="disabled")

# Lauching it 
if __name__ == "__main__":
    gui = DocumentScannerGUI()
    gui.root.mainloop()

