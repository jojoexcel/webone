import sqlite3
import tkinter as tk
from tkinter import messagebox

entry_name = None  # 將 entry_name 宣告為全域變數
entry_password = None  # 將 entry_password 宣告為全域變數


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
    cursor.execute("SELECT * FROM password")
    data = {row[0]: row[1] for row in cursor.fetchall()}
    conn.close()
    return data


def disp_data():
    data = read_data()
    result = "帳號\t密碼\n================\n"
    for key, value in data.items():
        result += f"{key}\t{value}\n"
    messagebox.showinfo("顯示帳號、密碼", result)


def update_data(button_id):
    # 在這裡根據按下的按鈕 ID 更新右側資料
    # 這裡只是一個示例，你需要根據實際需求編寫更新邏輯
    if button_id == 1:
        update_date_1()
        return
    elif button_id == 2:
        update_date_2()
        return
    elif button_id == 3:
        update_date_3()
        return
    else:
        return "無效的選擇"


def update_date_1():
    data = read_data()
    result = "帳號\t密碼\n================\n"
    for key, value in data.items():
        result += f"{key}\t{value}\n"
    label_right.config(text=f"{result}")


def update_date_2():
    label_right.config(text=f"更新資料: 按下了按鈕 2")


def update_date_3():
    label_right.config(text=f"更新資料: 按下了按鈕 3")


# global entry_name, entry_password  # 加上這行宣告，以使用全域變數
root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

root.title("左右分區示例")
# 第一層左右
# 左側 Frame，佔整個視窗的 15%
# frame_left = tk.Frame(root, width=0.25 * root.winfo_screenwidth(), bg="lightblue")
frame_left = tk.Frame(root, width=0.4 * root.winfo_screenwidth(), bg="lightblue")
frame_left.pack(
    side="left",
    fill="y",
    ipadx=15,  # 設定內距
)
# 右側 Frame，佔整個視窗的 85%
frame_right = tk.Frame(root, width=0.85 * root.winfo_screenwidth())
frame_right.pack(side="right", fill="both")


# 在左側 Frame 中放置兩個功能鍵
button1 = tk.Button(frame_left, text="查詢", command=lambda: update_data(1))
button1.pack(
    pady=10,
    ipadx=40,
    ipady=8,
)

button2 = tk.Button(frame_left, text="修改", command=lambda: update_data(2))
button2.pack(
    pady=10,
    ipadx=40,
    ipady=8,
)


# 在右側 Frame 中放置一個 Label，用於顯示更新後的資料
label_right = tk.Label(frame_right, text="右側資料區", font=("Arial", 16), padx=20, pady=20)
label_right.pack(expand=True, fill="both")

root.mainloop()
