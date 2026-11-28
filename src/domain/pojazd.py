#glówna kalsa Pojazd , pamieta pozycje x,y ,predkosc,kat obrotu i liczbe okrazen
import math
from abc import ABC, abstractmethod
from src.domain.wyjatki import NiepoprawneParametryError

class Pojazd(ABC):
    def __init__ (self, nazwa_samochodu, x, y, predkosc_max, kat_obrotu,  przyspieszenie, predkosc_skretu):

        if not nazwa_samochodu or not nazwa_samochodu.strip():
            raise NiepoprawneParametryError("Nazwa samochodu nie moze byc pusta")
        if predkosc_max <= 0:
            raise NiepoprawneParametryError("Predkosc maksymalna nie moze byc ujemna")
        if predkosc_skretu <= 0:
            raise NiepoprawneParametryError("Predkosc skretu nie moze byc ujemna")
        if przyspieszenie <= 0:
            raise NiepoprawneParametryError("Przyspieszenie nie moze byc ujemne")

        self._nazwa_samochodu = nazwa_samochodu
        self._x = x
        self._y = y
        self._predkosc = 0.0
        self._predkosc_max = predkosc_max
        self._kat_obrotu = kat_obrotu
        self._liczba_okrazen = 0
        self._przyspieszenie = przyspieszenie
        self._predkosc_skretu = predkosc_skretu

    @property
    def x(self)->float:
        return self._x
    @property
    def y(self)->float:
        return self._y
    @property
    def predkosc(self)->float:
        return self._predkosc
    @property
    def nazwa_samochodu(self)->str:
        return self._nazwa_samochodu
    @property
    def kat_obrotu(self)->float:
        return self._kat_obrotu
    @property
    def liczba_okrazen(self)->int:
        return self._liczba_okrazen
    
    def przyspiesz(self, dt:float):
        if dt < 0:
            raise NiepoprawneParametryError("Czas dt nie moze byc ujemny")  
        self._predkosc = min(self._predkosc_max, self._predkosc + self._przyspieszenie * dt)

    def hamuj(self, dt:float):
        if dt < 0:
            raise NiepoprawneParametryError("Czas dt nie moze byc ujemny")  
        self._predkosc = max(-self._predkosc_max*0.3, self._predkosc - self._przyspieszenie * 1.5 * dt)

    def skrec(self, kierunek:int, dt:float):
        if kierunek not in [-1, 1]:
            raise NiepoprawneParametryError("Kierunek skretu musi byc -1 lub 1")
        if dt < 0:
            raise NiepoprawneParametryError("Czas dt nie moze byc ujemny")
        if abs(self._predkosc) > 1.0:
            self._kat_obrotu += kierunek * self._predkosc_skretu * dt
            self._kat_obrotu %= 360.0

    def aktualizuj_pozycje(self, dt:float,nawierzchnia:str = "asfalt"):
        if dt < 0:
            raise NiepoprawneParametryError("Czas dt nie moze byc ujemny")
        efektywna_predkosc = self._predkosc*self.oblicz_wspolczynnik_nawierzchni(nawierzchnia)
        radiany = math.radians(self._kat_obrotu)
        self._x = self._x + efektywna_predkosc * math.cos(radiany) * dt
        self._y = self._y + efektywna_predkosc * math.sin(radiany) * dt
        self._predkosc *= 0.98 #opór toczenia pojazd sam zwalania po pusczeniu gazu

    def zalicz_okrazenie(self):
        self._liczba_okrazen += 1

    @abstractmethod
    def oblicz_wspolczynnik_nawierzchni(self, nawierzchnia:str)->float:
        pass
    

  

    
    