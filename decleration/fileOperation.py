import os

def check_file_param(file: str) -> str:
    """Checks if input is a path, otherwise assumes input is file content

    Args:
        file (str): file path or file text content

    Returns:
        str: file content
    """
    if os.path.isfile(file):
        with open(file, "r") as f:
            return f.read()

    return file

