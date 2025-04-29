# ------***** ORIGNIAL VERSION *****------
# import heapq # Heap Queue for prority queue operations

# # Step 1: Define Huffman Node
# class HuffmanNode:
#     def __init__(self, char, freq):
#         self.char = char
#         self.freq = freq
#         self.left = None
#         self.right = None

#     def __lt__(self, other):
#         return self.freq < other.freq

# # Step 2: Build Huffman Tree
# def build_huffman_tree(freq_map):
#     heap = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
#     heapq.heapify(heap)

#     while len(heap) > 1:
#         left = heapq.heappop(heap)
#         right = heapq.heappop(heap)
#         new_node = HuffmanNode(None, left.freq + right.freq)
#         new_node.left = left
#         new_node.right = right
#         heapq.heappush(heap, new_node)

#     return heap[0]

# # Step 3: Generate Huffman/Assign Codes
# def build_codes(node, prefix="", code_map={}):
#     if node is None:
#         return
#     if node.char is not None:
#         code_map[node.char] = prefix
        
#     build_codes(node.left, prefix + "0", code_map) # Left child (0)
#     build_codes(node.right, prefix + "1", code_map) # Right child (1)

#     return code_map

# # Step 4: Get your input and compute Huffman Encoding
# text = input("Enter the text to encode: ")
# freq_map = {char: text.count(char) for char in set(text)}

# root = build_huffman_tree(freq_map)
# codes = build_codes(root)
# encoded_text = "".join(codes[char] for char in text)

# print("Huffman Codes: ", codes)
# print("Encoded Text: ", encoded_text)

#------------------------------------------------------------------------------------------------

import heapq  # Heap Queue for priority queue operations

# Step 1: Define Huffman Node
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Step 2: Build Huffman Tree
def build_huffman_tree(freq_map):
    heap = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = HuffmanNode(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        heapq.heappush(heap, new_node)

    return heap[0]

# Step 3: Generate Huffman/Assign Codes
def build_codes(node, prefix="", code_map={}):
    if node is None:
        return
    if node.char is not None:
        code_map[node.char] = prefix
        
    build_codes(node.left, prefix + "0", code_map)  # Left child (0)
    build_codes(node.right, prefix + "1", code_map)  # Right child (1)

    return code_map

# Step 4: Function to encode text using Huffman Coding
def encode_text(text: str):
    if not text:
        return "", {}  # Return empty encoded text and code map if text is empty
    
    # Frequency map of characters
    freq_map = {char: text.count(char) for char in set(text)}

    # Build Huffman tree and generate codes
    root = build_huffman_tree(freq_map)
    codes = build_codes(root)
    
    # Encode the text using the generated codes
    encoded_text = "".join(codes[char] for char in text)
    
    return encoded_text, codes  # Return encoded text and the Huffman codes

# Optional: Test the function directly (You can remove this when integrating with the GUI)
if __name__ == "__main__":
    text = input("Enter the text to encode: ")  # For testing purposes only
    encoded_text, codes = encode_text(text)
    print("Huffman Codes: ", codes)
    print("Encoded Text: ", encoded_text)
