# Thay thế văn bản
import re

text = "Hello, world! This is a sample text."

new_text = re.sub(r"\bworld\b", "Python", text)
print(new_text)  # Output: Hello, Python! This is a sample text.