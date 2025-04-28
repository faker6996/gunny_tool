import tkinter as tk
from tkinter import messagebox

# Dữ liệu JSON
data = {
  "20_degree": [
    { "distance": 1, "force": 10 },
    { "distance": 2, "force": 19 },
    { "distance": 3, "force": 25 },
    { "distance": 4, "force": 36 },
    { "distance": 5, "force": 44 },
    { "distance": 6, "force": 47 },
    { "distance": 7, "force": 48 },
    { "distance": 8, "force": 51 },
    { "distance": 9, "force": 54 },
    { "distance": 10, "force": 57 },
    { "distance": 11, "force": 58 },
    { "distance": 12, "force": 60 },
    { "distance": 13, "force": 63 },
    { "distance": 14, "force": 65 },
    { "distance": 15, "force": 68 },
    { "distance": 16, "force": 70 },
    { "distance": 17, "force": 73 },
    { "distance": 18, "force": 75 },
    { "distance": 19, "force": 78 },
    { "distance": 20, "force": 80 }
  ],
  "65_degree": [
    { "distance": 1, "force": 13 },
    { "distance": 2, "force": 20 },
    { "distance": 3, "force": 26 },
    { "distance": 4, "force": 31 },
    { "distance": 5, "force": 37 },
    { "distance": 6, "force": 41 },
    { "distance": 7, "force": 45 },
    { "distance": 8, "force": 49 },
    { "distance": 9, "force": 52 },
    { "distance": 10, "force": 55 },
    { "distance": 11, "force": 58 },
    { "distance": 12, "force": 61 },
    { "distance": 13, "force": 64 },
    { "distance": 14, "force": 67 },
    { "distance": 15, "force": 70 },
    { "distance": 16, "force": 73 },
    { "distance": 17, "force": 76 },
    { "distance": 18, "force": 79 },
    { "distance": 19, "force": 82 },
    { "distance": 20, "force": 85 }
  ],
  "30_degree": [
    { "distance": 1, "force": 14 },
    { "distance": 2, "force": 20 },
    { "distance": 3, "force": 24 },
    { "distance": 4, "force": 28 },
    { "distance": 5, "force": 32 },
    { "distance": 6, "force": 35 },
    { "distance": 7, "force": 38 },
    { "distance": 8, "force": 41 },
    { "distance": 9, "force": 44 },
    { "distance": 10, "force": 47 },
    { "distance": 11, "force": 50 },
    { "distance": 12, "force": 52 },
    { "distance": 13, "force": 55 },
    { "distance": 14, "force": 57 },
    { "distance": 15, "force": 60 },
    { "distance": 16, "force": 62 },
    { "distance": 17, "force": 65 },
    { "distance": 18, "force": 67 },
    { "distance": 19, "force": 69 },
    { "distance": 20, "force": 72 }
  ],
  "50_degree": [
    { "distance": 1, "force": 14 },
    { "distance": 2, "force": 20 },
    { "distance": 3, "force": 24 },
    { "distance": 4, "force": 28 },
    { "distance": 5, "force": 32 },
    { "distance": 6, "force": 35 },
    { "distance": 7, "force": 38 },
    { "distance": 8, "force": 41 },
    { "distance": 9, "force": 44 },
    { "distance": 10, "force": 47 },
    { "distance": 11, "force": 50 },
    { "distance": 12, "force": 53 },
    { "distance": 13, "force": 55 },
    { "distance": 14, "force": 58 },
    { "distance": 15, "force": 60 },
    { "distance": 16, "force": 63 },
    { "distance": 17, "force": 65 },
    { "distance": 18, "force": 68 },
    { "distance": 19, "force": 70 },
    { "distance": 20, "force": 72 }
  ]

}

# Hàm xử lý logic
def calculate_output(event=None):  # Thêm `event` để hỗ trợ xử lý phím Enter
    try:
        input1 = int(entry1.get())
        input2 = float(entry2.get())
        
        if input1 < 1 or input1 > 20 or input2 < 0 or input2 >= 10:
            raise ValueError("Đầu vào không hợp lệ!")
        
        result_text = ""
        
        for angle, values in data.items():
            original_angle = int(angle.split("_")[0])  # Lấy góc từ key JSON
            force = next((item["force"] for item in values if item["distance"] == input1), None)
            
            if force is not None:
                output1 = original_angle - (input2 * 10 // 5)
                output2 = force - (input2 * 10 % 5)
                result_text += f"{angle}: Góc = {output1:.1f}, Lực = {output2:.1f}\n"
        
        output_label.config(text=result_text)
    except ValueError as e:
        messagebox.showerror("Lỗi", str(e))


def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    output_label.config(text="")



# Tạo giao diện
root = tk.Tk()
root.title("Ứng dụng Tìm Góc và Lực")
root.geometry("400x400")  # Thay đổi kích thước cửa sổ (500x400 là ví dụ)


# Nhập liệu
tk.Label(root, text="Nhập Cự Ly (Input1):",font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Nhập Tham Số (Input2):",font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Nút tính toán
tk.Button(root, text="Tính Toán", command=calculate_output,font=("Arial", 14)).grid(row=2, column=0, columnspan=2, pady=10)

# Nút xóa
tk.Button(root, text="Xóa", command=clear_fields,font=("Arial", 14)).grid(row=2, column=1, padx=5, pady=10)


# Hiển thị kết quả
output_label = tk.Label(root, text="", justify="left", wraplength=400,font=("Arial", 14))
output_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Liên kết phím Enter với hàm tính toán
root.bind('<Return>', calculate_output)

#root.iconbitmap('./gunny_a.ico')  # Đặt biểu tượng cho cửa sổ app
root.mainloop()
