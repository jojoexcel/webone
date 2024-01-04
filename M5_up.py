import sqlite3
import tkinter as tk
from tkinter import messagebox


class PasswordManager: #預載入的模組
    def __init__(self, root):
        self.root = root
        self.setup_ui()
        self.create_table()
        # self.update_data_1()

    def setup_ui(self):
        self.frame_left = tk.Frame(
            self.root, width=0.4 * self.root.winfo_screenwidth(), bg="lightblue"
        )
        self.frame_left.pack(side="left", fill="y", ipadx=15)

        self.frame_right = tk.Frame(self.root, width=0.85 * self.root.winfo_screenwidth())
        self.frame_right.pack(side="right", fill="both")

        self.button1 = tk.Button(self.frame_left, text="新增", command=self.into_date)
        self.button1.pack(pady=10, ipadx=40, ipady=8)

        self.button2 = tk.Button(self.frame_left, text="查詢", command=lambda: self.update_data_1())
        self.button2.pack(pady=10, ipadx=40, ipady=8)

        self.text_area = tk.Text(
            self.frame_right,
            width=int(0.85 * self.root.winfo_screenwidth()),
            font=("Arial", 14),
            wrap="word",
        )
        self.text_area.pack(expand=True, fill="both")

    def create_table(self):
        conn = sqlite3.connect("Sqlite01.sqlite")
        cursor = conn.cursor()
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS password (
                        name TEXT PRIMARY KEY,
                        pass TEXT)'''
        )
        conn.commit()
        conn.close()

    def read_data(self):
        conn = sqlite3.connect("Sqlite01.sqlite")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM password")
            data = {row[0]: row[1] for row in cursor.fetchall()}
            return data
        finally:
            conn.close()

    def update_data_1(self):
        self.text_area.delete(1.0, tk.END)

        data = self.read_data()
        row = "帳號\t密碼\t修改\t刪除\n================\n"
        self.text_area.insert(tk.END, row)

        for key, value in data.items():
            row = f"{key}\t{value}\t"
            self.text_area.insert(tk.END, row)

            button3 = tk.Button(
                self.text_area, text="修改", command=lambda k=f"{key}\t{value}\t": self.appUpdate(k)
            )
            button4 = tk.Button(
                self.text_area, text="刪除", command=lambda k=key: self.delete_entry(k)
            )

            self.text_area.window_create(tk.END, window=button3)
            self.text_area.window_create(tk.END, window=button4)
            self.text_area.insert(tk.END, "\n")

        self.text_area.insert(tk.END, "\n")

    def delete_entry(self, key):
        conn = sqlite3.connect("Sqlite01.sqlite")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM password WHERE name=?", (key,))
        existing_account = cursor.fetchone()

        if existing_account:
            cursor.execute("DELETE FROM password WHERE name=?", (key,))
            conn.commit()
            messagebox.showinfo("刪除成功", f"已刪除帳號 {key}")
        else:
            messagebox.showerror("錯誤", f"帳號 {key} 不存在")

        conn.close()
        self.update_data_1()

    def appUpdate(self, key):
        newWindow2 = tk.Toplevel(self.root)
        newWindow2.title("修改資料")

        windowWidth = self.root.winfo_screenwidth() // 10 * 2
        windowHeight = self.root.winfo_screenheight() // 10 * 2
        xCoordinate = (self.root.winfo_screenwidth() - windowWidth) // 2
        yCoordinate = (self.root.winfo_screenheight() - windowHeight) // 2

        newWindow2.geometry(
            "{0}x{1}+{2}+{3}".format(windowWidth, windowHeight, xCoordinate, yCoordinate)
        )

        labelName = tk.Label(newWindow2, text="帳號：" + key.split('\t')[0])
        labelName.pack(pady=5)

        labelPassword = tk.Label(newWindow2, text="密碼：")
        labelPassword.pack(pady=5)

        entryPassword = tk.Entry(newWindow2)
        entryPassword.insert(0, key.split('\t')[1])
        entryPassword.pack(pady=5)

        updateButton = tk.Button(
            newWindow2,
            text="更新",
            command=lambda: self.update_data(key.split('\t')[0], entryPassword.get(), newWindow2),
        )
        updateButton.pack(pady=10)

    def update_data(self, name, password, window):
        conn = sqlite3.connect("Sqlite01.sqlite")
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM password WHERE name=?", (name,))
            existing_account = cursor.fetchone()

            if existing_account:
                cursor.execute("UPDATE password SET pass=? WHERE name=?", (password, name))
                conn.commit()
                messagebox.showinfo("更新成功", f"已更新帳號 {name}")
            else:
                messagebox.showerror("錯誤", f"帳號 {name} 不存在")

            window.destroy()
            self.update_data_1()
        finally:
            conn.close()

    def into_date(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("新增資料")

        window_width = self.root.winfo_screenwidth() // 10 * 2
        window_height = self.root.winfo_screenheight() // 10 * 2
        x_coordinate = (self.root.winfo_screenwidth() - window_width) // 2
        y_coordinate = (self.root.winfo_screenheight() - window_height) // 2

        new_window.geometry(
            "{0}x{1}+{2}+{3}".format(window_width, window_height, x_coordinate, y_coordinate)
        )

        label_name = tk.Label(new_window, text="帳號：")
        label_name.pack(pady=4)

        entry_name = tk.Entry(new_window)
        entry_name.pack(pady=5)

        label_password = tk.Label(new_window, text="密碼：")
        label_password.pack(pady=4)

        entry_password = tk.Entry(new_window)
        entry_password.pack(pady=5)

        add_button = tk.Button(
            new_window,
            text="新增",
            command=lambda: self.add_data(entry_name.get(), entry_password.get(), new_window),
        )
        add_button.pack(pady=10)

    def add_data(self, name, password, window):
        conn = sqlite3.connect("Sqlite01.sqlite")
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM password WHERE name=?", (name,))
            existing_account = cursor.fetchone()

            if existing_account:
                messagebox.showerror("錯誤", f"帳號 {name} 已存在")
            else:
                cursor.execute("INSERT INTO password (name, pass) VALUES (?, ?)", (name, password))
                conn.commit()
                messagebox.showinfo("新增成功", f"已新增帳號 {name}")

                window.destroy()
                self.update_data_1()
        finally:
            conn.close()


if __name__ == "__main__":
    root = tk.Tk()
    # root.attributes("-fullscreen", True)  # Set the window to fullscreen  #非視窗
    root.title("左右分區示例")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))  # 視窗
    app = PasswordManager(root)
    root.mainloop()
