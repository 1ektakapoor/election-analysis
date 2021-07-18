# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initalizing total vote counter (equivalent to number of rows in CSV)
total_votes = 0

# Declare a list that will contain candidate options
candidate_options = []

# Declaring a dictionary to count the number of votes by candidates
candidate_votes = {}

# Variable holding an empty string for the winning candidate
winning_candidate = ""

# Variable for the winning count equal to zero
winning_count = 0

# Variable for the winning_percentage equal to zero
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read header row and skip it
    # Re: columns are {Ballot ID, County, Candidate}
    headers = next(file_reader)

    # Loop through each row in CSV file (will output a list)
    for row in file_reader:
        total_votes += 1

        # Grabbing each candidates name from the row
        candidate_name = row[2]

        # Adding each candidate name to the overall candidate list, but only unique names
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Candidate name is key for the dictionary, now this begins the tracking to see
            # how many votes each candidate received.
            candidate_votes[candidate_name] = 0

        # We will add one vote onto the candidate's value into the dictionary. Adding this after the if, 
        # because then only unique (aka one) instance of a vote will be counted. Placing the counter here
        # allows for each time vote for the candidate appears in the file, we add a vote then begin on a new row.
        candidate_votes[candidate_name] += 1
    
    with open(file_to_save, 'w') as text_file:
        election_results = (
            f"\nElection Results\n"
            f"-----------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-----------------------\n")

        print(election_results, end= "")

        # Save the final vote count to the text file.
        text_file.write(election_results)

        for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100

            # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            text_file.write(candidate_results)

            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

            # To do: print out the winning candidate, vote count and percentage to terminal.
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}\n"
            f"-------------------------\n"
        )

        # Print out results
        print(f"\n{winning_candidate_summary}")
        text_file.write(winning_candidate_summary)