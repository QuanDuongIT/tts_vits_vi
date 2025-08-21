from piper_phonemize import  *

# Thay thế các ký hiệu đặc biệt thành từ tương ứng
def symbols_to_vietnamese(text):
    return text.replace('%', 'phần trăm')

def get_real_sokuon(text):
    # Không áp dụng với tiếng Việt, placeholder để mở rộng
    return text

def get_real_hatsuon(text):
    # Không áp dụng với tiếng Việt, placeholder để mở rộng
    return text

# Thay thế các ký hiệu đặc biệt thành từ tương ứng
def symbols_to_vietnamese(text):
    return text.replace('%', 'phần trăm')

# Hàm chuyển văn bản sang IPA dùng viphoneme
def vietnamese_to_ipa_version4(text):
    text=symbols_to_vietnamese(text)
    return ''.join(p for word in phonemize_espeak(text, "vi") for p in word)



