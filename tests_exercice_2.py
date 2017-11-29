import unittest
from exercice_2 import Pomme, Orange, Cart
from exercice_2 import OffrePomme, OffreOrange
 
class TestUM(unittest.TestCase):
 
    def setUp(self):        

        self.test_matrix = [
            [[Pomme(), Pomme(), Orange(), Pomme()], 3.05],
        ]

        self.test_offers_matrix = [
            [[Pomme(), Pomme(), Orange(), Pomme()], [OffrePomme(), OffreOrange()], 2.45],
            [[Pomme(), Pomme()], [OffrePomme(), OffreOrange()], 0.6],
            [[Pomme(), Pomme(), Orange(), Pomme(), Orange(), Orange() ], [OffrePomme(), OffreOrange()], 3.7],
            [[Pomme(), Orange() ], [OffrePomme(), OffreOrange()], 1.85],
            [[], [OffrePomme(), OffreOrange()], 0],
        ]
 
    def test_matrix(self):

        for i in range(len(self.test_matrix)): 
            cart = Cart()
            products = self.test_matrix[i][0]
            for j in range(len(products)):
                
                cart.add_product(products[j])
           
            # Conversion de cents vers dollars
            self.assertEqual(cart.get_cart_value()/100.0, self.test_matrix[i][1])

    def test_offers_matrix(self):

        for i in range(len(self.test_offers_matrix)): 
            cart = Cart()
            products = self.test_offers_matrix[i][0]
            offers = self.test_offers_matrix[i][1]

            # Ajoute les produits au panier
            for j in range(len(products)):
                cart.add_product(products[j])

            # Applique les offres
            for j in range(len(offers)):
                cart.apply_offer(offers[j])
           
            # Conversion de cents vers dollars
            self.assertEqual(cart.get_cart_value()/100.0, self.test_offers_matrix[i][2])
 
if __name__ == '__main__':
    unittest.main()