# ToDo:
# [x] 1. Get stock price from web for a stock
# [ ] 2. Auto update at configurable setting
# [x] 3. View several stock prices, read from file
# [ ] 4. Show different detail in a table
# [ ] 5. Show graphical each stock
# [ ] 6. Store stock list in a DB, be able to add/remove via UI

import os
from yahoo_fin.stock_info import get_live_price

test = os.uname()
if test[0] == "Linux":
	stock_file = "/home/kishj/OneDrive/development/stock_portfolio_analyser/stock_list.txt"
else:
	stock_file = "/storage/emulated/0/development/stock_portfolio_analyser/stock_list.txt"

def get_stock_list():
	rows, cols = (100,3)
	item = [[0]*cols]*rows

	# Read the file
	file1 = open(stock_file, "r")
	read_data = file1.readlines()
	file1.close

	i = 0
	# Parse the file, getting each ticker name
	for line in read_data:
		item[i] = read_data[i].split(",")
		if item[i][2].endswith("\n"):
			item[i][2] = item[i][2][:-1]				# remove the trailing \n

		i = i + 1

	return(item)

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
		if stock[0] != 0:
			price = get_current_price(stock[0])

			curr_value = (float(stock[1]) * price) / 100
			
			# Show the output
			print (stock[0], \
				"Curr Price: {:.2f}p".format(price), \
					"Curr Val: £ {:.2f}".format(curr_value), \
						"Quantity: {:.2f}".format(float(stock[1])), \
							"Cost/Share: {:.2f}p".format(float(stock[2])))