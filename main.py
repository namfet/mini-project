def add(a, b):
    return a + b

if __name__ == "__main__":
    try:
        a = int(input("Nhập số thứ nhất: "))  # Nhập số từ bàn phím
        b = int(input("Nhập số thứ hai: "))   # Nhập số từ bàn phím
        result = add(a, b)
        print("Kết quả:", result)
    except ValueError:
        print("Vui lòng nhập một số hợp lệ.")