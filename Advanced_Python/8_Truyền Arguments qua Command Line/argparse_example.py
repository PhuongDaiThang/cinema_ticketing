import argparse

# Tạo đối tượng ArgumentParser
parser = argparse.ArgumentParser(description="Python Position argument")

# Thêm arguments
parser.add_argument("x", type=int, help="Specify x")
parser.add_argument("y", type=int, help="Specify y")
parser.add_argument("-a", "--alp", required=True, type=int, help="Specify alpha")
parser.add_argument("-b", "--bet", type=int, default=5, help="Specify beta")

# Phân tích arguments
args = parser.parse_args()

# Truy cập và sử dụng arguments
print(f"Input X: {args.x}")
print(f"Input Y: {args.y}")
print(f"Input A: {args.alp}")
print(f"Input B: {args.bet}")
#print(f"Output: {args.x + args.y}")