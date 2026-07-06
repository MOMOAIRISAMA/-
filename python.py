import json
import os

# 存储学生数据的文件
DATA_FILE = "student_data.json"
student_list = []

# 初始化：读取本地文件数据
def load_data():
    global student_list
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            student_list = json.load(f)
    else:
        student_list = []

# 保存数据到本地文件
def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(student_list, f, ensure_ascii=False, indent=2)

# 1. 添加学生信息
def add_student():
    print("===== 添加学生信息 =====")
    sid = input("请输入学号：")
    # 判断学号是否重复
    for s in student_list:
        if s["sid"] == sid:
            print("该学号已存在，无法重复添加！")
            return
    name = input("请输入姓名：")
    age = input("请输入年龄：")
    try:
        score = float(input("请输入成绩："))
    except ValueError:
        print("成绩输入格式错误，添加失败！")
        return
    new_stu = {
        "sid": sid,
        "name": name,
        "age": age,
        "score": score
    }
    student_list.append(new_stu)
    save_data()
    print("✅ 学生信息添加成功！")

# 2. 查询单个学生（按学号）
def search_student():
    print("===== 查询学生信息 =====")
    sid = input("输入要查询的学号：")
    for stu in student_list:
        if stu["sid"] == sid:
            print(f"\n学号：{stu['sid']}")
            print(f"姓名：{stu['name']}")
            print(f"年龄：{stu['age']}")
            print(f"成绩：{stu['score']}")
            return
    print("❌ 未查询到该学号学生")

# 3. 修改学生信息
def modify_student():
    print("===== 修改学生信息 =====")
    sid = input("输入待修改学号：")
    for stu in student_list:
        if stu["sid"] == sid:
            print("请输入新信息（直接回车则保留原内容）")
            new_name = input(f"新姓名[{stu['name']}]：") or stu['name']
            new_age = input(f"新年龄[{stu['age']}]：") or stu['age']
            score_input = input(f"新成绩[{stu['score']}]：")
            if score_input:
                try:
                    new_score = float(score_input)
                except:
                    print("成绩格式错误，本次成绩不修改")
                    new_score = stu['score']
            else:
                new_score = stu['score']

            stu['name'] = new_name
            stu['age'] = new_age
            stu['score'] = new_score
            save_data()
            print("✅ 修改完成！")
            return
    print("❌ 未找到该学生")

# 4. 删除学生
def delete_student():
    print("===== 删除学生信息 =====")
    sid = input("输入要删除的学号：")
    for i, stu in enumerate(student_list):
        if stu["sid"] == sid:
            del student_list[i]
            save_data()
            print("✅ 删除成功")
            return
    print("❌ 学号不存在")

# 5. 展示全部学生
def show_all():
    print("\n======== 全部学生信息 ========")
    if not student_list:
        print("暂无学生数据")
        return
    print(f"{'学号':<10}{'姓名':<8}{'年龄':<6}{'成绩':<6}")
    print("-"*35)
    for stu in student_list:
        print(f"{stu['sid']:<10}{stu['name']:<8}{stu['age']:<6}{stu['score']:<6}")

# 6. 成绩排序（降序）
def sort_by_score():
    global student_list
    if not student_list:
        print("无数据可排序")
        return
    # 按成绩从高到低排序
    student_list.sort(key=lambda x: x["score"], reverse=True)
    save_data()
    print("已按成绩降序排列！")
    show_all()

# 7. 成绩统计：平均分、最高分、最低分
def statistics():
    if not student_list:
        print("暂无学生数据，无法统计")
        return
    scores = [s['score'] for s in student_list]
    avg = sum(scores) / len(scores)
    max_s = max(scores)
    min_s = min(scores)
    print("\n===== 成绩统计信息 =====")
    print(f"学生总数：{len(student_list)}")
    print(f"平均分：{avg:.2f}")
    print(f"最高分：{max_s}")
    print(f"最低分：{min_s}")

# 系统菜单
def menu():
    load_data()  # 程序启动先加载历史数据
    while True:
        print("\n======== 学生信息管理系统 ========")
        print("1. 添加学生信息")
        print("2. 根据学号查询学生")
        print("3. 修改学生信息")
        print("4. 删除学生信息")
        print("5. 显示全部学生")
        print("6. 按成绩降序排序")
        print("7. 成绩数据统计")
        print("0. 退出系统")
        choice = input("\n请输入功能序号：")
        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            modify_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            show_all()
        elif choice == "6":
            sort_by_score()
        elif choice == "7":
            statistics()
        elif choice == "0":
            save_data()
            print("数据已保存，系统退出！")
            break
        else:
            print("输入错误，请选择0-7之间数字！")

if __name__ == "__main__":
    menu()