# Xác thực số điện thoại
import re

phone_number = "+84 123 456 789"

pattern = r"\+84\s[0-9]{3}\s[0-9]{3}\s[0-9]{3}"
is_valid = re.match(pattern, phone_number) is not None
print(is_valid)  # Output: True