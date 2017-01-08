import requests
from datetime import datetime,timedelta

def get_trending_repositories(top_size,weeks):

    week_ago = datetime.today() - timedelta(weeks)
    params = {'q': 'created:>{}'.format(week_ago.date()),
                             'sort': 'stars',
                             'order': 'desc'}
    response = requests.get('https://api.github.com/search/repositories',params)


    return response.json()['items'][:top_size]


def get_open_issues_info(repo_owner,repo_name):
    access_token = '5ffd44f5abc9aea3f65db57d1cd3e5183093a0e6'
    params = {'state': 'open', 'access_token': access_token}
    response = requests.get('https://api.github.com/repos/{}/{}/issues'.format(repo_owner, repo_name), params)
    return response.json()

def print_to_console(repos):
    for repo in repos:
        print('Репозиторий {} , звезд - {} , количество открытых проблем {} : '.format(repo['name'],
                                                                                       repo['stargazers_count'],
                                                                                       repo['open_issues']))
        counter = 1
        for issue in get_open_issues_info(repo.get('owner').get('login'), repo.get('name')):
            print(' {}. описание -  {} , url - {} '.format(counter, issue['title'], issue['html_url']))
            counter += 1
        print()

if __name__ == '__main__':
    top_size=20
    weeks=1
    repos = get_trending_repositories(top_size,weeks)
    print_to_console(repos)
