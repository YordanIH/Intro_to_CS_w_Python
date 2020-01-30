class Nematode:

    def __init__(self, body_length: float, gender: str, age: int):

        self.body_length = body_length
        self.gender = gender
        self.age = age

    def __repr__(self):

        return "Nematode({},'{}',{})".format(self.body_length, self.gender, self.age)

    def __str__(self):

        return "Length:{}\nGender:{}\nAge:{}".format(self.body_length,self.gender,self.age)