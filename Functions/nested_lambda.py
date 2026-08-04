# YouTube Video Link: https://youtu.be/YFuJ5zcGEQ8

# Example 1
lambda_fn = lambda a=2, b=3:lambda c: a + b + c
fn = lambda_fn()
print(fn(4))

# Example 2
discounted_price = lambda percent: lambda price: price - (price * percent / 100)
ten_percent = discounted_price(10)
print(ten_percent(100))

twenty_percent = discounted_price(20)
print(twenty_percent(200))
