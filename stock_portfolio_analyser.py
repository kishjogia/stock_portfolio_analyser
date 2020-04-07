# ToDo:
# [x] 1. Get stock price from web for a stock
# [x] 2. View several stock prices, read from file
# [x] 3. Show different detail in a table
# [x] 4. Auto update every 60 seconds (run in a thread)
# [ ] 5. Get historical information for stock
# [ ] 6. Put data into SQL DB
# [ ] 7. Show graphical each stock
# [ ] 8. Store stock list in a DB, be able to add/remove via UI

import os
import pandas as pd
import time
from threading import Thread
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
		item[i] = line.split(",")
		if item[i][2].endswith("\n"):
			item[i][2] = item[i][2][:-1]				# remove the trailing \n

		i = i + 1

	return(item)

def get_current_data(stock):
	global curr_value
	global total_chnge
	global percent_chng

	data = get_live_price(stock[0])

	curr_value = (float(stock[1]) * data) / 100
	total_chnge = curr_value - ((float(stock[2])* float(stock[1])) / 100)
	percent_chng = total_chnge / ((float(stock[2])* float(stock[1])) / 100) * 100
	
	return(data)

def get_historical_data(stock):

	return	

def timer_60_secs(stock_list):
	while True:
		i = 0
		# Get the latest price of each of the shares
		for stock in stock_list:
			if stock[0] != 0:
				price = get_current_data(stock)
				# Add the data into a new rows
				df.loc[i] = [stock[0],price,curr_value,stock[1],stock[2],total_chnge,percent_chng]
				
				i = i + 1
		print(df)
		time.sleep(60)

#********
# Main
#********

if __name__ == "__main__":

	# Read the list of shares from a CSV file
	stk_list = get_stock_list()

	# Add column into Pandas
	df = pd.DataFrame(columns=["Ticker", "Price", "Value", "Total", "Cost/Share","Change", "% Change"])

	# Get the data every minute
	get_data_thread = Thread(target=timer_60_secs, args=(stk_list,))
	get_data_thread.start()

#	print(df)

			#print ("Ticker |  Price   |  Value   |  Total   | Cst/Shre | Change  | % Chnge")
			# Show the output
#			print("{:<6s} | {:>7.2f}p | £{:>7.2f} | {:>8.2f} | {:>7.2f}p | {:>7.2f} | {:>7.2f}%" \
#				.format(stock[0],price,curr_value,float(stock[1]),float(stock[2]),total_chnge,percent_chng))