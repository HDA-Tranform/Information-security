from Crypto.Cipher import AES               # Nhập lớp AES để thực hiện mã hóa AES
from Crypto.Random import get_random_bytes   # Nhập hàm tạo số ngẫu nhiên an toàn
from datetime import datetime                # Nhập module để lấy thời gian hiện tại

def aes_encrypt(plain):
    key = get_random_bytes(16)               # Tạo khóa ngẫu nhiên 16 byte (128-bit)
    cipher = AES.new(key, AES.MODE_EAX)      # Khởi tạo đối tượng AES ở chế độ EAX (hỗ trợ xác thực)
    ct, tag = cipher.encrypt_and_digest(plain.encode())
                                              # Mã hóa plain text (chuỗi) sau khi chuyển sang bytes,
                                              # đồng thời sinh thẻ xác thực tag
    return key, cipher.nonce, ct             # Trả về khóa, giá trị nonce và ciphertext

plain = "HELLO AES 128 BIT"                 # Văn bản đầu vào cần mã hóa
key, nonce, ct = aes_encrypt(plain)         # Gọi hàm mã hóa, nhận về key, nonce, ciphertext
print(
    f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] "
    f"AES128 Key={key.hex()} Nonce={nonce.hex()} CT={ct.hex()}"
)                                            # In ra thời gian hiện tại, khóa, nonce và ciphertext dưới dạng hex
