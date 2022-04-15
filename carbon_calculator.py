import json
import csv
import operator
import sys
from datetime import datetime


#making sure the input that is given is correct, and sending an error message that shows the correct form of expected input
if len(sys.argv) != 5:
    print("you entered an incorrect input, the correct usage is the following: python carbon_calculator.py --car 'name_of_your_csv_file' --charge-sessions 'name_of_your_json_file'")
    quit()

if sys.argv[1] != '--cars':
    print("you entered an incorrect input, the correct usage is the following: python carbon_calculator.py --car 'name_of_your_csv_file' --charge-sessions 'name_of_your_json_file'")
    quit()

if sys.argv[3] != '--charge-sessions':
    print("you entered an incorrect input, the correct usage is the following: python carbon_calculator.py --car 'name_of_your_csv_file' --charge-sessions 'name_of_your_json_file'")
    quit()


#getting the filenames input from the user
cars = sys.argv[2]
charge_file = sys.argv[4]


#opening the json file and returning an error message and closing the program if it cannot be opened
try:
    with open(charge_file) as json_f:
        data = json.load(json_f)
except:
    print("json file could not be opened")
    quit()


#opening the csv file and returning an error message and closing the program if it cannot be opened
try: 
    with open(cars) as csv_f:
        reader = csv.reader(csv_f)
        csv_file = list(reader)
except:
    print("csv file could not be opened")
    quit()


#intial variables 
start = "";
end = "";
charge_rate_m = 0;
final_result = []

#main loop to go over the json file data
for i in range(len(data)):
    # get the times by getting the last 4 indexes of the start & end keys which would be our hours:minutes
    start = data[i]["start_time"][-5:]
    end = data[i]["end_time"][-5:]
    # get the number minutes first
    time_1 = datetime.strptime(start, "%H:%M").minute
    time_2 = datetime.strptime(end, "%H:%M").minute
    time_interval = time_2 - time_1

    # get the number hours
    time_1H = datetime.strptime(start, "%H:%M").hour
    time_2H = datetime.strptime(end, "%H:%M").hour
    time_interval_H = time_2H - time_1H

    #loop to add 60 minutes for each hour
    for j in range(time_interval_H):
        time_interval += 60
    
    #note: minutes would make working later with our calculations easier
    
    #loop over the csv file and extract data
    for k in range(len(csv_file) - 1): 
        if (csv_file[k+1][1] == data[i]['model']):
            charge_rate_m = int(csv_file[k+1][3])/60
            kwh100mile = int(csv_file[k+1][5])
            MPGe = int(csv_file[k+1][4])

    # just to make calculating the kg CO2 avoided easier.
    temp = (time_interval * charge_rate_m) / kwh100mile * 100

    #building the new json 
    curr_result={'id': data[i]['id'], 'car name': data[i]['name'], 'kWh charged': round(time_interval * charge_rate_m, 3), 'kg CO2 avoided': round((temp/MPGe) * 0.382, 3)}
    final_result.append(curr_result)
    


# formatting, sorting based on car name, and printing of the final result
temp_result = json.dumps(final_result)
result_to_sort = json.loads(temp_result)
result_to_sort.sort(key=operator.itemgetter('car name'))
print(json.dumps(result_to_sort))

# no need to close files as they are opened using with which does that for us automatically










