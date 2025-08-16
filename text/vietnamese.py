import re
from viphoneme import vi2IPA
from piper_phonemize import  *

# Regex để tách ký tự không thuộc bảng chữ cái tiếng Việt
_vietnamese_marks = re.compile(
    r'[^a-zA-Z0-9ăâđêôơưáàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệóòỏõọốồổỗộớờởỡợúùủũụứừửữựíìỉĩịýỳỷỹỵăâđêôơư ]'
)

# Thay thế các ký hiệu đặc biệt thành từ tương ứng
def symbols_to_vietnamese(text):
    return text.replace('%', 'phần trăm')

# Hàm chuyển văn bản sang IPA dùng viphoneme
def vietnamese_to_ipa(text):
    text = symbols_to_vietnamese(text)
    text = re.sub(_vietnamese_marks, '', text)  # loại bỏ ký tự không cần thiết
    ipa = vi2IPA(text)
    return ipa.strip()


def get_real_sokuon(text):
    # Không áp dụng với tiếng Việt, placeholder để mở rộng
    return text

def get_real_hatsuon(text):
    # Không áp dụng với tiếng Việt, placeholder để mở rộng
    return text


def vietnamese_to_ipa_version1(text):
    """Phiên bản IPA 1 (cơ bản)"""
    ipa = vietnamese_to_ipa(text)
    ipa = get_real_sokuon(ipa)
    ipa = get_real_hatsuon(ipa)
    return ipa


def vietnamese_to_ipa_version2(text):
    """Phiên bản IPA 2 (có thể thêm quy tắc chỉnh sửa ở đây)"""
    ipa = vietnamese_to_ipa(text)
    # Thêm xử lý nâng cao nếu cần
    return ipa


def vietnamese_to_ipa_version3(text):
    """Phiên bản IPA 3 (ví dụ: chuyển đổi âm vị cụ thể)"""
    ipa = vietnamese_to_ipa_version2(text)
    ipa = ipa.replace('ɗ', 'ɖ')  # Thay thế phụ âm nếu muốn
    return ipa


# Thay thế các ký hiệu đặc biệt thành từ tương ứng
def symbols_to_vietnamese(text):
    return text.replace('%', 'phần trăm')

# Hàm chuyển văn bản sang IPA dùng viphoneme
def vietnamese_to_ipa_version4(text):
    text=symbols_to_vietnamese(text)
    return ''.join(p for word in phonemize_espeak(text, "vi") for p in word)



