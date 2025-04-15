portfolio = {}

def add_stock(symbol, shares, purchase_price):
    portfolio[symbol] = {'shares': shares, 'purchase_price': purchase_price}

def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]

def calculate_portfolio_value(fetch_stock_data):
    total_value = 0
    for symbol, data in portfolio.items():
        stock_data = fetch_stock_data(symbol, '2025-01-01', '2025-04-15')
        current_price = stock_data['Close'][-1]  # Latest closing price
        total_value += current_price * data['shares']
    return total_value