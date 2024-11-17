import tkinter as tk
from tkinter import ttk
import pyperclip  # Thư viện hỗ trợ sao chép vào clipboard

# Bảng ký tự lật ngược
reverse_char_map = {
    'a': 'ɒ', 'b': 'b', 'c': 'ɔ', 'p': 'd', 'e': 'ǝ', 'f': 'ɟ', 'g': 'ƃ',
    'h': 'ɥ', 'i': 'ı', 'j': 'ɾ', 'k': 'ʞ', 'l': 'l', 'm': 'ɯ', 'u': 'u',
    'o': 'o', 'p': 'd', 'q': 'q', 'r': 'ɹ', 's': 's', 't': 'ʇ', 'n': 'u',
    'v': 'ʌ', 'w': 'ʍ', 'x': 'x', 'y': 'ʎ', 'z': 'z',
    'A': 'ɐ', 'B': 'q', 'C': 'Ɔ', 'D': 'ᗡ', 'E': 'Ǝ', 'F': 'ꟻ', 'G': 'ƃ',
    'H': 'H', 'I': 'I', 'J': 'ſ', 'K': 'ꓘ', 'L': '⅃', 'M': 'W', 'N': 'N',
    'O': 'O', 'P': 'Ԁ', 'Q': 'Ό', 'R': 'ɹ', 'S': 'S', 'T': '⊥', 'U': '∩',
    'V': 'Λ', 'W': 'M', 'X': 'X', 'Y': '⅄', 'Z': 'Z'
}

# Hàm để lật ngược từng ký tự trong chuỗi
def reverse_characters(s):
    return ''.join(reverse_char_map.get(c, c) for c in s)

# Hàm cập nhật kết quả khi nội dung của ô nhập liệu thay đổi
def on_entry_change(*args):
    global update_flag
    if not update_flag:
        return
    input_text = entry_var.get()  # Lấy chuỗi từ ô nhập liệu
    reversed_text = reverse_characters(input_text)  # Lật ngược ký tự

    # Tạm thời tắt cờ cập nhật
    update_flag = False

    # Cập nhật lại nội dung ô nhập liệu
    entry_var.set(reversed_text)

    # Bật lại cờ cập nhật
    update_flag = True

# Hàm sao chép văn bản vào clipboard
def copy_to_clipboard():
    text = entry_var.get()  # Lấy văn bản từ ô nhập liệu
    pyperclip.copy(text)  # Sao chép văn bản vào clipboard

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng dụng Độc lạ Ký tự")

# Tạo các widget
entry_var = tk.StringVar()
entry = ttk.Entry(root, textvariable=entry_var, width=40)
copy_button = ttk.Button(root, text="Sao chép", command=copy_to_clipboard)

# Khởi tạo cờ cập nhật
update_flag = True

# Gán hàm on_entry_change cho sự kiện thay đổi nội dung của ô nhập liệu
entry_var.trace_add("write", on_entry_change)

# Sắp xếp các widget trong cửa sổ
entry.pack(pady=10)
copy_button.pack(pady=10)

# Chạy ứng dụng
root.mainloop()
