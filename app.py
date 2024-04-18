# List of candidates
candidates = ["Candidate A", "Candidate B", "Candidate C"]

# Dictionary to store votes
votes = {}

# Function to add votes
def add_vote(candidate):
    if candidate not in votes:
        votes[candidate] = 1
    else:
        print("You have already voted for this candidate.")

# Function to display candidates and get vote
def get_vote():
    for i, candidate in enumerate(candidates):
        print(f"{i+1}. {candidate}")
    vote = int(input("Enter your vote (1-{len(candidates)}): "))
    if vote > 0 and vote <= len(candidates):
        add_vote(candidates[vote-1])
    else:
        print("Invalid vote.")

# Function to display results
def display_results():
    print("Results:")
    for candidate, vote in votes.items():
        print(f"{candidate}: {vote} votes")

# Main function
def main():
    while True:
        print("Welcome to the Student Government Election!")
        get_vote()
        display_results()
        play_again = input("Do you want to vote again? (yes/no): ")
        if play_again.lower() != "yes":
            break

# Call main function
if __name__ == "__main__":
    main()