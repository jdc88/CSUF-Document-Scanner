# Rabin Karp String Matching
# Application: Detecting duplicate phrases in documents

def rabin_karp(text, pattern, q = 101): # Prime number is hard-coded at 101)
    d = 256
    m = len(pattern)
    n = len(text)
    h = pow(d, m - 1) % q # Precompute highest power for rolling hash
    p_hash = 0 # Hash of pattern
    t_hash = 0 # Hash of current window of text
    positions = []

    # Compute initial hash for pattern and first window of the text
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        if p_hash == t_hash:
            if text[i: i + m] == pattern:
                positions.append(i)
        # Calculate hash for next window using rolling hash
        if i < n - m:
            t_hash = (d * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if t_hash < 0:
                t_hash += q # Ensures positive hash
    return positions

# Example Input
#text = "Hello World, this is Computer Science !!!"
#pattern = "Computer"

# Output
#print("Rabin Karp Pattern found at: ", rabin_karp(text, pattern))
