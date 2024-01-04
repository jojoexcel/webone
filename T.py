import os

os.system("cls")
y = int(input("請輸入2-10之間的數字： "))  # Convert input to an integer
x = list(range(1, y + 1))  # Generate a list of numbers from 1 to y
print(x[0:3])  # Print the first three elements of the list

for i in x:
    print(i)  # Print each element in the list


"""
sid = "9A435879"
sname = "Tom"
dage = 21
x = "20"
# print("學生資訊：\n學號：{}\n姓名：{}\n年齡：{}".format(sid, sname, dage))
# print("id: {:>10}\nnm: {:>10}\nyr: {:>10}".format(sid, sname, dage))
# 變數化
# print("學號:{:<{}}\n姓名:{:<{}}\n年齡:{:<{}}".format(sid, x, sname, x, dage, x)) #向左對齊 <
# print("學號:{:>{}}\n姓名:{:>{}}\n年齡:{:>{}}".format(sid, x, sname, x, dage, x)) #向右對齊 >
# print("學號:{:^{}}\n姓名:{:^{}}\n年齡:{:^{}}".format(sid, x, sname, x, dage, x)) #置中對齊 ^
# 空格差異
# print("學號: {:<{}}\n姓名: {:<{}}\n年齡: {:<{}}".format(sid, x, sname, x, dage, x))
# print("學號: {:>{}}\n姓名: {:>{}}\n年齡: {:>{}}".format(sid, x, sname, x, dage, x))
# print("學號: {:^{}}\n姓名: {:^{}}\n年齡: {:^{}}".format(sid, x, sname, x, dage, x))

# print(f"id: {sid}\nnm: {sname}\nyr: {dage}")
# print(f"id: {sid:>{x}}\nnm: {sname:>{x}}\nyr: {dage:>{x}}")
# print(f"id: {sid:<{x}}\nnm: {sname:<{x}}\nyr: {dage:<{x}}")
# print(f"id: {sid:^{x}}\nnm: {sname:^{x}}\nyr: {dage:^{x}}")
"""

"""
student = {}
students = {}
students['John'] = {}
students['John']['math'] = 89
students['John']['english'] = 78
students['John']['science'] = 92
students['Emily'] = {}
students['Emily']['math'] = 92
students['Emily']['english'] = 90
students['Emily']['science'] = 95
students['Tom'] = {}
students['Tom']['math'] = 80
students['Tom']['english'] = 85
students['Tom']['science'] = 88
students['Alice'] = {}
students['Alice']['math'] = 78
students['Alice']['english'] = 88
students['Alice']['science'] = 90

for name, scores in students.items():
    print(name, end=' ')
    for key, value in scores.items():
        print(key, value, end=' ')
    print()
"""
"""
import os.path

cur_path = os.path.dirname(__file__)
print(cur_path)
"""
