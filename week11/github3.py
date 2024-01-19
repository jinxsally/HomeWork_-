
#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
import requests
from github import Github

token = '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'

g = Github(token)

user_name="jinxsally"
user = g.get_user(user_name)
followings = user.get_following()
with open('D:\Git\git\homework\week7\Repos.csv', 'w') as f:
    for following in followings:
        print(following)
        f.write(str(following) + '\n')
        repos = following.get_repos()
        for repo in repos:
                print('repositories names:',repo.name)
                f.write('repositories names:'+repo.name+'\n')
                print('repositories url:',repo.url)
                f.write('repositories url:'+repo.url+'\n')
                print('repositories starcount:',repo.stargazers_count)
                f.write('repositories starcount:'+str(repo.stargazers_count)+'\n')
                try:
                    contents = repo.get_contents("")
                    print(contents)
                    for content_file in contents:
                        print(content_file)
                        f.write(str(content_file) + '\n')
                    f.write('\n')
                except Exception as e:
                    print(e,'仓库为空')

