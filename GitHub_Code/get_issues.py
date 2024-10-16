import pandas as pd
from github import Github
import time

token = "ghp_xxx"
g = Github(token)
repo_src = 'Selected_Projects.csv'
issue_src = 'Extracted_Issues.csv'

start = False
df_repo = pd.read_csv(repo_src, encoding='latin-1')
for index, paper in df_repo.iterrows():
    df_issue = pd.DataFrame()
    print(f'[{index + 1}] {paper["Repo_Name"]}')
    repo_name = paper['Repo_Name']
    try:
        repo = g.get_repo(repo_name)
    except:
        print("wrong")
        continue
    open_issues = repo.get_issues(state="open")
    closed_issues = repo.get_issues(state="closed")
    
    num_stars = repo.stargazers_count
    num_forks = repo.forks_count
    contributors = repo.get_contributors()
    num_contributors = len(list(contributors))
    des = repo.description
    lang = repo.language
    topics = repo.get_topics()
    topics_string = "#".join(topics) 
    print("Begin Get Sum")

    num_issue_open = sum(issue.pull_request is None for issue in open_issues)
    num_issue_closed = sum(issue.pull_request is None for issue in closed_issues)
    
    issue_labels = repo.get_labels()

    used_labels = set()
    issue_list = []
    for issues in [open_issues, closed_issues]:
        for issue in issues:
            remaining_limit = 0
            while remaining_limit < 100:
                try:
                    remaining_limit = g.get_rate_limit().core.remaining
                except Exception as e:
                    remaining_limit = 0
            row_num = len(df_issue)
            print(row_num)
            if issue.pull_request is None:
                df_issue.loc[row_num, 'Title'] = issue.title
                df_issue.loc[row_num, 'Repo_Name'] = repo_name
                df_issue.loc[row_num, 'State'] = issue.state
                df_issue.loc[row_num, 'Proposed_By'] = issue.user._identity
                df_issue.loc[row_num, 'Date_Created'] = issue.created_at
                df_issue.loc[row_num, 'Date_Closed'] = issue.closed_at
                df_issue.loc[row_num, 'Num_Comment'] = issue.comments
                df_issue.loc[row_num, 'Label'] = "#".join([label.name for label in issue.labels])
                df_issue.loc[row_num, 'Identity_Repo'] = issue._identity
                df_issue.loc[row_num, 'Identity_Global'] = issue.id
                df_issue.loc[row_num, 'Issue_Link'] = issue.html_url
                df_issue.loc[row_num, 'Body'] = issue.body
                issue_list.append(str(issue._identity))
            used_labels.update([label.name for label in issue.labels])

    df_repo.loc[index, 'Issue_Types'] = "#".join([label.name for label in issue_labels])
    
    print(f'[{repo_name}]')
    print(f'Number of stars: {num_stars}')
    df_repo.loc[index, 'Num_Star'] = num_stars

    print(f'Number of forks: {num_forks}')
    df_repo.loc[index, 'Num_Fork'] = num_forks
    
    print(f'Number of contributors: {num_contributors}')
    df_repo.loc[index, 'Num_Contributor'] = num_contributors
    
    #print(f'Number of closed issues: {num_issue_closed}')
    df_repo.loc[index, 'Language'] = lang
    
    #print(f'Number of closed issues: {num_issue_closed}')
    df_repo.loc[index, 'Description'] = des
    
    #print(f'Number of closed issues: {num_issue_closed}')
    df_repo.loc[index, 'Topics'] = topics_string
    
    print(f'Created at: {repo.created_at}')
    df_repo.loc[index, 'Date_Created'] = repo.created_at

    print(f'Last updated at: {repo.updated_at}')
    df_repo.loc[index, 'Date_Last_Mod'] = repo.updated_at

    print(f'Number of issues: {num_issue_open}')
    df_repo.loc[index, 'Num_Issue'] = num_issue_open + num_issue_closed
    
    print(f'Number of issue types: {issue_labels.totalCount}')
    df_repo.loc[index, 'Num_Issue_Type'] = issue_labels.totalCount

    print(f'Number of open issues: {num_issue_open}')
    df_repo.loc[index, 'Num_Issue_Open'] = num_issue_open

    print(f'Number of closed issues: {num_issue_closed}')
    df_repo.loc[index, 'Num_Issue_Closed'] = num_issue_closed
  
    df_repo.to_csv(repo_src, index=False)
    df_issue.to_csv(issue_src, index=False, mode='a', header=False)
    
    
    
    
    
    
    
