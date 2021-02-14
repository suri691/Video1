for i in range(0,100):
	print(i+1)

print("loop ended")

for price in range(0,500,100):
 	print(price+100)

for price in range(0,1000,200):
  	print(price+200)	

for price in range(10,2000,500):
	print(price+100)

price_list = [15000.05, 15000.15, 15200.25, 15300.35]

print(len(price_list))

for i in range(0,len(price_list)) :	
	print(price_list[i]*10)
	

win_trades = 100
average_win = 400
amount_made = 200*100
loss_trades = 150
average_loss = 500
amount_lost = 150*50
profit_factor = (amount_made/amount_lost)	

print(profit_factor)

daily_timeframe = [15119.15, 15168.25, 14977.20, 15106.50, 250000, 1500000]

summation = 0

for list_item in daily_timeframe:
	print(list_item)
	summation = summation+list_item

print(summation)

todaytoday_open = 15119.15
today_high = 15168.25
today_low = 14977.20
today_close = 15106.50


serial_number = [1,2,3]
weekday = ['what','when','why']

for i in serial_number:
	print(i)
	for j in weekday:
		print(j)

'''while(a condistion is true):
	execute action		
'''

last_number = 100
incrementing_number = 1

while incrementing_number <= 100: 	
		print(incrementing_number)
		incrementing_number = incrementing_number + 1	

ending_numner = 100
incrementing_number = 1 
while True:
	print(incrementing_number)
	incrementing_number = incrementing_number + 1

	if(incrementing_number > ending_numner):
		break	

print("ended loop")


for i in range(0,2000,100):		
	print(i+100)

daily_timeframe = [15119.15, 15168.25, 14977.20, 15106.50, 250000, 1500000]
for list_item in daily_timeframe:
	print(list_item)
	print(len(daily_timeframe))

	print(len(daily_timeframe))

	for i in range (0,len(daily_timeframe)):
		print(daily_timeframe[i]*10)



win_trades = 100
average_win = 400
amount_made = 200*100
loss_trades = 150
average_loss = 500
amount_lost = 150*50
profit_factor = (amount_made/amount_lost)	

print(profit_factor)

volume_list = [2500,1452022,558555,545855,84455]

summation = 0

for list_item in volume_list:
 		print(list_item)
 		summation = summation+list_item 
 		print(summation)
 		print(summation/5)
 		print()

nding_numner = 100
incrementing_number = 1 
while True:
	print(incrementing_number)
	incrementing_number = incrementing_number + 1

	if(incrementing_number > ending_numner):
		break	

print("ended loop")
