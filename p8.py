import pandas as pd
from datetime import datetime, timedelta

file_path = "employee.xlsx"
df = pd.read_excel(file_path)

current_date = datetime.today()
previous_dates = [current_date - timedelta(days=i) for i in range(1, 6)]

def count_wfh_wfo(date):
    wfh_count = df[date].str.count("WFH").sum()
    wfo_count = df[date].str.count("WFO").sum()
    return int(wfh_count), int(wfo_count)

current_wfh_count, current_wfo_count = count_wfh_wfo(current_date.strftime("%b %d"))
print(f"On {current_date.strftime('%b %d')}:\nWFH Count: {current_wfh_count}\nWFO Count: {current_wfo_count}\n")

for date in previous_dates:
    wfh_count, wfo_count = count_wfh_wfo(date.strftime("%b %d"))
    print(f"On {date.strftime('%b %d')}:\nWFH Count: {wfh_count}\nWFO Count: {wfo_count}\n")

all_days = [date.strftime("%b %d") for date in [current_date] + previous_dates]
absent_employees = df[df[all_days].isnull().all(axis=1)]["Emp ID"]

print("Employees who haven't filled attendance for all days:")
print(absent_employees.tolist())
