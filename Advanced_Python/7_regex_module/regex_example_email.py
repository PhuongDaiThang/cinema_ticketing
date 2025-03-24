# Tìm kiếm email trong chuỗi
import re

text = "This is an email address: example@email.com. You can also contact us at another@email.org."

pattern = r"[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
matches = re.findall(pattern, text)
print(matches)  # Output: ['example@email.com', 'another@email.org']