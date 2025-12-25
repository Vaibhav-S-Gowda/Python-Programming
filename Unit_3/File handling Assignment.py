# Assume that you have csv file of emp details that consist of name, empid, dept and sal. Read the file and compute the following values DA = 18% of sal, HRA = 2% of sal.
# Create an output file called as emp_sal.csv where empid, HRA, DA, Gross sal is written back.

import csv

# Input and output file names
input_file = "emp_details.csv"
output_file = "emp_sal.csv"

with open(input_file, mode='r') as infile, open(output_file, mode='w', newline='') as outfile:
    # Read CSV with semicolon delimiter
    reader = csv.DictReader(infile, delimiter=';', skipinitialspace=True)
 
    # Output CSV header
    fieldnames = ['Empid', 'HRA', 'DA', 'Gross']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        salary = float(row['Salary'])

        # Calculations
        DA = 0.18 * salary
        HRA = 0.02 * salary
        Gross = salary + DA + HRA

        # Write to output CSV
        writer.writerow({
            'Empid': row['Empid'],
            'HRA': round(HRA, 2),
            'DA': round(DA, 2),
            'Gross': round(Gross, 2)
        })

print("emp_sal.csv created successfully!")

