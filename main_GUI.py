# FINAL VERSION 5/8/25

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os # For getting file names
#------ Citation graphs
import re
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
#------ Scanner logic
from read_file_logic import read_file
#------ Algorithms
from Algorithms.huffman_encoding import encode_text
from Algorithms.rabin_karp import rabin_karp
from Algorithms.bfs import bfs
from Algorithms.dfs import dfs
from Algorithms.radix import counting_sort
from Algorithms.naive_search import naive_search
from Algorithms.quick import quick_sort

class DocumentScannerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Document Scanner")
        self.root.geometry("750x400")
        self.root.configure(bg="#1f2c33")

        self.file1_content = None
        self.file2_content = None
        self.file1_name = "No Document Loaded"
        self.file2_name = "No Document Loaded"
        self.metadata = []
        self.graph = {}

        tk.Label(self.root, text="Document Scanner Tool", font=("Helvetica", 18, "bold"),
                 bg="#1f2c33", fg="white").pack(pady=20)

        button_frame = tk.Frame(self.root, bg="#1f2c33")
        button_frame.pack(pady=10)

        # Upload Document 1
        tk.Button(button_frame, text="Upload Document 1", command=self.upload_file1,
                  bg="#3498db", fg="white", width=20, font=("Helvetica", 11)).grid(row=0, column=0, padx=10, pady=5)
        self.file1_label = tk.Label(button_frame, text=self.file1_name, bg="#1f2c33", fg="white", font=("Helvetica", 10))
        self.file1_label.grid(row=0, column=1, padx=10)

        # Upload Document 2
        tk.Button(button_frame, text="Upload Document 2", command=self.upload_file2,
                  bg="#2ecc71", fg="white", width=20, font=("Helvetica", 11)).grid(row=1, column=0, padx=10, pady=5)
        self.file2_label = tk.Label(button_frame, text=self.file2_name, bg="#1f2c33", fg="white", font=("Helvetica", 10))
        self.file2_label.grid(row=1, column=1, padx=10)

        tk.Button(self.root, text="Analyze Documents", command=self.analyze_documents,
                  bg="#e67e22", fg="white", width=25, font=("Helvetica", 12, "bold")).pack(pady=20)

        # Add search input for real-time search
        search_frame = tk.Frame(self.root, bg="#1f2c33")
        search_frame.pack(pady=10)

        self.search_entry = tk.Entry(search_frame, width=30, font=("Helvetica", 12))
        self.search_entry.grid(row=0, column=0, padx=10, pady=5)

        # Document 1
        tk.Button(search_frame, text="Search Document 1", command=self.search_document1,
                  bg="#f39c12", fg="white", width=20, font=("Helvetica", 11)).grid(row=0, column=1, padx=10, pady=5)

        # Document 2
        tk.Button(search_frame, text="Search Document 2", command=self.search_document2,
                  bg="#f39c12", fg="white", width=20, font=("Helvetica", 11)).grid(row=0, column=2, padx=10, pady=5)

        # Reset Button
        tk.Button(self.root, text="Reset", command=self.reset_data,
                  bg="#e74c3c", fg="white", width=25, font=("Helvetica", 12, "bold")).pack(pady=10)

    def upload_file1(self):
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if path:
            self.file1_content = read_file(path)
            meta = self.extract_metadata(self.file1_content)
            self.metadata.append(meta)
            self.file1_name = os.path.basename(path)  # Get file1 name for citation graph display
            self.file1_label.config(text=self.file1_name)  # Update Document 1 Label
            messagebox.showinfo("Success", "Document 1 loaded.")

    def upload_file2(self):
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if path:
            self.file2_content = read_file(path)
            meta = self.extract_metadata(self.file2_content)
            self.metadata.append(meta)
            self.file2_name = os.path.basename(path)  # Get file2 name for citation graph display
            self.file2_label.config(text=self.file2_name)  # Update Document 2 Label
            messagebox.showinfo("Success", "Document 2 loaded.")

    def analyze_documents(self):
        if not self.file1_content or not self.file2_content:
            messagebox.showerror("Error", "Please upload both documents first.")
            return

        matches = self.find_matches()
        encoded_text1, _ = encode_text(self.file1_content)
        encoded_text2, _ = encode_text(self.file2_content)

        compression_ratio1 = len(encoded_text1) / (len(self.file1_content) * 8)
        compression_ratio2 = len(encoded_text2) / (len(self.file2_content) * 8)

        self.build_graph()
        bfs_result = bfs(self.graph, "Document 1")
        dfs_result = dfs(self.graph, "Document 1")

        # Using Quick Sort to sort metadata by Author
        sorted_metadata = quick_sort(self.metadata, key=lambda x: x['author'])
        prioritized_phrases = self.prioritize_phrases(matches)

        similarity_percent = self.calculate_similarity(matches)

        self.show_results(matches, compression_ratio1, compression_ratio2,
                          bfs_result, dfs_result, sorted_metadata,
                          prioritized_phrases, similarity_percent)

        # Citation graph
        docs_with_authors = {}
        for i, content in enumerate([self.file1_content, self.file2_content]):
            meta = self.metadata[i]
            author = meta["author"]
            cited_authors = self.extract_citations(content)
            docs_with_authors[author] = cited_authors

        citation_graph = self.build_citation_graph(docs_with_authors)
        self.visualize_graph(citation_graph)

        # Visualize similarity
        self.visualize_similarity(similarity_percent)

    # Using Rabin Karp Algorithm
    def find_matches(self):
        matches = []
        words1 = self.file1_content.split()
        for i in range(len(words1) - 2):
            phrase = ' '.join(words1[i:i + 3])
            if rabin_karp(self.file2_content, phrase):
                matches.append(phrase)
        return matches

    def calculate_similarity(self, matches):
        phrases1 = set([' '.join(self.file1_content.split()[i:i+3]) for i in range(len(self.file1_content.split()) - 2)])
        phrases2 = set([' '.join(self.file2_content.split()[i:i+3]) for i in range(len(self.file2_content.split()) - 2)])
        total_phrases = len(phrases1.union(phrases2))
        match_count = len(set(matches))
        return (match_count / total_phrases) * 100 if total_phrases else 0

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

    def build_graph(self):
        self.graph = {
            "Document 1": ["Document 2"],
            "Document 2": []
        }

    def prioritize_phrases(self, phrases, k=5):
        scored_phrases = sorted(phrases, key=lambda p: -len(p))
        return scored_phrases[:k]

    def show_results(self, matches, ratio1, ratio2, bfs_result, dfs_result, sorted_metadata, prioritized_phrases, similarity_percent):
        result_window = tk.Toplevel(self.root)
        result_window.title("Results")
        result_window.geometry("700x600")
        result_window.configure(bg="#ecf0f1")

        text_area = scrolledtext.ScrolledText(result_window, wrap=tk.WORD, font=("Courier", 10))
        text_area.pack(expand=True, fill="both", padx=10, pady=10)

        text_area.insert(tk.END, "--- Matching Phrases ---\n")
        for match in matches:
            text_area.insert(tk.END, f"- {match}\n")

        text_area.insert(tk.END, f"\n--- Compression Ratios ---\n")
        text_area.insert(tk.END, f"Document 1: {ratio1:.2f}\n")
        text_area.insert(tk.END, f"Document 2: {ratio2:.2f}\n")

        text_area.insert(tk.END, f"\n--- Similarity Index ---\n")
        text_area.insert(tk.END, f"{similarity_percent:.2f}%\n")

        text_area.insert(tk.END, "\n--- BFS Traversal ---\n")
        text_area.insert(tk.END, " -> ".join(bfs_result) + "\n")

        text_area.insert(tk.END, "\n--- DFS Traversal ---\n")
        text_area.insert(tk.END, " -> ".join(dfs_result) + "\n")

        text_area.insert(tk.END, "\n--- Quick Sorted Metadata by Author ---\n")
        for doc in sorted_metadata:
            text_area.insert(tk.END, f"Author: {doc['author']}, Title: {doc['title']}, Date: {doc['date']}\n")

        text_area.insert(tk.END, "\n--- 5 Longest Phrases Matched ---\n")
        for phrase in prioritized_phrases:
            text_area.insert(tk.END, f"- {phrase}\n")

        text_area.config(state="disabled")

    def extract_citations(self, text):
        pattern = r"\b([A-Z][a-z]+(?: et al\.)?)\s*\(\d{4}\)"
        return re.findall(pattern, text)

    def build_citation_graph(self, docs_with_authors):
        G = nx.DiGraph()
        for author, cited_authors in docs_with_authors.items():
            G.add_node(author)
            for cited in cited_authors:
                G.add_edge(author, cited)
        return G

    def visualize_graph(self, G):
        title = f"Citation Graph\n {self.file1_name} and {self.file2_name}" # For dynamic display of which files are used for citation graph
        graph_window = tk.Toplevel()
        graph_window.title(title)
        graph_window.geometry("900x600")
        graph_window.configure(bg="#ffffff")

        fig, ax = plt.subplots(figsize=(8, 6))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000, arrows=True, ax=ax)
        ax.set_title(title)

        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both")
        plt.close(fig)

    def visualize_similarity(self, similarity_percent):
        graph_window = tk.Toplevel()
        bar_title = f"Comparison Between\n {self.file1_name} and {self.file2_name}" # For dynamic display of which files are used for bar graph
        graph_window.title(bar_title)
        graph_window.geometry("500x400")

        fig, ax = plt.subplots(figsize=(5, 4))
        categories = ['Similarity', 'Difference']
        values = [similarity_percent, 100 - similarity_percent]
        ax.bar(categories, values, color=['#27ae60', '#c0392b'])
        ax.set_ylim(0, 100)
        ax.set_ylabel('Percentage')
        ax.set_title(bar_title)
        ax.set_yticks(range(0, 101, 5))

        # This displays percentage inside the bar
        bars = ax.bar(categories, values, color=['#27ae60', '#c0392b'])
        
        for bar, value in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 5, f"{value:.2f}%", 
                ha='center', va='bottom', color='blue', fontweight='bold')

        canvas = FigureCanvasTkAgg(fig, master=graph_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        plt.close(fig)

    # Uses naive search to find words/phrases for Document 1
    def search_document1(self):
        search_term = self.search_entry.get()
        if not self.file1_content:
            messagebox.showerror("Error", "Please upload Document 1 first.")
            return

        positions = naive_search(self.file1_content, search_term)
        count = len(positions)
        
        if positions:
            messagebox.showinfo("Search Results", f"'{search_term}' found {count} times positions: {positions}")
        else:
            messagebox.showinfo("Search Results", f"'{search_term}' not found.")

    # Uses naive search to find words/phrases for Document 2
    def search_document2(self):
        search_term = self.search_entry.get()
        if not self.file2_content:
            messagebox.showerror("Error", "Please upload Document 2 first.")
            return

        positions = naive_search(self.file2_content, search_term)
        count = len(positions)

        if positions:
            messagebox.showinfo("Search Results", f"'{search_term}' found {count} times in Document 2 at positions: {positions}")
        else:
            messagebox.showinfo("Search Results", f"'{search_term}' not found in Document 2.")

    # Reset input documents and saved metadata
    def reset_data(self):
        self.file1_content = None
        self.file1_name = "No Document Loaded"
        self.file1_label.config(text=self.file1_name)

        self.file2_content = None
        self.file2_name = "No Document Loaded"
        self.file2_label.config(text=self.file2_name)
        
        self.metadata = []
        self.graph = {}

        messagebox.showinfo("Reset Inputs", "Data has been cleared.")

# ----------------- Launch the GUI ---------------------

if __name__ == "__main__":
    gui = DocumentScannerGUI()
    gui.root.mainloop()
