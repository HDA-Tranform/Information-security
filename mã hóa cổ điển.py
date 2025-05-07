from datetime import datetime  # Nhập module datetime để lấy thời gian hiện tại

# Hàm caesar_encrypt thực hiện mã hóa Caesar Cipher với một phép dịch (shift) nhất định
def caesar_encrypt(text, shift):
    result = ""  # Khởi tạo biến để chứa kết quả mã hóa
    for ch in text:  # Duyệt qua từng ký tự trong văn bản đầu vào
        if ch.isalpha():  # Nếu ký tự là chữ cái (A-Z hoặc a-z)
            base = ord('A') if ch.isupper() else ord('a')  # Xác định cơ sở là 'A' hoặc 'a' tùy vào chữ hoa hay chữ thường
            # Thực hiện phép dịch Caesar với phép chia lấy dư để quay vòng qua bảng chữ cái
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:  # Nếu ký tự không phải chữ cái (ví dụ: số, dấu cách, ...)
            result += ch  # Thêm ký tự không thay đổi vào kết quả
    return result  # Trả về chuỗi đã mã hóa

plaintext = "HELLO MSSV 22H1120001"  # Văn bản đầu vào
shift = 3  # Số bước dịch, dịch 3 ký tự
cipher = caesar_encrypt(plaintext, shift)  # Mã hóa văn bản với phép dịch Caesar
# In kết quả mã hóa cùng với thời gian hiện tại
print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] Caesar Cipher: {cipher}")
