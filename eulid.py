from datetime import datetime  # Nhập module datetime để lấy thời gian hiện tại

# Hàm extended_gcd tính ước chung lớn nhất (GCD) của a và b và trả về các hệ số x, y sao cho a*x + b*y = GCD(a, b)
def extended_gcd(a, b):
    if b == 0:  # Nếu b = 0, GCD(a, b) là a, với x = 1 và y = 0
        return a, 1, 0
    # Đệ quy gọi extended_gcd(b, a % b) để tìm GCD của a và b
    d, x1, y1 = extended_gcd(b, a % b)
    # Trả về d (GCD), x và y sao cho a*x + b*y = d
    return d, y1, x1 - (a // b) * y1  # Sử dụng công thức đệ quy để tính x và y

# Hàm mod_inverse tính nghịch đảo của a mod m
def mod_inverse(a, m):
    d, x, _ = extended_gcd(a, m)  # Tìm GCD(a, m) và các hệ số x, y
    if d != 1:  # Nếu GCD(a, m) khác 1, không có nghịch đảo tồn tại
        return None  # Trả về None nếu không có nghịch đảo
    return x % m  # Trả về x modulo m, đảm bảo giá trị trong phạm vi 0 đến m-1

# Ví dụ: Tính nghịch đảo của 7 mod 26
a, m = 7, 26  # Đặt giá trị a = 7 và m = 26
inv = mod_inverse(a, m)  # Tính nghịch đảo của a mod m
# In ra kết quả nghịch đảo và thời gian hiện tại
print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Nghịch đảo của {a} mod {m} là: {inv}")

