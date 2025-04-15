import matplotlib.pyplot as plt
from stock_data import fetch_stock_data

def plot_stock_trends(symbol):
    stock_data = fetch_stock_data(symbol, '2025-01-01', '2025-04-15')
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'])
    plt.title(f'{symbol} ke liye Stock Moolya Trend')
    plt.xlabel('Tareekh')
    plt.ylabel('Moolya')
    plt.show()