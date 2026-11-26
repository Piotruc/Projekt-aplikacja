#glówna kalsa Pojazd , pamieta pozycje x,y ,predkosc,kat obrotu i liczbe okrazen
import math
from abc import ABC, abstractmethod

class Pojazd(ABC):
    def __init__ (self, nazwa_samochodu, x, y,predkosc, predkosc_max, kat_obrotu, liczba_okrazen, przyspieszenie, predkosc_skrętu,predkosc_startowa = 0):
        self.nazwa_samochodu = nazwa_samochodu
        self.x = x
        self.y = y
        self.predkosc = predkosc
        self.predkosc_max = predkosc_max
        self.kat_obrotu = kat_obrotu
        self.liczba_okrazen = liczba_okrazen 
        self.przyspieszenie = przyspieszenie
        self.predkosc_skrętu = predkosc_skrętu
        self.predkosc_startowa = predkosc_startowa

        if self.predkosc_max < 0:
            raise ValueError("Predkosc maksymalna nie moze byc ujemna")
        if self.predkosc_skrętu < 0:
            raise ValueError("Predkosc skrętu nie moze byc ujemna")
        if liczba_okrazen < 0:
            raise ValueError("Liczba okrazen nie moze byc ujemna")
        if przyspieszenie < 0:
            raise ValueError("Przyspieszenie nie moze byc ujemne")
        if predkosc_startowa < 0:
            raise ValueError("Predkosc startowa nie moze byc ujemna")

        liczba_okrazen = 0

        @property
