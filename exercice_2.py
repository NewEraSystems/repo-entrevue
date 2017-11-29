from abc import ABCMeta

class Product:

    __metaclass__ = ABCMeta
    _product_name = "Base Product"
    _unit_price = 0
    _is_free = False

    def get_price(self):
        return 0 if self._is_free else self._unit_price

    def set_free(self):
        self._is_free = True

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

    def apply_offer(self, offer):

        if not isinstance(offer, Offre):
            return

        offer.process(self._products)

class Offre:

    __metaclass__ = ABCMeta
    _product_class = None
    _nth_free = -1

    def __init__(self, product_class, nth_free):
        self._product_class = product_class
        self._nth_free = nth_free

    def process(self, products):
        product_count = 0
        for i in range(len(products)):

            if products[i]._product_name == self._product_class:
 
                product_count += 1
                if not product_count % (self._nth_free):
                    products[i].set_free()

class OffrePomme(Offre):

    def __init__(self):
        Offre.__init__(self, "Pomme", 2)

    def process(self, products):
        Offre.process(self, products)

class OffreOrange(Offre):

    def __init__(self):
        Offre.__init__(self, "Orange", 3)

    def process(self, products):
        Offre.process(self, products)
