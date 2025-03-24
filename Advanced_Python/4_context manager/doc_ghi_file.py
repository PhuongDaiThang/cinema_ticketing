with open("4_context manager/filename.txt", "r") as file:
    content = file.read()
    print(content)

with open("4_context manager/filename.txt", "w") as file:
    file.write("This is some text to write.")
