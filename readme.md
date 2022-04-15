## Program brief description

- This program takes in a json file representing charging-sessions and a csv file representing cars information, it then uses the information gathered from both files to calculate and measure the amount of "avoided carbon emissions" when users charge their cars with solar-powered chargers as well as the kWh charged. it will then print out each car alphabetically ordered with the kWh Charged and kg CO2 avoided.

## Instructions

- Make sure you have both CSV and JSON file in the same directory as the program
- invoke the program using the following format
  `$ python --cars 'csv_file_name' --charge-sessions 'json_file_name'`

- you can the following in your terminal in the program directory to run the program if everything is set up correct
  `python carbon_calculator.py --cars cars.csv --charge-sessions charge_sessions.json`

## Algorithm Approach

- Steps to get the KWh Charged
  - Calculate the charging time by subtracting the session_end time from the session_start time.
  - Convert it to minutes (to make calculations easier)
  - Get the max charge rate per hour for the car and divide by 60, to convert it to charge rate per minute.
  - Multiply the charge rate per minute by the number of charge session minutes to get the kWh Charged.
- Steps to get the kg CO2 avoided
  - Get the kWh/100 mi
  - Divide (kWh Charger) / (kWh/100mi)
  - Multiply the result by 100 and let's call our result here MPkWh.
  - get the MPGe
  - divide the calculated MPkWh by MPGe and then multiply the result by 0.382
  - the final result would be kg CO2 avoided

# Trade offs & risky decisions

- I assumed that the format of time will always be consistent.
- I assumed that the files would be in the same directory.
- I have used multiple for loops in my solution, which is not ideal for run-time and maybe can be improved.
- formatting and calculations is not the prettiest, which can give a hard time for future co-workers who try to work on the code.

# Possible Improvements & Time spent

- instead of assuming the format of time will be consistent, look for it dynamically in and then parse it.
- instead of assuming the files would be in the same directory, we can instead ask for the full path of the file and build the path.
- use DP or a recursive approach to improve performance and efficiency
- use more clear formatting and variable naming with more comments
- instead of having files locally we can extend the program to connect to databases directly and grab information from there instead.

# Time spent

- I spent around 45 minutes total on coding, most of the time was spent formatting and parsing.
- I came up with the algorithm approach before I started coding in about 15-20 minutes after checking the files.
