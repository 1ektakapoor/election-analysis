# Election Audit Analysis
# Overview
### Purpose
A Colorado Board of Elections employee has given the following tasks to complete the election audit being conducted. The election is for their local Congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Get a complete list of the counties which the votes were placed in.
7. Calculate the total number of votes for each county.
8. Calculate the percentage of votes each county received.
9. Determine the largest county of the election based on the percentage of votes the county received.

# Election Audit Results
### Total Votes Cast in the Congressional Election
The total number of votes cast in the election are: 369,711

### County Results Summary
The three counties in the precint for the election are:
* Arapahoe
* Denver
* Jefferson

The respective number of votes and percentage of total votes for each county are as follows:
* Jefferson County received 10.5% of the total vote, with 38,855 votes.
* Denver County received 82.8% of the total vote, with 06,055 votes.
* Arapahoe County received 6.7% of the total vote, with 24,801 votes.

### County with the Largest Number of Votes
The county that received the largest number of votes, or had the largest turnout, was Denver County.

### Candidate Results Summary
The election was between the following three candidates:
* Diana DeGette
* Raymon Anthony Doane
* Charles Casper Stockham

The respective number of votes and percentage of total votes for each candidate are as follows:
* Diana DeGette received 73.8% of the total vote, with 272,892 votes.
* Raymon Anthony Doane received 3.1% of the total vote, with 11,606 votes.
* Charles Casper Stockham received 23.0% of the total vote, with 85,213 votes

### Winning Candidate Summary
The candidate that won the election was Diana DeGette. Diana won the election with a vote count at 272,892 votes. Her votes accounted for 73.8% of the total votes.

# Election Audit Summary
The Colorado Board of Elections can use this script in the future got any elections with a few modifications. The following are a couple of recommendations and/or examples on how to use this script for other elections:
* This script can be modified to be used with any election data. The Board of Elections can save the new election data and modify the script to fetch data from the new file. The modifications would be to change the locations and the names of files that are being loaded and saved, please see the code snippet below to see location in the script and where to make the modification. This modification would provide future flexibility for the Board if they want to achieve quick summaries for other elections.

```
# Add a variable to load a file from a path.
file_to_load = os.path.join("new_folder_location", "new_filename.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("new_folder_location", "new_filename.txt")
```

* With future elections, more data can be gathered and the same logic can be applied. Additional data that can be retrieved about elections are age, sex, or party affiliation. For example, we can apply the logic of unique candidate names to unique ages - the modification would be to loop through the list of ages and retrieve the unique ages and the number of times each age has come up. This logic mirrors the logic the script uses for the candidate and the number of votes each candidate received. Using this modification, the Board would be able to narrow down any age ranges the candidates would need to specifically target to either thank or gather more votes from.
