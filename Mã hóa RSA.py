from Crypto.PublicKey import RSA           # Nhập lớp RSA để sinh và quản lý khóa RSA
from Crypto.Cipher import PKCS1_OAEP        # Nhập lớp PKCS1_OAEP để thực hiện mã hóa RSA an toàn
from datetime import datetime               # Nhập module để lấy thời gian hiện tại

def rsa_encrypt(msg):
    key = RSA.generate(2048)               # Sinh cặp khóa RSA 2048 bit (key.n, key.e công khai; key.d riêng tư)
    pub = key.publickey()                  # Trích xuất khóa công khai từ cặp khóa vừa sinh
    cipher = PKCS1_OAEP.new(pub)           # Tạo đối tượng mã hóa RSA theo chuẩn OAEP với khóa công khai
    c = cipher.encrypt(msg.encode())       # Mã hóa chuỗi msg (chuyển sang bytes) và trả về ciphertext
    return key, c                          # Trả về cặp khóa đầy đủ và ciphertext

# Gọi hàm mã hóa với thông điệp "HELLO RSA"
key, ciphered = rsa_encrypt("HELLO RSA")
# In ra thời gian hiện tại cùng 64 ký tự đầu tiên của ciphertext ở dạng hex
print(
    f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] "
    f"RSA CT={ciphered.hex()[:64]}..."
)
