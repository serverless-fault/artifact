import pandas as pd
from github import Github
import time
import csv

token = "ghp_xxx"
g = Github(token)
repo_src = 'Candidate_Projects.csv'
filter_src = 'Selected_Projects.csv'
start = False
df_repo = pd.read_csv(repo_src, encoding='latin-1')
rows = []
for index, paper in df_repo.iterrows():
    df_filter = pd.DataFrame()
    print(f'[{index + 1}] {paper["Repo_Name"]}')
    repo_name = paper['Repo_Name']
    try:
        repo = g.get_repo(repo_name)
    except:
        print("wrong")
        continue
    
    num_stars = repo.stargazers_count
    num_forks = repo.forks_count
    num_watchers = repo.subscribers_count
    contributors = repo.get_contributors()
    num_contributors = len(list(contributors))
    if num_stars > 100 and num_forks > 10 and num_contributors > 3:
        rows.append([repo_name, num_stars, num_forks, num_watchers, num_contributors])
    print(f'[{repo_name}]')
    print(f'Number of stars: {num_stars}')
    df_repo.loc[index, 'Num_Star'] = num_stars

    print(f'Number of forks: {num_forks}')
    df_repo.loc[index, 'Num_Fork'] = num_forks

    print(f'Number of watchers: {num_watchers}')
    df_repo.loc[index, 'Num_Watcher'] = num_watchers
    
    print(f'Number of contributors: {num_contributors}')
    df_repo.loc[index, 'Num_Contributors'] = num_contributors

    df_repo.to_csv(repo_src, index=False)
    
wtr = csv.writer(open(filter_src, 'w'), delimiter=',', lineterminator='\n')
wtr.writerow(['Repo_Name','Num_Star','Num_Fork','Num_Watcher','Num_Contributors'])
for row in rows:
    wtr.writerow(row)
    
    
    
    
    
    
    
