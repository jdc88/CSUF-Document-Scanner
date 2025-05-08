# ------***** PAUL'S VERSION *****------
# # Logic for reading the file

# def read_file(file_p):
#     try:
#         # UTF - 8 is standard for reading files to include special symbols
#         # Using with open() has a subsequent close() after
#         with open(file_p, 'r', encoding = 'utf-8') as file:
#             return file.read()

#     # Exception handling
#     except FileNotFoundError:
#         print(f"Error: The file at {filePath} was not found.")
#         return None
#     except Exception as e:
#         print(f"An error occured while reading the file: {e}")
#         return None

#------------------------------------------------------------------------------------------------

# Logic for reading the file

def read_file(file_path):
    """
    This function reads a text file and returns its contents as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file {file_path}: {e}")
