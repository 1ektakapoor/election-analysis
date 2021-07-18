#3.2.8 Decision Statements
counties = ["Araphoe","Denver","Jefferson"]

# if counties[1] == 'Denver':
#     print(counties[1])

# if counties[3] != 'Jefferson':
#     print(counties[2])

# temperature = int(input("What is the temperature outside?"))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")

# What is the score?
# score = int(input("What is your test score? "))

# Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')

# 3.2.9 Membership and Logical Operators
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# if "Araphoe" in counties or "El Paso" in counties:
#     print("Araphoe or El Paso are in the list of counties.")
# else:
#     print("Araphoe or El Paso is not in the list of counties.")

# if "Araphoe" in counties and "El Paso" not in counties:
#     print("Only Araphoe is in the list.")
# else:
#     print("Araphoe is in the list and El Paso is not in the list.")

#3.2.10 Repetition Statements
#x = 0
# while x <= 5:
#     print(x)
#     x = x+1

# for county in counties:
#     print(county)

# numbers = [0,1,2,3,4]
# for num in numbers:
#     print(num)

# for num in range(5):
#     print(num)

# for i in range(len(counties)):
#     print(counties[i])

# counties_tuple = ("Araphoe", "Denver", "Jefferson")

# for county in counties_tuple:
#     print(county)

# for i in range(len(counties_tuple)):
#     print(counties_tuple[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for voters in counties_dict.values():
#     print(voters)

# dictionary.keys > gives you the keys in the dictionary, the for variable does not matter
# dictionary.values > gives your values in the dictionary (same as keys)
#dictionary[key] also gives you the keys

# for county in counties_dict:
#     print(counties_dict[county])

# for county in counties_dict:
#     print(counties_dict.get(county))

# for key, value in counties_dict.items():
#     print(f"{key} county has {value} registered votes.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# range(len(voting_data)) > you get the length of the dictionary then you start the range
# for i in the range we want to print out the county
# so we call the dictionary at the index then we specificially call out the county key
# for county in range(len(voting_data)):
#     print(voting_data[county]['county'])

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# for county_dict in voting_data:
#     for key, value in counties_dict.items():
#         print(value)

# for county_dict in voting_data:
#     for value in counties_dict:
#     print(county_dict["registered_voters"])

#3.2.11 Printing Formats
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes."
# )
# print(message_to_candidate)

for county_dict in voting_data:
    print(f"{county_dict['county']} has {county_dict['registered_voters']:,} voters. ")