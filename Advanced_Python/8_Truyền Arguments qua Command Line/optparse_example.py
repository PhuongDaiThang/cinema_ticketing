import optparse

# Tạo đối tượng OptionParser
parser = optparse.OptionParser()

# Thêm options
parser.add_option("-f", "--file", dest="filename", help="Specify input file")
parser.add_option("-o", "--output", dest="output", help="Specify output file")

# Phân tích options
(options, args) = parser.parse_args()

# Truy cập và sử dụng options
if options.filename:
    print(f"Input file: {options.filename}")

if options.output:
    print(f"Output file: {options.output}")