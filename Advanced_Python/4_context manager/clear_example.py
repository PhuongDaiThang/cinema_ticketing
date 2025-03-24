import os

with open("4_context manager/temp.txt", "w") as temp_file:
    temp_file.write("This is some temporary data.")

print("Temporary data written to file.")

# Tập tin temp.txt sẽ được tự động đóng sau khi khối `with` kết thúc.