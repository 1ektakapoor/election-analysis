import csv
import os

# Retrieve Data 
# file_to_load = os.path.join("Resources","election_results.csv")

# Open election results
# election_data = open(file_to_load,'r')
# with open(file_to_load,'r') as election_data:
#     print(election_data)

    # Total number of votes cast
    # Complete list of candidates who received votes
    # Percentage of votes each candidate won
    # Total number of votes each candidate won
    # Winner of the election based on popular vote

# Close the file
# election_data.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_save, 'w') as out_file:
    # Using the with statement open the file as a text file.
    #outfile = open(file_to_save, "w")
    out_file.write("Counties in the Election\n---------------------\n")
    out_file.write("Arapahoe\nDenver\nJefferson")
    
# Close the file
#out_file.close()