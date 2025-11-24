import re

def n_name(name):
    return bool(re.fullmatch(r"[A-Za-zА-Яа-яЁё\s]+", name))

def p_phone(phone):
    return bool(re.fullmatch(r"\d{7,15}", phone))

def e_email(email):
    return bool(re.fullmatch(r"[\w\.-]+@[\w\.-]+\.\w{2,4}", email))


class Student:

    def __init__(self,name,phone,age,email):
        self.name=name
        self.phone=phone
        self.age=age
        self.email=email

class Group:
    def __init__(self,title,profession):
        self.title=title
        self.profession=profession
        self.students=[]

    def add_students(self):
        name=input("name:")
        phone=input("phone:")
        age=input("age:")
        email=input("email:")

        if not n_name(name):
            print("name xato , faqat harf bo'lishi kerak")
            return
        if not p_phone(phone):
            print("telefon raqam noto'g'ri")
            return
        if not e_email(email):
            print("email noto'g'ri")
            return

        student=Student(name,phone,age,email)
        self.students.append(student)
        print("student qo'shildi")

    def view_students(self):
        if not self.students:
            print("student yoq")
            return

        for i,item in enumerate(self.students,start=1):
            print(f"{i}. name:{item.name}, phone:{item.phone}, age:{item.age}, email:{item.email}")

    def update_student(self):
        name=input("tahrirlanadigan ism:")

        for i in self.students:
            if i.name==name:
                print("1.ismni o'zgartirish")
                print("2.telefon nomerni o'zgartirish")
                print("3.yoshni o'zgartirish")
                print("4.emailni o'zgartirish")

                tanlang=input("tanlang:")

                if tanlang=="1":
                    i.name=input("yangi ism:")
                elif tanlang=="2":
                    i.phone=input("yangi telefon raqam:")
                elif tanlang=="3":
                    i.age=input("yoshini kiriting:")
                elif tanlang=="4":
                    i.email=input("yangi email ni kiriting:")
                else:
                    print("noto'g'ri tanlov")
                    return
                print("student tahrirlandi")
                return
        print("bunday ismli student topilmadi")

    def delete_student(self):
        name = input("o'chiriladigan ism: ")

        for i in self.students:
            if i.name == name:
                self.students.remove(i)
                print("student o'chirildi")
                return

        print("bunday student yo'q")



class OTM:
    def __init__(self,title):
        self.title=title
        self.groups=[]

    def add_group(self):
        title=input("title:")
        profession=input("profession:")
        group=Group(title,profession)
        self.groups.append(group)
        print("guruh qo'shildi")

    def view_groups(self):
        if not self.groups:
            print("guruh yoq")
            return

        for i,item in enumerate(self.groups,start=1):
            print(f"{i}. title:{item.title}, profession:{item.profession}")


class ERP:
    def __init__(self):
        self.title='ERP'
        self.otms=[]

    def add_otm(self):
        title=input("title:")
        otm=OTM(title)
        self.otms.append(otm)
        print("OTM qo'shildi")

    def view_otms(self):
        if not self.otms:
            print("OTM lar yoq")
            return
        for i,item in enumerate(self.otms,start=1):
            print(f"{i}. {item.title}")

erp=ERP()

def group_manager(group: Group):
    while True:
        kod=input(" 1.add student \n 2.view students \n 3.update student \n 4.delete student \n 5.back \n :")

        if kod=="1":
            group.add_students()
        elif kod=="2":
            group.view_students()
        elif kod=="3":
            group.update_student()
        elif kod=="4":
            group.delete_student()
        else:
            break


def otm_manager(otm: OTM):
    while True:
        kod=input(" 1.add group \n 2.view groups \n 3.group detail \n 4.back \n : ")

        if kod=="1":
            otm.add_group()
        elif kod=="2":
            otm.view_groups()
        elif kod=="3":
            otm.view_groups()
            index=int(input("group_id:"))
            group=otm.groups[index-1]
            group_manager(group)
        else:
            break

def erp_manager(ep: ERP):
    while True:
        kod = input(" 1.add otm \n 2.view otms \n 3.otm detail \n 4.exit \n : ")

        if kod == "1":
            ep.add_otm()
        elif kod == "2":
            ep.view_otms()

        elif kod == "3":
            ep.view_otms()
            index = int(input("otm id: "))
            otm = ep.otms[index - 1]
            otm_manager(otm)

        else:
            break


erp_manager(erp)
