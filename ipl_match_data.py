import pandas as pd

# Load IPL dataset
ipl = pd.read_csv(r"try\tasks\matches.csv")

print("\nIPL Match Dataset\n")
print(ipl.head())


# -----------------------------------
# Dataset Details
# -----------------------------------

print("\nShape of Dataset :", ipl.shape)

print("\nColumn Names:\n")
print(ipl.columns.tolist())


# -----------------------------------
# Matches Played Per Season
# -----------------------------------

season_matches = ipl["season"].value_counts()

print("\nMatches in Each Season:\n")
print(season_matches)


# -----------------------------------
# Teams with Most Wins
# -----------------------------------

team_wins = ipl["winner"].value_counts()

print("\nTop Winning Teams:\n")
print(team_wins.head())

print("\nMost Successful Team :")
print(team_wins.idxmax())


# -----------------------------------
# Famous Venue Analysis
# -----------------------------------

wankhede_data = ipl[
    ipl["venue"] == "Wankhede Stadium"
]

print("\nMatches Played at Wankhede Stadium :")
print(len(wankhede_data))


# -----------------------------------
# Player of the Match Analysis
# -----------------------------------

top_players = (
    ipl["player_of_match"]
    .value_counts()
    .head(5)
)

print("\nTop Performing Players:\n")
print(top_players)


# -----------------------------------
# Missing Values
# -----------------------------------

print("\nMissing Values in Dataset:\n")
print(ipl.isnull().sum())


# -----------------------------------
# Remove Null Records
# -----------------------------------

clean_data = ipl.dropna()

print("\nDataset After Removing Null Values :")
print(clean_data.shape)


# -----------------------------------
# Sort Matches by Season
# -----------------------------------

sorted_data = ipl.sort_values(
    by="season",
    ascending=True
)

print("\nSorted Match Records:\n")
print(sorted_data.head())


# -----------------------------------
# Win Count by Teams
# -----------------------------------

wins_by_team = ipl.groupby("winner").size()

print("\nTotal Wins By Teams:\n")
print(wins_by_team)


# -----------------------------------
# Toss Decision Analysis
# -----------------------------------

batting_first = ipl[
    ipl["toss_decision"] == "bat"
]

fielding_first = ipl[
    ipl["toss_decision"] == "field"
]

bat_success = (
    (batting_first["toss_winner"] ==
     batting_first["winner"]).mean()
) * 100

field_success = (
    (fielding_first["toss_winner"] ==
     fielding_first["winner"]).mean()
) * 100


print("\nToss Decision Success Rate:\n")

print(f"Bat First Win Rate   : {bat_success:.2f}%")
print(f"Field First Win Rate : {field_success:.2f}%")


# -----------------------------------
# Final Output
# -----------------------------------

print("\nIPL Data Analysis Finished Successfully!")