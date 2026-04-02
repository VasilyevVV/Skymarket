from src.Product import Product


class Category:
    name: str
    description: str

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        """Строковое отображение для класса Category в виде:
        <Название категории>, количество продуктов: <Х> шт.
        Количество продуктов считается из общего числа всех продуктов в списке товаров категории.
        Общее количество складывается из атрибута "Количества" каждого товара.
        """
        total_prod_count = 0
        for product in self.product_in_category:
            total_prod_count += product.quantity
        return f"{self.name}, количество продуктов: {total_prod_count} шт."

    @property
    def products(self):
        """Метод-геттер возвращает строку со всеми продуктами, используя приватный атрибут '__products'"""
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def product_in_category(self):
        """Метод-геттер для доступа к списку продуктов в категории"""
        return self.__products

    def add_product(self, new_product: Product):
        """Метод для добавления продукта в список товаров в категории - атрибут products"""
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            self.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product или его подклассы")

    def middle_price(self):
        """Метод расчёта средней цены товаров в категории. Если в категории товары отсутствуют, возвращается 0"""
        try:
            return round(sum(product.price for product in self.__products) / len(self.product_in_category), 2)
        except ZeroDivisionError:
            return 0
