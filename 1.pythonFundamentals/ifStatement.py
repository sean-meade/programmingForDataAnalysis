#This explains IF statements
# Import module
import datetime

today = datetime.datetime.today()
dayofweek = today.weekday()

if dayofweek == 1:
  print("It's Tuesday!")

else:
  print("Unfortunately it's not Tuesday.")

