class Student :
    def __init__(self, id, name, gpa) :
        self.id = id
        self.name = name
        self.gpa = gpa
    
    def get_std_id(self) :
        return self.id
    
    def get_name(self) :
        return self.name
    
    def get_gpa(self) :
        return self.gpa
    
    def print_detail(self) :
        print("ID:", self.get_std_id())
        print("Name:", self.get_name())
        print("GPA:", self.get_gpa())

def main(text_in):
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_detail()
main(input())
