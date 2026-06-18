from abc import ABC, abstractmethod
 
class AbstractStudentDAO(ABC):
 
    @abstractmethod
    def insert(self, student):
        raise NotImplementedError()
        # pass
   
    @abstractmethod
    def update(self, student_id, student):
        raise NotImplementedError()
   
    @abstractmethod
    def delete(self, student_id):
        raise NotImplementedError()
   
    @abstractmethod
    def get_one(self, student_id):
        raise NotImplementedError()
 
 
class StudentImpl(AbstractStudentDAO):
    def __init__(self):
        self.students = {}
 
    def insert(self, student):
        student_id = student['id']
        self.students[student_id] = student
        print(f"Inserted student with id: {student_id}")
   
    def update(self, student_id, student):
        if student_id in self.students:
            self.students[student_id] = student
            print(f"Updated student with id: {student_id}")
        else:
            print(f"Student with id {student_id} not found.")
   
    def delete(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student with id {student_id} deleted")
        else:
            print(f"Student with id {student_id} not found.")
   
    def get_one(self, student_id):
        return self.students.get(student_id, None)
 
 
def main():
    student_dao = StudentImpl()
 
    student_dao.insert({"id": 1, "name": "John Doe"})
    student_dao.insert({"id": 2, "name": "Bob M."})
    student_dao.update(1, {"id": 1, "name": "Mike Doe"})
    st = student_dao.get_one(1)
    student_dao.delete(2)
 
 
 
if __name__ == "__main__":
    main()