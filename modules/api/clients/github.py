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
        list = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits', headers = {'Set-Cookie': '_gh_sess=Lf%2BHynH7MbPucvrrb1qRFBOu%2Bry6i6VAxF%2BbDKbSmb88eBtT3AAlN4D4SZGT4XaWIr08trgadZWfmflGGrbd7ZvCnB%2Bx6YOBbrL35DfqFTkMN9pRiDgXw0cwC9qvQsAwgXBXq%2BBpD8aqCw3Hmk%2Fe7bdxiLfLcci0B8D%2FzfjcDoEqPivc2W%2Bm6Z%2BXYLUPj7wjOV3DvaeHe%2BMkNYD%2BomRrb1TrLgc%2FeLvOS%2FI6AWCVAcJCutiTxWCZ4DRkdzlsDzOWGfJJLvIS20qmvEfZxBQd9kUH%2BxtAFm1U5KUX1AamzSKPEM0h3VxKntpHtwoOpM3%2F%2BE%2F6%2F9aLp5ph8gmFrz9xIA4DRLH%2FlkoLBC2jonTJyhIw5y0ondJEPAt4HuQ73VXlU8yW5lj6Mf9PoNkJb0%2B%2BxqLDlVpWCqAOa%2FzlR0v1EPeL7NX%2FbVSs%2Bs4%3D--JU9vyC7jfo3hy%2Bvu--FGOvss7tdQy91r5P08LAWw%3D%3D; path=/; secure; HttpOnly; SameSite=Lax'})
        body = list.json()

        return body
    

        