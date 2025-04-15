from portfolio import add_stock, remove_stock, calculate_portfolio_value
from visualizer import plot_stock_trends
from stock_data import fetch_stock_data

def main():
    while True:
        action = input("'add', 'remove', 'track', 'plot', ya 'quit' darj karein: ")
        if action == 'add':
            symbol = input("Stock prateek darj karein: ")
            shares = float(input("Shares ki sankhya darj karein: "))
            purchase_price = float(input("Kharid moolya darj karein: "))
            add_stock(symbol, shares, purchase_price)
        elif action == 'remove':
            symbol = input("Hataane ke liye stock prateek darj karein: ")
            remove_stock(symbol)
        elif action == 'track':
            print("Kul Portfolio Moolya: ", calculate_portfolio_value(fetch_stock_data))
        elif action == 'plot':
            symbol = input("Stock prateek darj karein jiska trend dekhna hai: ")
            plot_stock_trends(symbol)
        elif action == 'quit':
            break

if __name__ == "__main__":
    main()