import requests


class GitHub:

    def get_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", 
            params ={"q": name}
        )
        body = r.json()

        return body
    
    def get_emoji(self, emoji):
        emo = requests.get(
            "https://api.github.com/emojis", 
            params ={"q": emoji}
        )
        body = emo.json()

        return body

    def list_commits(self, owner, repo):
        list = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')
        body = list.json()

        return body
    

        