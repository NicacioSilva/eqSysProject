from django.db import models


class EquationSystem(models.Model):
    MAX_DIGITS = 24
    DECIMAL_PLACES = 12
    a1 = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    b1 = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    c1 = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    a2 = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    b2 = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    c2 = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        coefficients = {
            'a1': str(self.a1),
            'b1': str(self.b1),
            'c1': str(self.c1),
            'a2': str(self.a2),
            'b2': str(self.b2),
            'c2': str(self.c2),
        }
        return str(coefficients)