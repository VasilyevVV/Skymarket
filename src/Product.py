class Product:
    name: str
    description: str
    quantity: int
    # атрибут для сохранения списка продуктов - объектов класса Product
    __product_list: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.__product_list.append(self)

    def __str__(self):
        """
        Строковое отображение для класса Product в формате:
        <Название продукта>, <Цена> руб. Остаток: <Х> шт.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Метод для сложения продуктов. Стоимость каждого товара перемножается на его количество.
        Возвращает полную стоимость всех складываемых товаров.
        """
        return self.quantity * self.price + other.quantity * other.price

    @property
    def price(self):
        """Метод-геттер для получения цены товара"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Метод для изменения цены товара"""
        if new_price < 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        # Если цена товара меньше текущей цены, то запрашивается подтверждение от пользователя
        if new_price < self.price:
            answer = input("Цена товара ниже текущей. Вы согласны изменить цену? Y - 'Да', любая буква - 'Нет': ")
            # Если пользователь ввёл не "Y" - цена не изменяется
            if answer.lower() != "y":
                return
        self.__price = new_price

    @classmethod
    def new_product(cls, new_product_dict: dict):
        """
        Метод для создания продукта из словаря. Если товар уже существует, количество суммируется с добавляемым.
        При конфликте цен выбирается более высокая цена
        """
        for product in cls.__product_list:
            if product.name == new_product_dict["name"]:
                product.quantity += new_product_dict["quantity"]
                product.price = max(product.price, new_product_dict["price"])
                return product
        product_instance = cls(
            name=new_product_dict["name"],
            description=new_product_dict.get("description", "Описание отсутствует"),
            price=new_product_dict.get("price", 0.0),
            quantity=new_product_dict.get("quantity", 0),
        )
        # Альтернативный вариант создания объекта класса Product - распаковка словаря (протестирован)
        # product_instance = cls(**new_product_dict)
        return product_instance


class Smartphone(Product):
    """Конструктор класса Smartphone - наследника класса Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Сложение для объектов класса Smartphone"""
        if type(other) is Smartphone:
            return self.quantity * self.price + other.quantity * other.price
        else:
            raise TypeError("Операция может применяться только к смартфонам")


class LawnGrass(Product):
    """Конструктор класса LawnGrass - наследника класса Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Сложение для объектов класса LawnGrass"""
        if type(other) is LawnGrass:
            return self.quantity * self.price + other.quantity * other.price
        else:
            raise TypeError("Операция может применяться только к товарам класса LawnGrass")
