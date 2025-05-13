#static method

class math:
    def __init__(self, num):
        self.num = num


    def add(self, n):
        self.num += n

    @staticmethod
    def additin(num1, num2):
        return num1 + num2
    

a = math(5)
print(a.num)

a.add(5)
print(a.num)

