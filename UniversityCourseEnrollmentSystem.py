class Course:
    def __init__(self,capacity):
        self.__capacity=capacity
        self.__enrolled= 0

    def get_capacity(self):
        return self.__capacity
    def get_enrolled(self):
        return self.__enrolled
    def set_capacity(self,new_capacity):
        if new_capacity <= 0:
            print("Invalid capacity!")
        elif new_capacity < self.__enrolled:
            print("Cannot reduce capacity below enrolled students!")
        else:
            self.__capacity=new_capacity

    def enroll_students(self,number):
        if number <=0:
            print("Invalid number!")
        elif self.__enrolled + number >self.__capacity:
            print("Not enough seats!")
        else:
           self.__enrolled += number
    def drop_students(self,number):
        if number <=0 or number > self.__enrolled:
            print("Invalid number!")
        else:
           self.__enrolled -= number


course=Course(5)
course.enroll_students(3)
print(course.get_enrolled())
course.set_capacity(2)
course.enroll_students(3)
course.drop_students(1)
course.set_capacity(2)
print(course.get_capacity())
print(course.get_enrolled())