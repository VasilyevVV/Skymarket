from src.Product import LawnGrass, Product, Smartphone


def test_print_mixin(capsys):
    Product(name="Xiaomi Redmi Note 14", description="1024GB, Синий", price=12000.0, quantity=14)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Xiaomi Redmi Note 14, 1024GB, Синий, 12000.0, 14)"

    Smartphone("Xiaomi Redmi Note 15", "1024GB, Синий", 25000.0, 10, 90.3, "Note 15", 1024, "Синий")
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Xiaomi Redmi Note 15, 1024GB, Синий, 25000.0, 10)"

    LawnGrass("Клевер газонный", "Цветочный газон", 200.0, 10, "Россия", "14 дней", "Белый, розовый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass(Клевер газонный, Цветочный газон, 200.0, 10)"
