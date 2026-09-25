"""
Practical work 1: Student mark management
------------------------------------------
Cau truc du lieu:
    students: list cac dict  {"id":..., "name":..., "dob":...}
    courses : list cac dict  {"id":..., "name":...}
    marks   : dict, key la tuple (student_id, course_id), value la diem (float)
"""


# ---------- INPUT FUNCTIONS ----------

def input_num_students():
    n = int(input("Nhap so luong sinh vien: "))
    return n


def input_student_info():
    print("--- Nhap thong tin sinh vien ---")
    sid = input("  ID: ")
    name = input("  Ten: ")
    dob = input("  Ngay sinh (dd/mm/yyyy): ")
    return {"id": sid, "name": name, "dob": dob}


def input_num_courses():
    m = int(input("Nhap so luong mon hoc: "))
    return m


def input_course_info():
    print("--- Nhap thong tin mon hoc ---")
    cid = input("  ID mon: ")
    cname = input("  Ten mon: ")
    return {"id": cid, "name": cname}


def input_marks_for_course(students, courses, marks):
    """Chon 1 mon hoc, nhap diem cho tung sinh vien trong mon do."""
    if not courses:
        print("Chua co mon hoc nao.")
        return

    list_courses(courses)
    course_id = input("Chon ID mon hoc de nhap diem: ")

    # kiem tra mon hoc co ton tai khong
    found = any(c["id"] == course_id for c in courses)
    if not found:
        print("Khong tim thay mon hoc voi ID nay.")
        return

    for sv in students:
        while True:
            try:
                diem = float(input(f"  Diem cua {sv['name']} ({sv['id']}): "))
                if 0 <= diem <= 10:
                    break
                else:
                    print("  Diem phai trong khoang 0-10, nhap lai.")
            except ValueError:
                print("  Vui long nhap so.")
        marks[(sv["id"], course_id)] = diem


# ---------- LISTING FUNCTIONS ----------

def list_courses(courses):
    print("\n=== DANH SACH MON HOC ===")
    if not courses:
        print("(chua co mon hoc nao)")
    for c in courses:
        print(f"  {c['id']} - {c['name']}")


def list_students(students):
    print("\n=== DANH SACH SINH VIEN ===")
    if not students:
        print("(chua co sinh vien nao)")
    for sv in students:
        print(f"  {sv['id']} - {sv['name']} - {sv['dob']}")


def show_marks_by_course(students, courses, marks):
    print("\n=== XEM DIEM THEO MON HOC ===")
    if not courses:
        print("(chua co mon hoc nao)")
        return

    list_courses(courses)
    course_id = input("Nhap ID mon hoc muon xem diem: ")

    course = next((c for c in courses if c["id"] == course_id), None)
    if course is None:
        print("Khong tim thay mon hoc voi ID nay.")
        return

    print(f"\nDiem mon {course['name']} ({course['id']}):")
    for sv in students:
        key = (sv["id"], course_id)
        if key in marks:
            print(f"  {sv['name']} ({sv['id']}): {marks[key]}")
        else:
            print(f"  {sv['name']} ({sv['id']}): chua co diem")


# ---------- MAIN ----------

def main():
    students = []
    courses = []
    marks = {}

    n = input_num_students()
    for _ in range(n):
        students.append(input_student_info())

    m = input_num_courses()
    for _ in range(m):
        courses.append(input_course_info())

    input_marks_for_course(students, courses, marks)

    list_courses(courses)
    list_students(students)
    show_marks_by_course(students, courses, marks)


if __name__ == "__main__":
    main()