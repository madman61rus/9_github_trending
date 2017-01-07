import requests
from datetime import datetime,timedelta

def get_trending_repositories(top_size):
    '''Функция возвращает последние проекты на github в количестве top_size и отсортированные по количеству звезд'''

    week_ago = datetime.today() - timedelta(weeks=1)
    params = {'q': 'created:>{}'.format(week_ago.date()),
                             'sort': 'stars',
                             'order': 'desc'}
    response = requests.get('https://api.github.com/search/repositories',params)


    return response.json()['items'][:top_size]

def get_open_issues_amount(repo_owner, repo_name):
    '''Функция возвращает данные по количеству ошибок и  '''
    ACCESS_TOKEN = '5ffd44f5abc9aea3f65db57d1cd3e5183093a0e6'
    params = {'state':'open','access_token': ACCESS_TOKEN}
    response = requests.get('https://api.github.com/repos/{}/{}/issues'.format(repo_owner,repo_name), params)
    return response.json()

if __name__ == '__main__':

    repos = get_trending_repositories(20)
    for repo in repos:
        print ('Репозиторий {} , звезд - {} , количество открытых проблем {} : '.format(repo['name'],repo['stargazers_count'],repo['open_issues']))
        counter = 1
        for issue in get_open_issues_amount(repo.get('owner').get('login'),repo.get('name')):
            print(' {}. описание -  {} , url - {} '.format(counter,issue['title'],issue['html_url']))
            counter += 1
        print()