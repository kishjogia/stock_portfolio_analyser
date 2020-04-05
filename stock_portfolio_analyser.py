# ToDo:
# [x] 1. Get stock price from web for a stock
# [ ] 2. Auto update at configurable setting
# [x] 3. View several stock prices, read from file
# [ ] 4. Show different detail in a table
# [ ] 5. Show graphical each stock
# [ ] 6. Store stock list in a DB, be able to add/remove via UI

from yahoo_fin.stock_info import get_live_price

stock_file = "/storage/emulated/0/development/stock_portfolio_analyser/stock_list.txt"

def get_stock_list():
	# Read the file
	file1 = open(stock_file, "r")
	read_data = file1.read()
	file1.close
	
	# Parse the file, getting each ticker name
	list = read_data.split(",")
	
	return(list)

def get_current_price(stock):
	data = get_live_price(stock)
	
	return(data)

#********
# Main
#********

if __name__ == "__main__":
	# Read the list of shares from a CSV file
	stk_list = get_stock_list()

	# Get the latest price of each of the shares	
	for stock in stk_list:
		price = get_current_price(stock)
		
		print (stock, price)