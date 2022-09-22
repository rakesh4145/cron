
from github import Github
from github import GithubException

PAT = "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"
ORG_NAME = "rakesh4145"
REPO_NAME = "ML_AI"
PERMISSION = "push"

#-------------------------------------------------------------------

user_file = open("./users.txt","r")
users = user_file.readlines()
user_file.close()
gh = Github(login_or_token=PAT)
for user in users:
    try:
        ghuser = gh.get_user(user.strip())
        print(ghuser)
    except GithubException:
        print("Could not detect user {}".format(user.strip()))
        continue
    try:
        gh.get_repo(ORG_NAME+"/"+REPO_NAME).add_to_collaborators(ghuser,PERMISSION)
    except GithubException:
        print("Error in adding user {}".format(user.strip()))
        continue
    print("{} added to repo {}".format(user.strip(),REPO_NAME))
