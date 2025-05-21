def calculate_vat(price):
  pdv=0.2
  res=price*pdv
  return(res)
print(calculate_vat(400))

def usd_to_uah(amount):
  return amount * 39.5
print(usd_to_uah(20))

def monthly_salary(hours, rate):
  return(hours*rate)
print(monthly_salary(20, 10))

def apply_discount(price, discount):
  return(price-(price*(discount/100)))
print(apply_discount(100, 60))

def profit(revenue, cost, tax):
  return((revenue-cost)*(1-(tax/100)))
print(profit(10000, 2000, 20))

def weighted_average_price(prices, quantities):
  c=0
  d=0
  for i in range(len(prices)):
    c+=prices[i]*quantities[i]
    d+=quantities[i]
  return(c/d)
print(weighted_average_price([20, 40, 43, 29, 10], [3, 5, 20, 10, 15]))

def calculate_wacc(equity, debt, cost_of_equity, cost_of_debt, tax_rate):
  return(equity/(equity+debt)*cost_of_equity+(debt/(equity+debt))*cost_of_debt*(1-tax_rate))
print(calculate_wacc(2000, 1000, 100, 200, 0.2))

def monthly_payment(present_value, rate, months):
  return(present_value*((1+rate)**months-1)/rate)
print(monthly_payment(20000, 0.4, 5))

def analyze_prices(prices):
  a=0
  b=0
  count=0
  for i in prices:
    a+=i
    b+=1
  avg=a/len(prices)
  for j in prices:
    if j < avg:
      count+=1
  return(min(prices), max(prices), avg, count)
print(analyze_prices([10, 20 ,23, 17, 39]))

def adjust_for_inflation(income, inflation_rates):
  b=[]
  c=income
  d=0
  for i in inflation_rates:
    c=c*(i+1)
    b.append(c)
  return(b)
print(adjust_for_inflation(10000, [0.08, 0.1, 0.07]))