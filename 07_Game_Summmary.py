game_summary = []

rounds_lost = 0
rounds_won = 0
rounds_played = 1

# Calculate Game Statistics
rounds_won = sum(question["Result"] == "correct" for question in game_summary)
rounds_lost = rounds_played - rounds_won

# Display Game Statistics
percent_win = rounds_won / rounds_played * 100
percent_lost = rounds_lost / rounds_played * 100

print("\n***** Game Statistics *****")
print(f"Total Rounds Played: {rounds_played}")
print(f"Total Rounds Won: {rounds_won}")
print(f"Total Rounds Lost: {rounds_lost}")
print()
print("Thank you for playing!")
