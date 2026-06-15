import numpy as np
import pandas as pd

matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

print('=' * 50)
print('Matches Dataset')
print('=' * 50)
print(f'Shape: {matches.shape}')
print('_' * 50)
print(f'Column Names: {list(matches.columns)}')
print('_' * 50)
print(f'First 5 rows:\n{matches.head()}')
print('_' * 50)
print(f'Number of missing values: \n{matches.isnull().sum()}')
print('_' * 50)
print(f'Datatypes:\n{matches.dtypes}')

print("\n" + "=" * 50)
print('Deliveries Dataset')
print("=" * 50)
print(f'Shape: {deliveries.shape}')
print("_" * 50)
print(f'Column Names: {list(deliveries.columns)}')
print("_" * 50)
print(f'First 5 rows:\n{deliveries.head()}')
print("_" * 50)
print(f'Number of missing values:\n{deliveries.isnull().sum()}')
print("_" * 50)
print(f'Datatypes:\n{deliveries.dtypes}')

matches.fillna({'winner': 'No Result'}, inplace=True)
deliveries.dropna(subset=["batter", "bowler", "total_runs"], inplace=True)

print('\n' + '=' * 50)
print('Matches Analysis\n' + '=' * 50)
team_wins = matches["winner"].value_counts().reset_index()
team_wins.columns = ["Teams", "Wins"]
team_wins.index += 1
print(f"\nTop 5 teams by wins:\n{team_wins.head()}\n")

print('\n' + '=' * 50)
print('Toss Analysis\n' + '=' * 50)
toss_decision = matches["toss_decision"].value_counts().reset_index()
toss_decision.columns = ["Toss Decision", "Count"]
toss_decision["Toss Decision"] = toss_decision["Toss Decision"].str.capitalize()
toss_decision.index += 1
print(toss_decision)

print('\n' + '=' * 50)
matches["toss_match_win"] = matches["toss_winner"] == matches["winner"]
toss_win_rate = matches["toss_match_win"].mean() * 100
print(f"Toss Winner also won the match: {toss_win_rate:.2f}%")

print('\n' + '=' * 50)
matches["date"] = pd.to_datetime(matches["date"])
matches["season"] = matches["date"].dt.year
season_matches = matches.groupby("season")["id"].count().reset_index()
season_matches.columns = ["Season", "Matches"]
season_matches.index += 1
print('Matches per Seasons\n' + '=' * 50)
print(season_matches)

batsman_runs = (deliveries.groupby("batter")["batsman_runs"].sum().reset_index()
                .rename(columns={"batter": "Batter", "batsman_runs": "Total runs"})
                .sort_values("Total runs", ascending=False))
batsman_runs.index += 1
print('\n' + '=' * 50)
print('Top run scores\n' + '=' * 50)
print(batsman_runs.head())

