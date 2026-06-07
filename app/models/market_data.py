from dataclasses import dataclass

@dataclass
class MarketData:
    ticker: str
    price: float
    volume: int = 0
    oi: int = 0