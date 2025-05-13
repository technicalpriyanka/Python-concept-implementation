#access modifier
# public private protected

class employee:
    def __init__(self, name):
        self.__name = "Priyanka"

a  = employee("Priyanka")
print(a.__name) # will raise an AttributeError
# print(a.__name) # will raise an AttributeError
# print(a.__employee__name)

print(a.__dir__()) # will show all the attributes of the class


#protected

class employee:


