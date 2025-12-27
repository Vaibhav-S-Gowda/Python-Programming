# A utility class uses a static method to check if a year is a leap year. 
# You must run this for five sample years.

class Utility:
    
    @staticmethod
    def is_leap_year(year: int) -> bool:
        return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
        
sample_years = [
    2000,
    2024,
    1900,
    2023,
    2100
]

print("--- Leap Year Checker Results ---")
print("Year | Is Lear Year?")

for year in sample_years:
    is_leap = Utility.is_leap_year(year)
    print(f"{year} | {is_leap}")