# In python, we can /////raise//// custom errors by using the raise keyword.

payment=int(input("Enter the payment amount:"))
if not payment>20000 and payment<5000:
  raise ValueError("Not a valid payment")


a = int(input("Enter any value between 5 and 9"))

if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")
 