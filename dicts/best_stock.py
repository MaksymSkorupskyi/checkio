"""Best Stock
You are given the current stock prices. You have to find out which stocks cost more.

Input: The dictionary where the market identifier code is a key and the value is a stock price.
Output: The market identifier code (ticker symbol) as a string.

Example:
best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
Preconditions: All the prices are unique.
"""


# v1 - simple iteration
def best_stock(stocks: dict) -> str:
    """ Return market identifier code (ticker symbol) which stocks cost more """
    stock = ''
    value = 0
    for k, v in stocks.items():
        if v > value:
            value = v
            stock = k
    return stock


# v2 - max get
def best_stock(stocks: dict) -> str:
    """ Return market identifier code (ticker symbol) which stocks cost more """
    return max(stocks, key=stocks.get)


if __name__ == '__main__':
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
    print("Coding complete? Click 'Check' to earn cool rewards!")