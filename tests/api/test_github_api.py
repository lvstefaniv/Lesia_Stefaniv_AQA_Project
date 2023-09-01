import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user ['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 43
    assert 'become-qa-auto' in r['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('lesia-stefaniv-repo-non-exist')
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('l')
    assert r['total_count'] != 0   

@pytest.mark.api
def test_emojis_list(github_api):
    emo = github_api.get_emoji('https://github.githubassets.com/images/icons/emoji/unicode/1f6be.png?v8')
    assert emo ['wc'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f6be.png?v8'

@pytest.mark.api
def test_existing_emoji(github_api):
    emo = github_api.get_emoji('zzz')
    if 'zzz' in emo:
        assert emo['zzz'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f4a4.png?v8'
    else:
        print('This emoji is not available to use')

@pytest.mark.api
def test_emoji_non_existing(github_api):
    emo = github_api.get_emoji('kalyna')
    if 'kalyna' in emo:
        print (emo['kalyna'])
    else:
        print('This emoji is not available to use')

@pytest.mark.api
def test_oldest_commit(github_api):
    list = github_api.list_commits('lvstefaniv', 'Lesia_Stefaniv_AQA_Project')
    assert '9aa1e19f4be56323f94bf72c55e3798f76aec3ca' in list[-1]

@pytest.mark.api
def test_last_committer(github_api):
    list = github_api.list_commits('lvstefaniv', 'Lesia_Stefaniv_AQA_Project')
    assert 'Lesia Stefaniv' in list[0]