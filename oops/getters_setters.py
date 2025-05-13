class MyClass:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"value: {self.value}")

    @property
    def ten_value(self):
        return 10 * self.value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self.value = new_value / 10
    
obj = MyClass(5)
obj.ten_value = 100 # This will raise an AttributeError
print(obj.ten_value) # This will print 50
obj.show() # This will print "value: 5"