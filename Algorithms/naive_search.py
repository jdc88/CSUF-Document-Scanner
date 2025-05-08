# Naive String Matching

def naive_search(text, pattern):
    positions = [] # To store indices where pattern is found
    n = len(text)
    m = len(pattern)

    # Makes capital lettered words to lowercase for uniformity of calculation
    text_lower = text.lower()
    pattern_lower = pattern.lower()

    # Loop through all possible starting positions
    for i in range(n - m + 1):
        match = True
        for j in range(m): # Compare each character
            if text_lower[i + j] != pattern_lower[j]: 
                match = False # Mismatch found
                break
        if match:
            positions.append(i) # Store the index of the match
    return positions

# Example input (hard-coded)
#text = "Hello World, this is Computer Science !!!"
#pattern = "Computer"

# Output
#print("Naive Search Matching found at: ", naive_search(text, pattern))
