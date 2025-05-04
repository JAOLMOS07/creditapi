from dataclasses import dataclass

@dataclass
class Product:
    id: str
    name: str
    rate: float
    min_amount: float
    max_amount: float
    min_term: int
    max_term: int
    color: str
