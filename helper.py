from person import Lecturer, Student
import json
import csv
def get_lecturer_info():
    lecturer = Lecturer()
    code = input("Enter your code please: ")
    if code != "":
        lecturer.code = code
    name = input("Enter your name please: ")
    if name != "":
        lecturer.name = name
    family = input("Enter your family please: ")
    if family != "":
        lecturer.family = family
        
    lecturer.show_info()
    lecturer.greet()
    return lecturer

def get_student_info():
    std = Student()
    code = input("Enter your code please: ")
    if code != "":
        std.code = code
        name = input("Enter your name please: ")
    if name != "":
        std.name = name
    family = input("Enter your family please: ")
    if family != "":
        std.family = family
        
    std.show_info()
    return std


def create_json(lst):
    string = []
    for item in lst:
        obj = {}
        obj["code"] = item.code
        obj["name"] = item.name
        obj["family"] = item.family
        string.append(obj)
    data = json.dumps(string)
    print(data)
    Path("participants.json").write_text(data, encoding="utf-8")


def create_csv(lst):
    with open("participants.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Code", "Name", "Family"])
        for item in lst:
            writer.writerow([item.code, item.name, item.family])
