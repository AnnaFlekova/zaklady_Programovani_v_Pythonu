import math

class Locality:
    def __init__ (self, name, coefficient):
        self.name = name
        self.coefficient = coefficient

class Property:
    def __init__(self, locality:Locality): 
        self.locality = locality

class Estate(Property):
    def __init__(self, locality: Locality, estate_type: str, area: int):
        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area

    def calculate_tax (self):
       types = {
           "land": 0.85,
           "building site": 9,
           "forrest": 0.35
       }
       estate_type_coef = types[self.estate_type]
       tax =  math.ceil(self.area * self.locality.coefficient * estate_type_coef)
       return tax


class Residence (Property):
    def __init__(self, locality: Locality, area: int, commercial: bool):
        super().__init__(locality)
        self.commercial = commercial
        self.area = area

    def calculate_tax (self):
        residence_tax_coef = 15
        tax = self.area * self.locality.coefficient * residence_tax_coef
        if self.commercial == True:
            tax = tax * 2
        return math.ceil (tax)



#test
manetin = Locality ("Manětín", 0.8)
brno = Locality ("Brno", 3)

zemedelsky_pozemek = Estate (manetin, "land", 900)
dum = Residence(manetin, 120, False)
kancelar = Residence(brno, 90, True)

print(zemedelsky_pozemek.calculate_tax())
print(dum.calculate_tax())
print(kancelar.calculate_tax())