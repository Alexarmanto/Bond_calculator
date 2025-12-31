import matplotlib.pyplot as plt
import numpy as np
from bond_calculator import BondCalculator

def plot_price_vs_yield():
    # 1. Paramètres de l'obligation
    face_value = 1000
    coupon_rate = 0.05
    maturity = 10
    
    # 2. Création d'une plage de taux (Yields) de 0% à 15%
    yields = np.linspace(0.001, 0.15, 50) # 50 points
    prices = []
    
    # 3. Calcul du prix pour chaque taux
    for y in yields:
        bond = BondCalculator(face_value, coupon_rate, maturity, yield_rate=y)
        res = bond.calculate_metrics()
        prices.append(res['price'])
        
    # 4. Création du graphique
    plt.figure(figsize=(10, 6))
    plt.plot(yields * 100, prices, label='Prix de l\'obligation', color='blue', linewidth=2)
    
    # Ajout d'un point rouge pour la situation actuelle (ex: yield 5%)
    current_yield = 0.05
    bond_curr = BondCalculator(face_value, coupon_rate, maturity, current_yield)
    curr_price = bond_curr.calculate_metrics()['price']
    plt.scatter([current_yield * 100], [curr_price], color='red', zorder=5, label=f'Yield 5% : ${curr_price:.2f}')
    
    # Esthétique
    plt.title(f"Relation Prix-Rendement (Maturité {maturity} ans, Coupon {coupon_rate*100}%)")
    plt.xlabel("Yield (%)")
    plt.ylabel("Prix ($)")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    print("Graphique généré !")
    plt.show()

if __name__ == "__main__":
    plot_price_vs_yield()