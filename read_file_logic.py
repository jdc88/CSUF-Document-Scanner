# Logic for reading the file

def read_file(file_p):
    try:
        # UTF - 8 is standard for reading files to include special symbols
        # Using with open() has a subsequent close() after
        with open(file_p, 'r', encoding = 'utf-8') as file:
            return file.read()

    # Exception handling
    except FileNotFoundError:
        print(f"Error: The file at {filePath} was not found.")
        return None
    except Exception as e:
        print(f"An error occured while reading the file: {e}")
        return None
