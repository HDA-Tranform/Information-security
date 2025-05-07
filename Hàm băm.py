import hashlib                          # Nhập thư viện hashlib để sử dụng các thuật toán băm (hashing) như SHA256
from datetime import datetime           # Nhập module datetime để lấy thời gian hiện tại

def sha256_hash(txt):                   # Định nghĩa hàm sha256_hash nhận đầu vào là chuỗi txt
    return hashlib.sha256(txt.encode()).hexdigest()  # Băm chuỗi txt sau khi chuyển thành bytes và trả về giá trị băm (hex)

txt = "Hash me with SHA256!"            # Đặt giá trị chuỗi cần băm vào biến txt
h = sha256_hash(txt)                    # Gọi hàm sha256_hash để băm chuỗi và lưu kết quả vào biến h
# In ra thời gian hiện tại cùng với kết quả SHA256 của chuỗi txt dưới dạng hexdigest (chuỗi hex)
print(f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] SHA256={h}")

