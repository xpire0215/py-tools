from twstock import Stock
from twstock import codes

def main():
    stock = Stock('0056')
    #average_price = stock.moving_average(stock.price, 10)
    print(stock.data[0])

    print(codes['0056'])

if __name__ == "__main__":
    main()
