class Person:
    def __init__(self, name):
        self._name = name
   
    def get_name(self):
        if not hasattr(self, '_name'):
            return "Name attribute has been deleted."
        print("Getting name", end=": ")
        return self._name
   
    def set_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        print("Setting name", end=": ")
        self._name = value
   
    def del_name(self):
        print("Deleting name...")
        del self._name
   
    name = property(get_name, set_name, del_name, "This is 'name' property")
 
def main():
    p = Person("John")
    # print(p.get_name())
    # p.set_name("Nikias")
    # print(p.get_name())
    p.name = "Nikias"
    print(p.name)
 
if __name__ == "__main__":
    main()
