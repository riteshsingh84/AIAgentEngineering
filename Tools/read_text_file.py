
def read_text_file(file_path):

    """Read the contents of a text/md file specified by the file path and return it as a string."""
    
    if not file_path:
        return "Error reading file: No file path provided"
    
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "Error reading file: File not found" 
    except Exception as e:
        return f"Error reading file: {e}"