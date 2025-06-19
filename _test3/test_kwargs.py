from tkinter import messagebox

class Test():

    def __init__(self, name, age, country):
        self.name = name
        self.age  = age
        self.country = country
        self.description = ""

    # 변수의 값 반환
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_country(self):
        return self.country
    
    # 설명란 추가
    def add_description(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'description':
                self.description = value
        messagebox.showinfo("설명 부분 추가 성공", "설명 부분을 추가하는데 성공했습니다.")

    # 결과 출력
    def print_result(self):
        result = (
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Country: {self.country}\n"
            f"Description: {self.description}"
        )
        print(result)
        messagebox.showinfo("결과 출력", result)

    # 딕셔너리 to리스트 변환
    def list_to_dict(self):
        return [self.name, self.age, self.country, self.description]
    
    # 리스트 to 딕셔너리 변환
    def dict_to_list(self):
        return {
            "name" : self.name,
            "age" : self.age,
            "country" : self.country,
            "description" : self.description
        }


person = Test("Jeon", 30, "Korea")
person.add_description(description="설명설명.")
person.print_result()
messagebox.showinfo("리스트 결과", person.list_to_dict())

messagebox.showinfo("딕셔너리 결과", )