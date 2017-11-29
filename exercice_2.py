from abc import ABCMeta

class Product:
    __metaclass__ = ABCMeta
    _product_name = "Base Product"
    _unit_price = 0

    def get_price(self):
        return self._unit_price

class Pomme(Product):
    _product_name = "Pomme"
    _unit_price = 60


class Orange(Product):
    _product_name = "Orange"
    _unit_price = 125

class Cart:


    def __init__(self):
        self._products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            return

        self._products.append(product)

    def get_cart_value(self):
        value = 0

        for i in range(len(self._products)):
            value += self._products[i].get_price()

        return value