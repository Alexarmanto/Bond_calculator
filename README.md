# Bond_calculator


Un calculateur d'obligations (Bond Pricing) utilisant l'**actualisation continue** (Continuous Compounding).
Ce projet calcule le Prix, la Duration de Macaulay et la Convexité.

## Fonctionnalités
- Calcul du **Prix théorique** avec actualisation continue ($e^{-rt}$).
- Calcul de la **Duration de Macaulay** et de la **Convexité**.
- **Visualisation graphique** de la relation Prix/Yield.
- **Tests unitaires** pour valider les cas limites (Zéro-coupon, Au pair).

## Comment l'utiliser
1. Cloner le repo.
2. Lancer le calculateur :
   ```bash
   python bond_calculator.py
