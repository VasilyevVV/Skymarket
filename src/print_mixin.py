class PrintMixin:

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        """Метод печатает в консоль информацию от какого класса и с какими параметрами был создан объект"""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
