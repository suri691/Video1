moving_average = 13500
vwap = 15000

print("moving_average is:", moving_average, " \nvwap is:" ,  vwap)

my_name = "neeraj suri"
wife_name = "jharna suri"
daughter_name = "anya suri"

print("my_name is :", my_name, "\t wife_name:", wife_name, "\t daughter_name:", daughter_name) 

statement = " This is first line. \n\t this is second line. "
print(statement) 

open_today = 13500
close_today = 13000
high_today = 13750
low_today = 13250
volume = 300000
date = "22/12/2020"
time = "11:35:00"

print("\nopen_today:",open_today,"\nclose_today",close_today, "\nhigh_today\t", high_today, "\nlow_today\t", low_today, "\nvolume:\t\t", volume, "\ndate:\t\t", date, "\ntime:\t\t", time)

""" tuple amd list their is a difference () - tuple [] is list
Tuple is unchangable and list is called as changebale """

name_list  = ["neeraj", "Jaharna", "Anya"]
print(name_list[0])
print(name_list[1])
print(name_list[2])

print(name_list[0],[1],[2])
name_list [0] = "Savira"
name_list[1]  = "Nishant"

print(name_list)

print(name_list[2])
print(name_list[1])


print(name_list)

name_list.append("karan")
print(name_list)

home_people = [["Neeraj", "Jharna", "Anya", "Savira"],
				[39,36,3,70], 
				["american", "Indian", "austrailian"]]



print((home_people[0][1]),home_people[1][2],home_people[2][1])				

home_people[0] = "Suri",
print(home_people)

price_list = [13500.20, 13100.56, 13200.50, 13400.56]
print(price_list)

price_list.append(13600.52)

print(price_list)

price_list_backup = price_list.copy()

price_list.clear()

print(price_list)

print(price_list_backup)
win_win_list = [ 1,1,1,0,1,0,1,0,1,0,0,1,1,0,1]

print(len(win_win_list))

print(win_win_list.count(1))

win_rate= win_win_list.count(1) / len(win_win_list)

print((win_rate*100), "%")	

Daiy_timeframe = (13500,13200,13250,13450)

print(Daiy_timeframe)

open_today = 13500
close_today = 13000
high_today = 13750
low_today = 13250
volume = 300000
turnover_data = 50000

print("\nopen_today:", open_today, "\nclose_today", close_today, "\nhigh_today",high_today,"\nlow_today", low_today, "\nvolume:", volume, "\nturnover_data:", turnover_data)

today_Volume = 250000
yesterday_volume = 52000022

cumalative_volume = (today_Volume+yesterday_volume)
print(cumalative_volume)

today_closing = 13500
yesterday_closing = 14500
average = (today_closing+yesterday_closing/2)

print(average)

today_pricerange = 1540
yesterday_pricerange = 4568
previous_pricerange = 5845

print("\ntoday_pricerange\t\t",today_pricerange, "\nyesterday_pricerange\t", yesterday_pricerange, "\nprevious_pricerange\t\t", previous_pricerange)


today_turover = 15888
yesterday_turnover = 54455
previous_dayturnover = 544845
daybefore_turnover = 545545

print(today_turover+yesterday_turnover+previous_dayturnover+daybefore_turnover)

from nsepy import get_history
from datetime import date
data = get_history ( symbol = "SBIN", 
	start = date (2015,1,1)),
	 end= date(2015,1,31)
$ pip install nsepy
