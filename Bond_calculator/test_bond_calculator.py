import unittest
import math
# Assure-toi que le fichier bond_calculator.py est dans le même dossier
from bond_calculator import BondCalculator

class TestBondCalculator(unittest.TestCase):

    def test_zero_coupon_bond(self):
        """
        Test théorique 1 : Pour une obligation Zéro-Coupon (coupon = 0),
        la Duration doit être exactement égale à la Maturité.
        """
        # Obligation 10 ans, 0% coupon, taux 5%
        bond = BondCalculator(face_value=1000, coupon_rate=0, maturity=10, yield_rate=0.05)
        res = bond.calculate_metrics()
        
        # On utilise assertAlmostEqual pour gérer les petites erreurs d'arrondi flottant
        self.assertAlmostEqual(res['duration'], 10.0, places=4)
        # On retire le print ici pour garder la sortie propre, unittest nous dira si c'est bon

    def test_par_bond(self):
        """
        Test théorique 2 corrigé : Pour obtenir un prix au pair (1000) avec 
        des coupons annuels et une actualisation CONTINUE, le Yield doit être
        le taux équivalent : y = ln(1 + coupon_rate).
        """
        face_val = 1000
        c_rate = 0.05
        # Calcul du yield équivalent pour que Prix == Face Value
        equivalent_yield = math.log(1 + c_rate) 
        
        bond = BondCalculator(face_value=face_val, coupon_rate=c_rate, maturity=5, yield_rate=equivalent_yield)
        res = bond.calculate_metrics()
        
        # Maintenant, ça devrait être exactement 1000
        self.assertAlmostEqual(res['price'], 1000.0, places=2)

    def test_specific_case(self):
        """
        Test de régression : Vérifie que notre exemple manuel donne toujours le même résultat.
        """
        bond = BondCalculator(face_value=100, coupon_rate=0.05, maturity=3, yield_rate=0.04)
        res = bond.calculate_metrics()
        
        self.assertAlmostEqual(res['price'], 102.5462, places=3)
        self.assertAlmostEqual(res['duration'], 2.8613, places=3)

# C'est cette partie qui était probablement manquante ou décalée :
if __name__ == '__main__':
    print("Lancement des tests...")
    unittest.main()