import shutil

from github import Github
from datetime import datetime
import random
import string
import git
import os

github_token = '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'
github_username = 'gagasheka'
repo_name = 'test_repo'

def create_github_repository(repo_name, token):
    # Создание репозитория на GitHub
    g = Github(token)
    user = g.get_user()

    try:
        repo = user.create_repo(repo_name, auto_init=True)
        print(f"Репозиторий '{repo_name}' успешно создан!")
    except Exception as e:
        print(f"Не удалось создать репозиторий. Причина: {e}")


# создание нового репо
# create_github_repository(repo_name, github_token)

# def list_github_repositories(username, token):
#     g = Github(token)
#     user = g.get_user(username)
#
#     list_of_repos = []
#
#     for repo in user.get_repos():
#         list_of_repos.append(repo.name)
#
#     return list_of_repos[0]
#
# print(list_github_repositories(github_username, github_token))


def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def contribute_to_repository(repo_name, token):
    g = Github(token)
    user = g.get_user()
    repo = user.get_repo(repo_name)

    # Устанавливаем желаемую дату
    contribution_date = datetime(2024, 2, 4, 14, 0, 0)  # 14:00 on Feb 4, 2024

    # Создаем новый файл с рандомным именем
    random_file_name = generate_random_string(10) + ".txt"
    random_file_content = f"Random contribution by {user.login}"

    try:
        # Создаем файл
        repo.create_file(random_file_name, "Random contribution", random_file_content, branch="main")

        # Клонируем репозиторий в существующую директорию
        repo_dir = f"./{repo_name}_clone"
        repo_clone_url = repo.clone_url
        git.Repo.clone_from(repo_clone_url, repo_dir)

        # Устанавливаем конфигурацию пользователя
        repo_config = git.Repo(repo_dir).config_writer()
        repo_config.set_value('user', 'name', 'Your Name')
        repo_config.set_value('user', 'email', 'you@example.com')
        repo_config.release()

        # Фиксируем изменения с установкой желаемой даты
        repo = git.Repo(repo_dir)
        repo.git.add('.')
        repo.git.commit('-m', 'Random contribution', '--date', contribution_date.strftime('%a %b %d %H:%M %Y %z'))

        print(f"Случайная контрибуция внесена успешно.")
    except Exception as e:
        print(f"Не удалось внести случайную контрибуцию. Причина: {e}")
    finally:
        # Не удаляем временную директорию, так как она уже существует
        pass



contribute_to_repository(repo_name, github_token)