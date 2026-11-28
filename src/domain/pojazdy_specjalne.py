#klasy konkretnych aut (np. BolidF1, AutoRajdowe), które dziedziczą po klasie glownej Pojazd
from src.domain.pojazd import Pojazd
from src.domain.wyjatki import NiepoprawneParametryError


class BolidF1(Pojazd):
    def __init__(self, x:float, y:float,kat_obrotu:float,nazwa_samochodu:str = "BolidF1"):
        super().__init__(nazwa_samochodu, x, y,340.0, kat_obrotu,260.0,170.0)
    def oblicz_wspolczynnik_nawierzchni(self, nawierzchnia: str) -> float:
        if nawierzchnia == "trawa":
            return 0.25
        elif nawierzchnia == "asfalt":
            return 1.0
        elif nawierzchnia == "szuter":
            return 0.8
        else:
            raise NiepoprawneParametryError("Nieznana nawierzchnia: {}".format(nawierzchnia))

class AutoRajdowe(Pojazd):
    def __init__(self, x:float, y:float,kat_obrotu:float,nazwa_samochodu:str = "AutoRajdowe"):
        super().__init__(nazwa_samochodu, x, y,265.0, kat_obrotu,220.0,190.0)
    def oblicz_wspolczynnik_nawierzchni(self, nawierzchnia: str) -> float:
        if nawierzchnia == "trawa":
            return 0.85
        elif nawierzchnia == "asfalt":
            return 1.0
        elif nawierzchnia == "szuter":
            return 0.9
        else:
            raise NiepoprawneParametryError("Nieznana nawierzchnia: {}".format(nawierzchnia))

class Terenowka(Pojazd):
    def __init__(self, x:float, y:float,kat_obrotu:float,nazwa_samochodu:str = "Terenowka"):
        super().__init__(nazwa_samochodu, x, y,245.0, kat_obrotu,180.0,145.0)
    def oblicz_wspolczynnik_nawierzchni(self, nawierzchnia: str) -> float:
        if nawierzchnia == "trawa":
            return 0.9
        elif nawierzchnia == "asfalt":
            return 1.0
        elif nawierzchnia == "szuter":
            return 0.95
        else:
            raise NiepoprawneParametryError("Nieznana nawierzchnia: {}".format(nawierzchnia))


class Rozoweauto(Pojazd):
    def __init__(self, x:float, y:float,kat_obrotu:float,nazwa_samochodu:str = "Rozowe Auto"):
        super().__init__(nazwa_samochodu, x, y,290.0, kat_obrotu,230.0,160.0)
    def oblicz_wspolczynnik_nawierzchni(self, nawierzchnia: str) -> float:
        if nawierzchnia == "trawa":
            return 0.5
        elif nawierzchnia == "asfalt":
            return 1.0
        elif nawierzchnia == "szuter":
            return 0.9
        else:
            raise NiepoprawneParametryError("Nieznana nawierzchnia: {}".format(nawierzchnia))


