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

    @property
    def products(self):
        """Метод-геттер возвращает строку со всеми продуктами, используя приватный атрибут '__products'"""
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    def add_product(self, new_product: Product):
        """Метод для добавления продукта в список товаров в категории - атрибут products"""
        if isinstance(new_product, Product):
            self.__products.append(new_product)
            self.product_count += 1
        else:
            raise ValueError("Можно добавлять только объекты класса Product")

    @property
    def product_in_category(self):
        """Метод-геттер для доступа к списку продуктов в категории"""
        return self.__products
