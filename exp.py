import datetime
#input date
dob = '1/5/2000'

#date being split based on /
dob_day = int(dob.split("/")[0])
dob_month = int(dob.split("/")[1])
dob_year = int(dob.split("/")[2])

#datetime library being used to get the current date, month and year
today_day = datetime.datetime.now().day
today_month = datetime.datetime.now().month
today_year = datetime.datetime.now().year

#age of user
#To calculate age, DOByear has been subtracted from current year
difference_age = today_year-dob_year

#if the ongoing month number is less than Dob_month, than one will be removed from year, if it is more; than difference_age would stay the same
if today_month < dob_month:
  print(f"age is : {difference_age-1}")
elif today_month > dob_month:
  print(f"age is : {difference_age}")

# if the ongoing month number is same as DOB_month, than the same condition as above will be applied to dates, meaning if todays date is less than dob-date than 1 will be subtracted otherwise it will stay the same
else:
  if today_month == dob_month:
    if today_day < dob_day:
      print(f"age is : {difference_age-1}")
    else:
      print(f"age is : {difference_age}")

    #dont know why this else is added, since everything is covered above
  else:
    print(f"age is : {difference_age}")

#calculating how many days left in next birthday
isPassed = None 
if dob_month > today_month:
  #dob not passed
  difference  = (dob_month - today_month)*30
  #the days are being adjust as per Dob and current date, depending on whether DOB is greater or less than today
  #if it is more, will will add some more days to difference and if is less, we will subtract
  if dob_day > today_day:
    difference = difference + (dob_day-today_day)
  elif dob_day < today_day:
    difference = difference - (today_day-dob_day)
  print(f"{difference} days to your BDAY remains")

elif dob_month < today_month:
  #dob is passed
  #calculation the approx number of days left in next birthday.
  #the below line will calculate the number of days left in current year + the number of approx days in next year before BDay
  difference = (12 - today_month) * 30 + ((dob_month)*30)

  #if the total went above, the below if block will be usefull otherwise, if it is less elif block would be used (which shouldnt be present as it means the birthday still hasnt arived in current year, the calculation for it has already been done above
  if dob_day > today_day:
    difference = difference + (dob_day-today_day)
  #dob hasn't passed (default comment, dont know why it says DOB hasnt passed as this part will only be used if
  elif dob_day < today_day:
    difference = difference - (today_day-dob_day)
  
  print(f"{difference} days to your BDAY remans")
#for the same month
if dob_month == today_month:
    #it means today is your birthday and next one will arrive after 365days
    if dob_day == today_day:
      print("365 days remaning")

    #The below block will work if the birthday is in few days from today or in next year
    elif dob_day > today_day:
      day = dob_day - today_day
      print(f"{day} days to your BDAY are remaining")
    else:
      print(f"{365- (today_day - dob_day)} days remains")


