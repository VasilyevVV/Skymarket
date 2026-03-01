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

    @property
    def price(self):
        """ "Метод-геттер для получения цены товара"""
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
