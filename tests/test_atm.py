from app.strategy.atm_calculator import calculate_atm

atm = calculate_atm("NIFTY", 23547)

print(f"ATM Strike: {atm}")