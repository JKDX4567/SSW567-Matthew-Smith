import requests

def get_user_repos_commits(user_id):
    repo_url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(repo_url)
    
    if response.status_code != 200:
        if response.status_code == 403:
            raise Exception("Rate limit exceeded")
        #Nothing might be necessarily wrong just out of calls
        else:
            raise Exception(f"Couldn't find {user_id}")
    # 200 is the status code that basically says "ok got it", so it should always be 200

    repos = response.json()
    repo_commit_count = []
    
    for repo in repos:
        repo_name = repo['name']
        commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        commits_response = requests.get(commits_url)
        
        if commits_response.status_code != 200:
            raise Exception(f"Failed to fetch commits for repository {repo_name}")
        
        commits = commits_response.json()
        commit_count = len(commits)
        repo_commit_count.append((repo_name, commit_count))
        # Basically for each repo, gets a list of all the commits and then gets its length,
        # then adds the repo+length into a list to be printed later
        # Note that the length of the commit list should in theory always match the commit count
    
    return repo_commit_count

def print_repo_commit_count(user_id):
    repo_commit_count = get_user_repos_commits(user_id)
    for repo_name, commit_count in repo_commit_count:
        print(f"Repo: {repo_name}. Number of commits: {commit_count}.")

def main():
    user_id = input("Enter GitHub user ID: ")
    print_repo_commit_count(user_id)
    # If error = 403, request limit has been reached

if __name__ == "__main__":
    main()