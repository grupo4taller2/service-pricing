from decimal import getcontext, Decimal

PRECISION = 5
getcontext().prec = PRECISION


class Rule:
    def __init__(self, id, c_km, c_trips_last_30m, c_rating, c_min):
        self.id = id
        self.c_km = Decimal(c_km)
        self.c_trips_last_30m = Decimal(c_trips_last_30m)
        self.c_rating = Decimal(c_rating)
        self.c_min = Decimal(c_min)

    def price_for(self, n_km, n_trips_last_30m, n_rating, n_min):
        result = Decimal('0')
        result += n_km * self.c_km
        result += n_trips_last_30m * self.c_trips_last_30m
        result += n_rating * self.c_rating
        result += n_min * self.c_min
        # FIXME: Sería mejor modelado como una clase Price o similar
        return str(result)
