from github import Github

# using username and password
g = Github("user", "password")

# or using an access token
g = Github("access_token")

# Github Enterprise with custom hostname
g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

for repo in g.get_user().get_repos():
    print("Name of repository:\n" + repo.name)
    repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))

# return list of open issues
repo = g.get_repo("PyGithub/PyGithub")
open_issues = repo.get_issues(state="open")
for issue in open_issues:
    print(issue)

# return list of branches
list(repo.get_branches())
