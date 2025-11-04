from typing import List, Optional
from abc import ABC, abstractmethod
 
class Product:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)
    def __init__(self, name: str, price: float=0):
        if not name(0).isalpha() or name(len(name)-1).isdigit():
            raise ValueError("Niepoprawna nazwa produktu")
        else:
            self.name=name
            self.price=price
    def __eq__(self, other):
        return self.name == other.name and self.price == other.price  # FIXME: zwróć odpowiednią wartość
 
    def __hash__(self):
        return hash((self.name, self.price))
 
 
class TooManyProductsFoundError(Exception):
    def __init__(self, max: int, current: int):
        self.max=max
        self.current=current
    def __str__(self):
        return f'too many products'

    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    

class Serwer(ABC):
    @abstractmethod
    def get_entries(self, n_letters:int):
        pass
    
 
# FIXME: Każada z poniższych klas serwerów powinna posiadać:
#   (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#   (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania,
#   (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania
 
class ListServer(Serwer):
    def __init__(self, products: List[Product], n_max_returned_entries: int):
        if not isinstance(products, list):
            raise ValueError("Produkty nie zostały przekzane jako lista")
        if n_max_returned_entries not in range (3,8):
            raise ValueError("Ilośc produktów musi być między 3 a 7")
        self.products = products
        self.n_max_returned_entries = n_max_returned_entries
    def __str__(self):
        return f"{self.products}"
    
    def get_entries(self, n_letters):
        match=[p for p in self.products if len(p.name)==n_letters]
        if len(match)>self.n_max_returned_entries:
            raise TooManyProductsFoundError(self.n_max_returned_entries, len(match))
        return match
    

        
    
 
 
class MapServer(Serwer):
    def __init__(self, products_: List[Product], n_max_returned_entries: int):
        if not isinstance(products_, list):
            raise ValueError('Produkty nie zostały przekazane jako listy')
        if n_max_returned_entries not in range (3,8):
            raise ValueError("Ilośc produktów musi być między 3 a 7")
        self.products = dict()
        for p in products_:
            self.products[p.name] = p
        self.n_max_returned_entries = n_max_returned_entries
    def __str__(self):
        return f"{self.products}"
    def get_entries(self, n_letters)
        match=[p for p in self.products.values() if len(p.name)== n_letters]
        if len(match)>self.n_max_returned_entries:
            raise TooManyProductsFoundError(self.n_max_returned_entries, len(match))
        return match
 
class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
    def __init__(self, serwer_: Serwer):
        self.serwer = serwer_
    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        try:
            
        except TooManyProductsFoundError:
            return None
        