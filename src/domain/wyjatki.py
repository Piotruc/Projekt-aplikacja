#klasy z wlasnych bledow - np jak przez przypadek stworzymy auta z ujemna predkoscia

"""Własne wyjątki wykorzystywane w logice wyścigu."""

class BladWysciguError(Exception):
    """Bazowy wyjątek dla wszystkich błędów logiki gry"""
    pass


class NiepoprawneParametryError(BladWysciguError):
    """Rzucany przy podaniu błędnych wartości (np. ujemna prędkość)."""
    pass


class WyscigZakonczonyError(BladWysciguError):
    """Rzucany przy próbie wykonania ruchu po zakończeniu wyścigu."""
    pass