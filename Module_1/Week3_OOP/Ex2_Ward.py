from abc import ABC, abstractmethod


class Ward:
    def __init__(self, name):
        self.name = name
        self.lst_person = []

    def add_person(self, person):
        self.lst_person.append(person)

    def describe(self):
        print("Ward name: ", self.name)
        for person in self.lst_person:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.lst_person:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        return sorted(self.lst_person, key=lambda x: x.yob)

    def compute_average(self):
        total_age = 0
        count = 0
        for person in self.lst_person:
            if isinstance(person, Teacher):
                total_age += person.yob
                count += 1
        return total_age/count


class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name)
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(f"Student: Name:{self.name}, YOB:{self.yob}, Grade:{self.grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name)
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(
            f"Teacher: Name:{self.name}, YOB:{self.yob}, SUBJECT:{self.subject}")


class Doctor(Person):
    def __init__(self, name, yob, speciality):
        super().__init__(name)
        self.yob = yob
        self.speciality = speciality

    def describe(self):
        print(
            f"Doctor: Name:{self.name}, YOB:{self.yob}, Speciality:{self.speciality}")


if __name__ == "__main__":
    student1 = Student("John", 1990, "A")
    teacher1 = Teacher("Jane", 1980, "Math")
    teacher2 = Teacher("Vinh", 1985, "Physics")
    doctor1 = Doctor("Jack", 1970, "Neurology")
    doctor2 = Doctor("Rose", 1975, "Surgery")
    ward1 = Ward("AIO")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()
    print(ward1.count_doctor())
    ward1.sort_age()
    ward1.describe()
    ward1.compute_average()
