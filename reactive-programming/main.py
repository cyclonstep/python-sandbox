import rx

stocks = [
  { 'TCKR' : 'APPL', 'PRICE': 200},
  { 'TCKR' : 'GOOG', 'PRICE': 90},
  { 'TCKR' : 'TSLA', 'PRICE': 120},
  { 'TCKR' : 'MSFT', 'PRICE': 150},
  { 'TCKR' : 'INTL', 'PRICE': 70},
  { 'TCKR' : 'ELLT', 'PRICE': 0}
]

def buy_stock_events(observer, scheduler):
    for stock in stocks:
        if(stock['PRICE'] > 100):
            observer.on_next(stock['TCKR'])
        elif(stock['PRICE'] <= 0):
            observer.on_error(stock['TCKR'])
    observer.on_completed()

source = rx.create(buy_stock_events)

source.subscribe(on_next=lambda value: print("Received Instruction to buy {0}".format(value)),
                 on_completed=lambda: print("Completed trades"),
                 on_error=lambda e: print(e))


# class PrintObserver(Observer):

#     def on_next(self, value):
#         print("Received {0}".format(value))
#     def on_completed(self):
#         print("Done!")
#     def on_error(self, error):
#         print("Error Occurred: {0}".format(error))

# source = Observable.from_list([1,2,3,4,5,6])

# source.subscribe(lambda value: print("Received {0}".format(value)))

