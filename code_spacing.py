import re
from typing import Union, List

def normalize_code_spacing(code: Union[str, List[str]]) -> Union[str, List[str]]:
    """
    Adds spaces around punctuations and symbols in Python code to improve readability.
    Handles both single-line code (as a string) and multi-line code (as a list of strings).
    
    Parameters:
    - code: str or List[str] : A string (one line) or list of strings (multiple lines) containing the Python code.

    Returns:
    - str or List[str] : The formatted code with spaces around symbols and punctuations.
    """
    # Define a regular expression to match all punctuations and symbols
    punctuation_pattern = r"([\[\]\(\)\{\}\'\"\=\+\-\*\%\/\:\,\.])"

    def format_line(line: str) -> str:
        # Add spaces around all matched punctuation and symbols
        spaced_line = re.sub(punctuation_pattern, r" \1 ", line)
        # Replace multiple spaces with a single space
        spaced_line = re.sub(r'\s+', ' ', spaced_line).strip()
        return spaced_line

    # Check if input is a list of strings (multi-line) or a single string
    if isinstance(code, list):
        # Process each line in the list
        return [format_line(line) for line in code]
    elif isinstance(code, str):
        # Process a single line of code
        return format_line(code)
    else:
        raise TypeError("Input must be a string or a list of strings.")
