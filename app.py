import sqlite3
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
personnel_id = None

# 連接到 SQLite 資料庫
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# 創建人員表格（如果不存在）
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS personnel (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT,
        mobile TEXT
    )
'''
)
conn.commit()  # 執行SQL

# 關閉游標
cursor.close()


@app.route('/')
def index():
    # 顯示所有人員資料
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM personnel')
    personnel_list = cursor.fetchall()
    cursor.close()
    return render_template('index.html', personnel_list=personnel_list)


# Modify the route to handle deletion directly


@app.route('/', methods=['POST'])
def handle_actions():
    if request.form.get('action') == 'delete':
        # Delete personnel record
        personnel_id = request.form.get('personnel_id')
        if personnel_id:
            conn = sqlite3.connect('example.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM personnel WHERE id=?', (personnel_id,))
            conn.commit()
            cursor.close()
            return redirect(url_for('index'))
    # elif request.form.get('action') == 'edit':  # 修改這裡的條件
    #     # Handle 'edit' action
    #     personnel_id = request.form.get('personnel_id')
    #     # 其他處理 'edit' 操作的邏輯...
    #     cursor.execute('SELECT * FROM personnel WHERE id=?', (personnel_id,))
    #     personnel = cursor.fetchone()
    #     cursor.close()
    #     return render_template('edit_personnel.html', personnel=personnel)
    # Redirect back to the index page after handling the action


@app.route('/add_personnel', methods=['GET', 'POST'])
def add_personnel():
    if request.method == 'POST':
        # 新增人員資料
        name = request.form['name']
        phone = request.form['phone']
        mobile = request.form['mobile']

        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO personnel (name, phone, mobile) VALUES (?, ?, ?)',
            (name, phone, mobile),
        )
        conn.commit()
        cursor.close()

        return redirect(url_for('index'))

    return render_template('add_personnel.html')


@app.route('/edit_personnel/<int:personnel_id>', methods=['GET', 'POST'])
def edit_personnel(personnel_id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        # 修改人員資料
        name = request.form['name']
        phone = request.form['phone']
        mobile = request.form['mobile']

        cursor.execute(
            'UPDATE personnel SET name=?, phone=?, mobile=? WHERE id=?',
            (name, phone, mobile, personnel_id),
        )
        conn.commit()

        cursor.close()
        return redirect(url_for('index'))

    else:
        # 取得原始人員資料
        cursor.execute('SELECT * FROM personnel WHERE id=?', (personnel_id,))
        personnel = cursor.fetchone()
        cursor.close()

        return render_template('edit_personnel.html', personnel=personnel)


@app.route('/delete_personnel/<int:personnel_id>', methods=['GET', 'POST'])
def delete_personnel(personnel_id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    if request.method == 'POST':
        cursor.execute('DELETE FROM personnel WHERE id=?', (personnel_id,))
        conn.commit()
        cursor.close()
        return redirect(url_for('index'))
    else:
        # 取得原始人員資料
        cursor.execute('SELECT * FROM personnel WHERE id=?', (personnel_id,))
        personnel = cursor.fetchone()
        cursor.close()
        return render_template('delete_personnel.html', personnel=personnel)


if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)  # 本機測拭
    # app.run(host="0.0.0.0", debug=True)  #測拭（本機IP：5000）
    # app.run(host="0.0.0.0")  #正式


# bash --
# waitress-serve --host=0.0.0.0 --port=5000 app:app
