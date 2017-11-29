import unittest
from exercice_2 import Pomme, Orange, Cart
 
class TestUM(unittest.TestCase):
 
    def setUp(self):        

        self.test_matrix = [
            [[Pomme(), Pomme(), Orange(), Pomme()], 3.05],
        ]
 
    def test_matrix(self):

        for i in range(len(self.test_matrix)): 
            cart = Cart()
            products = self.test_matrix[i][0]
            for j in range(len(products)):
                
                cart.add_product(products[j])

            # Conversion de cents vers dollars
            self.assertEqual(cart.get_cart_value()/100.0, self.test_matrix[i][1])
 
if __name__ == '__main__':
    unittest.main()