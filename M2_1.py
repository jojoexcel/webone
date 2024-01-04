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
    result = "帳號\t密碼\n================\n"
    for key, value in data.items():
        result += f"{key}\t{value}\n"
    text_area.insert(tk.END, result)


def update_date_2():
    text_area.insert(tk.END, "更新資料: 按下了按鈕 2\n")


def update_date_3():
    text_area.insert(tk.END, "更新資料: 按下了按鈕 3\n")


root = tk.Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("左右分區示例")

frame_left = tk.Frame(root, width=0.4 * root.winfo_screenwidth(), bg="lightblue")
frame_left.pack(side="left", fill="y", ipadx=15)

frame_right = tk.Frame(root, width=0.85 * root.winfo_screenwidth())
frame_right.pack(side="right", fill="both")

button1 = tk.Button(frame_left, text="查詢", command=lambda: update_data(1))
button1.pack(pady=10, ipadx=40, ipady=8)

button2 = tk.Button(frame_left, text="修改", command=lambda: update_data(2))
button2.pack(pady=10, ipadx=40, ipady=8)
text_area = tk.Text(
    frame_right, width=int(0.85 * root.winfo_screenwidth()), font=("Arial", 14), wrap="word"
)


text_area.pack(expand=True, fill="both")

root.mainloop()
