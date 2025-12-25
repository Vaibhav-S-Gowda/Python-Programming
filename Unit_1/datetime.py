from datetime import datetime, time
import sys

print(f'The current day is {datetime.now().strftime("%w")}')


#%d - day of the month
#%j - day of the year(3 digits 1 to 365)
#%b %B - month name ( abbr, full)
#%m - month of the yaer
#%y %Y - year (2 digits, 4 digits)
#%H %I - hour (24 hour, 12 hour)

#Accessing system Information
# a. Version

print(f'The python version is {sys.version}')

# b. Operating System

print(f'The Operation system is {sys.platform}')

