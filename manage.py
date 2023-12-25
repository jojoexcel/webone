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


def input_data():
    name = entry_name.get()
    password = entry_password.get()

    if name == "" or password == "":
        messagebox.showwarning("輸入錯誤", "帳號和密碼不能為空")
        return

    data = read_data()

    conn = sqlite3.connect("Sqlite01.sqlite")
    cursor = conn.cursor()

    if name in data:
        # 帳號已存在，更新密碼
        cursor.execute("UPDATE password SET pass = ? WHERE name = ?", (password, name))
        conn.commit()
        conn.close()
        messagebox.showinfo("更新完畢", f"{name} 的密碼已更新")
    else:
        # 帳號不存在，新增資料
        cursor.execute("INSERT INTO password VALUES (?, ?)", (name, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("儲存完畢", f"{name} 已儲存完畢")


def del_date():
    name = entry_name.get()
    if name == "":
        messagebox.showwarning("輸入錯誤", "帳號不能為空")
        return
    data = read_data()
    conn = sqlite3.connect("Sqlite01.sqlite")
    cursor = conn.cursor()

    if name in data:
        # 帳號已存在，更新密碼
        cursor.execute("DELETE FROM password WHERE name = ?", (name,))
        conn.commit()
        conn.close()
        messagebox.showinfo("更新完畢", f"{name} 帳號已刪除")
    else:
        # 帳號不存在
        messagebox.showinfo("錯誤", f"{name} 帳號不存在")


def main_menu():
    global entry_name, entry_password  # 加上這行宣告，以使用全域變數
    window = tk.Tk()
    window.title("帳號、密碼管理系統")

    label_name = tk.Label(window, text="帳號：")
    label_name.grid(row=0, column=0, padx=10, pady=5)

    entry_name = tk.Entry(window)  # 定義 entry_name
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    label_password = tk.Label(window, text="密碼：")
    label_password.grid(row=1, column=0, padx=10, pady=5)

    entry_password = tk.Entry(window, show="*")  # 定義 entry_password
    entry_password.grid(row=1, column=1, padx=10, pady=5)

    button_input = tk.Button(window, text="新增修改帳號、密碼", command=input_data, width=20)
    button_input.grid(row=2, column=0, columnspan=2, pady=10)

    button_display = tk.Button(window, text="顯示帳號、密碼", command=disp_data, width=20)
    button_display.grid(row=3, column=0, columnspan=2, pady=10)

    button_display = tk.Button(window, text="帳號刪除", command=del_date, width=20)
    button_display.grid(row=4, column=0, columnspan=2, pady=10)

    button_exit = tk.Button(window, text="結束程式", command=window.destroy, width=20)
    button_exit.grid(row=5, column=0, columnspan=2, pady=10)

    window.mainloop()


if __name__ == "__main__":
    create_table()
    main_menu()
