class Student :
    def __init__(self, std_id, name, gpa) :
        self.std_id = std_id
        self.name = name
        self.gpa = gpa
    
    def print_detail(self) :
        print("ID:", self.std_id)
        print("Name:", self.name)
        print("GPA:", self.gpa)

class ProbHash:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * size

    def hash(self, key):
        return key % self.size

    def rehash(self, key):
        return (key + 1) % self.size

    def insert_data(self, student):
        index = self.hash(student.std_id)
        
        if self.hash_table[index] is None:
            self.hash_table[index] = student
            print(f"Inserted {student} at index {index}")
        else:
            print(f"Collision at index {index}, trying rehash...")
            original_index = index
            while self.hash_table[index] is not None:
                index = self.rehash(index)
                if index == original_index:
                    print(f"The list is full. {student.std_id} could not be inserted.")
                    return
            self.hash_table[index] = student
            print(f"Inserted {student} at index {index}")

    def search_data(self, std_id):
        """ ค้นหานักศึกษาตาม std_id และคืนค่า index """
        index = self.hash(std_id)
        original_index = index
        
        while self.hash_table[index] is not None:
            if self.hash_table[index].std_id == std_id:
                print(f"Found {std_id} at index {index}")
                return self.hash_table[index]
            index = self.rehash(index)
            if index == original_index:
                break
        
        print(f"{std_id} does not exist.")
        return None

    def display_table(self):
        """ แสดงค่าใน Hash Table """
        for i, val in enumerate(self.hash_table):
            print(f"Index {i}: {val}")

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_detail()
            print("------")
        else:
            print("Invalid Condition!")
main()