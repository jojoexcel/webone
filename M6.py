import sqlite3
import tkinter as tk
from tkinter import messagebox
import subprocess


class LoginWindow:
    def __init__(self, root, on_login_success):
        self.root = root
        self.on_login_success = on_login_success
        self.setup_ui()

    def setup_ui(self):
        self.label_username = tk.Label(self.root, text="帳號：")
        self.label_username.pack(pady=10)

        self.entry_username = tk.Entry(self.root)
        self.entry_username.pack(pady=5)

        self.label_password = tk.Label(self.root, text="密碼：")
        self.label_password.pack(pady=10)

        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack(pady=5)

        self.button_login = tk.Button(self.root, text="登入", command=self.login)
        self.button_login.pack(pady=10)

    def login(self):
        # Connect to the SQLite database
        conn = sqlite3.connect("Sqlite01.sqlite")
        cursor = conn.cursor()

        try:
            # Execute a SELECT query to check username and password   RTRIM(
            cursor.execute(
                "SELECT * FROM password WHERE name=? AND pass=?",
                (self.entry_username.get(), self.entry_password.get()),
            )
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("登入成功", "登入成功！")
                self.on_login_success()
            else:
                messagebox.showerror("登入失敗", "帳號或密碼錯誤。請重新輸入。")
        finally:
            # Close the database connection
            conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("登入")
    root.geometry("300x200")

    def on_login_success():
        root.destroy()  # 關閉登入視窗
        subprocess.run(["python", "M5_up.py"])  # 呼叫 M5_up.py

    login_window = LoginWindow(root, on_login_success)

    root.mainloop()
