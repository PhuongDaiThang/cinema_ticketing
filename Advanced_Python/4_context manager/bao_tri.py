def process_file(filename):
    with open(filename, "r") as file:
        content = file.read()
        # Xử lý nội dung tập tin
        print(content)

# Sử dụng hàm `process_file` để xử lý nhiều tập tin
process_file("4_context manager/data1.txt")
process_file("4_context manager/data2.txt")