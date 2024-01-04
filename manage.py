import sqlite3
import tkinter as tk
from tkinter import messagebox

entry_name = None
entry_password = None


def create_table():
    conn = sqlite3.connect("Sqlite01.sqlite")
    cursor = conn.cursor()
    cursor.execute(
        '''CREATE TABLE IF NOT EXISTS password (
                        name TEXT PRIMARY KEY,
                        pass TEXT)'''
    )
    conn.commit()
    conn.close()


def read_data():
    conn = sqlite3.connect("Sqlite01.sqlite")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM password")
        data = {row[0]: row[1] for row in cursor.fetchall()}
        return data
    finally:
        conn.close()


def update_data(button_id):
    text_area.delete(1.0, tk.END)

    if button_id == 1:
        update_date_1()
    elif button_id == 2:
        update_date_2()
    elif button_id == 3:
        update_date_3()


def update_date_1():
    data = read_data()
    row = "帳號\t密碼\t修改\t刪除\n================\n"
    text_area.insert(tk.END, row)

    for key, value in data.items():
        row = f"{key}\t{value}\t"
        text_area.insert(tk.END, row)

        # 在文字後面插入按鈕
        button3 = tk.Button(
            text_area, text="修改", command=lambda k=f"{key}\t{value}\t": app_update(k)
        )
        button4 = tk.Button(text_area, text="刪除", command=lambda k=key: delete_entry(k))
        text_area.window_create(tk.END, window=button3)
        text_area.window_create(tk.END, window=button4)
        text_area.insert(tk.END, "\n")

    text_area.insert(tk.END, "\n")


def update_entry(key):
    text_area.insert(tk.END, f"按下了查詢按鈕，操作的是 {key}\n")


def delete_entry(key):
    conn = sqlite3.connect("Sqlite01.sqlite")
    cursor = conn.cursor()

    # 先檢查帳號是否存在
    cursor.execute("SELECT * FROM password WHERE name=?", (key,))
    existing_account = cursor.fetchone()

    if existing_account:
        # 帳號存在，執行刪除操作
        cursor.execute("DELETE FROM password WHERE name=?", (key,))
        conn.commit()
        messagebox.showinfo("刪除成功", f"已刪除帳號 {key}")
    else:
        # 帳號不存在，顯示錯誤訊息
        messagebox.showerror("錯誤", f"帳號 {key} 不存在")

    conn.close()
    update_data(1)


def app_update(key):
    new_window2 = tk.Toplevel(root)  # 創建 Toplevel 視窗
    new_window2.title("修改資料")

    # 計算新視窗的寬度和高度
    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()
    window_width = window_width // 10 * 2
    window_height = window_height // 10 * 2

    # 計算新視窗的 x 和 y 座標，使其置中
    x_coordinate = (root.winfo_screenwidth() - window_width) // 2
    y_coordinate = (root.winfo_screenheight() - window_height) // 2

    # 設定新視窗的大小和位置
    new_window2.geometry(
        "{0}x{1}+{2}+{3}".format(window_width, window_height, x_coordinate, y_coordinate)
    )

    # label_name = tk.Label(new_window2, text="帳號：")
    # label_name.pack(pady=4)

    label_name = tk.Label(new_window2, text="帳號：" + key.split('\t')[0])
    label_name.pack(pady=5)
    # entry_name = tk.Label(new_window2)  # 定義 entry_name
    # entry_name.insert(0, key.split('\t')[0])  # 設定 entry_name 的初始值
    # entry_name.pack(pady=5)

    label_password = tk.Label(new_window2, text="密碼：")
    label_password.pack(pady=5)

    entry_password = tk.Entry(new_window2)  # 定義 entry_password
    entry_password.insert(0, key.split('\t')[1])  # 設定 entry_password 的初始值
    entry_password.pack(pady=5)

    update_button = tk.Button(
        new_window2,
        text="更新",
        command=lambda: update_data(entry_name.get(), entry_password.get(), key, new_window2),
    )
    update_button.pack(pady=10)


def into_date():
    new_window = tk.Toplevel(root)  # 創建 Toplevel 視窗
    new_window.title("新增資料")

    # 計算新視窗的寬度和高度
    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()
    window_width = window_width // 10 * 2
    window_height = window_height // 10 * 2

    # 計算新視窗的 x 和 y 座標，使其置中
    x_coordinate = (root.winfo_screenwidth() - window_width) // 2
    y_coordinate = (root.winfo_screenheight() - window_height) // 2

    # 設定新視窗的大小和位置
    new_window.geometry(
        "{0}x{1}+{2}+{3}".format(window_width, window_height, x_coordinate, y_coordinate)
    )

    label_name = tk.Label(new_window, text="帳號：")
    label_name.pack(pady=4)

    entry_name = tk.Entry(new_window)  # 定義 entry_name
    entry_name.pack(pady=5)

    label_password = tk.Label(new_window, text="密碼：")
    label_password.pack(pady=4)

    entry_password = tk.Entry(new_window)  # 定義 entry_password
    entry_password.pack(pady=5)

    add_button = tk.Button(
        new_window,
        text="新增",
        command=lambda: add_data(entry_name.get(), entry_password.get(), new_window),
    )
    add_button.pack(pady=10)


# def update_data(k):
#     text_area.insert(tk.END, f"按下了查詢按鈕，操作的是 {k}\n")


def add_data(name, password, window):
    conn = sqlite3.connect("Sqlite01.sqlite")
    cursor = conn.cursor()

    try:
        # 檢查是否已存在相同帳號
        cursor.execute("SELECT * FROM password WHERE name=?", (name,))
        existing_account = cursor.fetchone()

        if existing_account:
            messagebox.showerror("錯誤", f"帳號 {name} 已存在")
        else:
            # 插入新資料
            cursor.execute("INSERT INTO password (name, pass) VALUES (?, ?)", (name, password))
            conn.commit()
            messagebox.showinfo("新增成功", f"已新增帳號 {name}")

            # 關閉新增視窗
            window.destroy()
            # 更新顯示資料
            update_data(1)
    finally:
        conn.close()


root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("左右分區示例")

frame_left = tk.Frame(root, width=0.4 * root.winfo_screenwidth(), bg="lightblue")
frame_left.pack(side="left", fill="y", ipadx=15)

frame_right = tk.Frame(root, width=0.85 * root.winfo_screenwidth())
frame_right.pack(side="right", fill="both")

button1 = tk.Button(frame_left, text="新增", command=into_date)
button1.pack(pady=10, ipadx=40, ipady=8)

button2 = tk.Button(frame_left, text="查詢", command=lambda: update_data(1))
button2.pack(pady=10, ipadx=40, ipady=8)

# button2 = tk.Button(frame_left, text="修改", command=lambda: update_data(2))
# button2.pack(pady=10, ipadx=40, ipady=8)

text_area = tk.Text(
    frame_right, width=int(0.85 * root.winfo_screenwidth()), font=("Arial", 14), wrap="word"
)
text_area.pack(expand=True, fill="both")

root.mainloop()
