import csv
import os

# Add a variable to load a file from a path.
file_to_load = 'Election_Analysis/election_results.csv'
# Add a variable to save the file to a path.
file_to_save = 'Election_Analysis/election_results.txt'

with open(file_to_save, "w") as txt_file:

 # Write some data to the file.
   txt_file.write("Countries in the election\n--------------------------\nArapahoe\nDenver\nJefferson")

# Open the election results and read the file.
with open(file_to_load) as election_data:

 file_reader = csv.reader(election_data)

 headers = next(file_reader)
 print(headers)