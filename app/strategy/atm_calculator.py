from app.config.constants import STRIKE_DIFF


def calculate_atm(index_name: str, spot_price: float):

    strike_gap = STRIKE_DIFF[index_name]

    atm = round(spot_price / strike_gap) * strike_gap

    return atm

