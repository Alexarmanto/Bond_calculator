import math

class BondCalculator:
    def __init__(self, face_value, coupon_rate, maturity, yield_rate, freq=1):
        self.face_value = face_value
        self.coupon_rate = coupon_rate
        self.maturity = maturity
        self.yield_rate = yield_rate
        self.freq = freq

    def calculate_metrics(self):
        """
        Calcule le Prix, la Duration de Macaulay et la Convexité
        en une seule boucle pour optimiser la performance.
        """
        dt = 1 / self.freq
        coupon_payment = self.face_value * self.coupon_rate * dt
        
        price = 0
        weighted_duration_sum = 0
        weighted_convexity_sum = 0
        
        # 1. Boucle sur les coupons
        periods = int(self.maturity * self.freq)
        for i in range(1, periods + 1):
            t = i * dt
            # Valeur actuelle du Cash Flow
            pv_cf = coupon_payment * math.exp(-self.yield_rate * t)
            
            # Accumulation pour les formules
            price += pv_cf
            weighted_duration_sum += t * pv_cf
            weighted_convexity_sum += (t ** 2) * pv_cf
            
        # 2. Ajout du remboursement final (Principal)
        t_final = self.maturity
        pv_final = self.face_value * math.exp(-self.yield_rate * t_final)
        
        price += pv_final
        weighted_duration_sum += t_final * pv_final
        weighted_convexity_sum += (t_final ** 2) * pv_final
        
        # 3. Calculs finaux (Division par le prix)
        macaulay_duration = weighted_duration_sum / price
        convexity = weighted_convexity_sum / price
        
        return {
            "price": price,
            "duration": macaulay_duration,
            "convexity": convexity
        }

if __name__ == "__main__":
    # Mêmes paramètres que tout à l'heure
    bond = BondCalculator(face_value=100, coupon_rate=0.05, maturity=3, yield_rate=0.04, freq=1)
    
    resultats = bond.calculate_metrics()
    
    print("-" * 30)
    print(f"Prix      : {resultats['price']:.4f}")
    print(f"Duration  : {resultats['duration']:.4f} années")
    print(f"Convexité : {resultats['convexity']:.4f}")
    print("-" * 30)
    