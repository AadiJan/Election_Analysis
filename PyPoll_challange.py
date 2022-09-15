import csv
import os
from webbrowser import get

file_to_load = os.path.join("Election_Analysis", "election_results.csv")

file_to_save = os.path.join("Election_Analysis", "election_results.txt")

total_votes = 0

candidate_options = []
candidate_votes = {}

county_list = []
county_votes = {}




winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    
    for row in file_reader:
       
        total_votes += 1
        
        candidate_name = row[2]

        county_name = row[1]

        if county_name not in county_list:

          county_list.append(county_name)

          county_votes[county_name] = 0
        county_votes[county_name] += 1
        
        if candidate_name not in candidate_options:
           
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] += 1


with open(file_to_save, "w") as txt_file:
    
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    
    txt_file.write(election_results)
    
    c = (
      f"\nCounty Votes:\n")
    print(str(c))
    txt_file.write(c)
    
    for county_name in county_votes:
       
        votes = county_votes[county_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        m_turnout = max(county_votes, key=county_votes.get)
      
         
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

        
        print(county_results)

       
        txt_file.write(county_results)


    county_turnout =  (
        f"\n-------------------------\n"
        f"Largest County Turnout: {m_turnout}\n"
        f"-------------------------\n")
    print(county_turnout)
    
    txt_file.write(county_turnout)

    for candidate_name in candidate_votes:
       
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        
        print(candidate_results)
        
        txt_file.write(candidate_results)
        
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    
    txt_file.write(winning_candidate_summary)