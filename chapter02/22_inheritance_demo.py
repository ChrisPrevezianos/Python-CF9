class Base:
    def __init__(self):
        self.__private = "I am private"
        self._protected = "I am protected"
        self.public = "I am public"

    def __private_method(self):
        return "This is private"
    
    def get_private(self):
        return self.__private
    
    def call_private_method(self):
        return self.__private_method()
    
class Derived(Base):
    def __init__(self):
        super().__init__()
        self.__private = "I am privated in Derived"
    
    def get_derived_private(self):
          return self.__private
    
def main():
    base = Base()
    print(base.public)
    print(base._protected)
    # print(base.__private)
    print(base.get_private())
    print("----------------")

    derived = Derived()
    print(derived.public)
    print(derived._protected)
    print(derived.get_private())
    print(derived.get_derived_private())
    print("----------------")

    print(base._Base__private) # Name Mangling...
    print(derived._Base__private)
    print(derived._Derived__private)

    # print(base.__private)

    print("=" * 31)
    base.__private = "SHFHS"
    print(base.__private)

if __name__ == "__main__":
    main()   