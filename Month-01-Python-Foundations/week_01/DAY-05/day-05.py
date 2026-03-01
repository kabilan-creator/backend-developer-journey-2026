# Example of a decorator that checks for user roles before allowing access to a function

from logging import exception


current_role = {"role": "ADMIN"}

def required_role(role):
    def decorator(func):
        def wrapper(*args,**kwargs):
            if current_role["role"] != role:
                raise Exception(f"Access denied. Required role: {role}")
            return func(*args,**kwargs)
        return wrapper
    return decorator  

@required_role("ADMIN")
def admin_function():
    return "Admin function executed successfully"

print(admin_function())  

# proble solving
# Given an array of prices where prices[i] is the price of a given stock on the ith day, find the maximum profit you can achieve. You may complete at most one transaction (i.e., buy one and sell one share of the stock). Note that you cannot sell a stock before you buy one.
# method : array pointer approach
def price(prices):
    max_p = 0
    min = float('inf')

    for price in prices:
        if price < min:
            min = price
        
        profit = price - min

        max_p = max(max_p,profit)
    return max_p

print(price([7,1,5,3,6,4]))