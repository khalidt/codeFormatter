# codeFormatter

**codeFormatter** is a Python library that helps you normalize code by adding spaces around punctuation marks and symbols, making your code more readable and well-formatted.

## Features

- Adds spaces around common punctuation and symbols such as `[]`, `{}`, `()`, `=`, `+`, `-`, `*`, `/`, etc.
- Handles both single-line and multi-line code.
- Easy to integrate into any Python project.

## Installation

You can install the library using pip:

```bash
pip install codeFormatter
```

Or, if you're developing locally:

```bash
pip install .
```

## Usage

Here’s how you can use the `codeFormatter` library to normalize code spacing:

### Single-line Code Example

```python
from codeFormatter import normalize_code_spacing

code = "custom['age']= 30"
formatted_code = normalize_code_spacing(code)
print(f'Formatted code: "{formatted_code}"')
```

### Multi-line Code Example

```python
from codeFormatter import normalize_code_spacing

code_lines = [
    "custom['age']= 30",
    "if x == 5: print(x)"
]
formatted_code_lines = normalize_code_spacing(code_lines)
print("Formatted multi-line code:")
for line in formatted_code_lines:
    print(f'"{line}"')
```

### Output

```text
Formatted code: "custom [ ' age ' ] = 30"
Formatted multi-line code:
"custom [ ' age ' ] = 30"
"if x == 5 : print ( x )"
```

