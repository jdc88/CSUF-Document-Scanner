## Overview
This project is a GUI-based tool designed to analyze student documents, detect plagiarism, compress text data, and visualize citation structures using various algorithmic techniques. It integrates string matching, compression, sorting, and graph traversal to demonstrate practical applications of computer science algorithms.

## How to Run

1. Ensure you have Python installed.
2. Install required libraries
3. Run the application:
   ```
   python main_GUI.py
   ```

## Features

- **Plagiarism Detection:**  
  Uses Rabin-Karp, KMP, and Naive Search to compare documents and highlight duplicated content.

- **Compression:**  
  Implements Huffman Coding to reduce the file size of text inputs after analysis.

- **Citation Graphs:**  
  Uses BFS and DFS traversal on document references and visualizes the citation structure using NetworkX and Matplotlib.

- **Sorting:**  
  Applies Merge Sort and Counting Sort to organize files by author, title, or date.

- **User Interface:**  
  Built with Tkinter for ease of use, allowing file upload, search execution, and results display.

## File Structure

```
.
├── Algorithms/
│   ├── bfs.py
│   ├── dfs.py
│   ├── huffman_encoding.py
│   ├── kmp_algorithm.py
│   ├── naive_search.py
│   ├── quick.py
│   ├── rabin_karp.py
│   └── radix.py
│
├── Text Files/
│   ├── text1.txt
│   ├── text2.txt
│   ├── text3.txt
│   ├── text4.txt
│   ├── text5.txt
│   └── text6.txt
│
├── __pycache__/
├── main_GUI.py              # Main program file to run the GUI
├── read_file_logic.py       # Handles reading and parsing uploaded text files
├── test.py                  # Script for running algorithm test cases (old file)
├── README.md                # GitHub-formatted README (this file)
├── Old_main_gui_code.txt    # Previous GUI version (for backup/reference)
```

## Credits

All team members contributed collaboratively.  
- **Frank** focused on file reading and backend integration.  
- **Paul** led the UI development.  
- **JC** handled the plagiarism detection modules.
