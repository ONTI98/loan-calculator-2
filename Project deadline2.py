#programme to work out how many days user has until deadline
#(how many days they have to complete the project)
#user gets prompted for a dealine details
#give answer in weeks and days

import datetime

#user input
user_input=input("When is your dealine (YYYY/MM/DD)? ")

#deadline date
deadline=datetime.datetime.strptime(user_input,"%Y/%m/%d").date()
print(f"Your project deadline is: {deadline}")

#current date(will be subtractred from the dealine date)
current_date=datetime.datetime.now()
print(f"Current date is: {current_date}" )

#how many days until submission
days_until_submission=deadline.day - current_date.day
print(f"{days_until_submission} days until submission")

#final output in a combination of weeks and days.

#weeks from dealine to  current date
weeks=days_until_submission /7
weekss=("{:.2f}".format(weeks))

print(f"you have {days_until_submission} days and {weekss} weeks until you next submission. A re ye,bafanas.")





