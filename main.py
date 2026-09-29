from bank.fees import apply_fee
from app.calculator import deposit
from bank.account import show_balance




balance = 1000 
print(show_balance(balance))


balance = deposit(balance, 500) 
print(show_balance(balance))



balance = apply_fee(balance, 50) 
print(show_balance(balance))