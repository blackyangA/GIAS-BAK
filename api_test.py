from pprint import pprint

import requests


# 139.224.192.64


def student_add():
    url = "http://139.224.192.64:5901/api/student/"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyNjk2MzcwLCJpYXQiOjE2NDgzNzYzNzAsImp0aSI6ImUyMGMxZDg5OGY3MjQzNGJiZDQxY2I3NjdjMTBmN2JlIiwidXNlcl9pZCI6MX0.qCZr4FJXI5nepH-1-89-rWQVIe4qJbcLsH5VHS_1ddE"
    }
    data = {
        "s_id": "1001",
        "s_name": "洋洋洋",
        "sex": "男",
        "ethnic": "汉族",
        "political_a": "中共党员",
        "homeland": "北京",
        "birthday": "2020-01-02",
        "id_no": "120593200001023022",
        "qq": "88888888",
        "phone": "13888888888",
        "data_status": 11,
    }
    response = requests.post(url=url, headers=headers, json=data)
    print(response.json())


def subject_add():
    url = "http://139.224.192.64:5901/api/subject/"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyNjk2MzcwLCJpYXQiOjE2NDgzNzYzNzAsImp0aSI6ImUyMGMxZDg5OGY3MjQzNGJiZDQxY2I3NjdjMTBmN2JlIiwidXNlcl9pZCI6MX0.qCZr4FJXI5nepH-1-89-rWQVIe4qJbcLsH5VHS_1ddE"
    }
    data = {
        "s_id": "1001",
        "maths": 100,
        "english": 100,
        "physics": 100,
        "computer_networks": 100,
        "c_language": 100,
        "data_structure": 100,
        "computer": 100,
        "network_programming": 100,
        "network_security": 100,
    }
    response = requests.post(url=url, headers=headers, json=data)
    print(response.json())


def overall_add():
    url = "http://139.224.192.64:5901/api/overall/"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyNjk2MzcwLCJpYXQiOjE2NDgzNzYzNzAsImp0aSI6ImUyMGMxZDg5OGY3MjQzNGJiZDQxY2I3NjdjMTBmN2JlIiwidXNlcl9pZCI6MX0.qCZr4FJXI5nepH-1-89-rWQVIe4qJbcLsH5VHS_1ddE"
    }
    data = {
        "s_id": "1001",
        "community_activities": 100,
        "sports": 100,
        "physical_test": 100,
        "computer_grade_exams": 100,
        "english_grade_exams": 100,
    }
    response = requests.post(url=url, headers=headers, json=data)
    print(response.json())


def design_add():
    url = "http://139.224.192.64:5901/api/design/"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyNjk2MzcwLCJpYXQiOjE2NDgzNzYzNzAsImp0aSI6ImUyMGMxZDg5OGY3MjQzNGJiZDQxY2I3NjdjMTBmN2JlIiwidXNlcl9pZCI6MX0.qCZr4FJXI5nepH-1-89-rWQVIe4qJbcLsH5VHS_1ddE"
    }
    data = {
        "s_id": "1001",
        "linux": 100,
        "c": 100,
        "java": 100,
        "python": 100,
        "web": 100,
        "graduation_design": 100,
    }
    response = requests.post(url=url, headers=headers, json=data)
    print(response.json())


def user_add():
    url = "http://localhost:5902/api/users/"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUzNDEwMjM2LCJpYXQiOjE2NDkwOTAyMzYsImp0aSI6ImExODQ3MGVhMjRlZTRkMTRhNTFkNjg0NzJkYmY1NzM0IiwidXNlcl9pZCI6MX0.sZF1D-AGFhiNVM4mAbrV6WaoSB7oGz32nLha6f6ONjc"
    }
    data = {
        # 'url': '',
        # 'first_name': 'zsh',
        # 'last_name': 'zshh',
        'username': 'lin3',
        'password': '123456',
        'is_active': 1,
        # 'groups': [],
        'is_staff': 0,
        'is_superuser': 0,
        's_id': '1304'
    }

    response = requests.post(url=url, headers=headers, data=data)
    print(f"status_code:{response.status_code}")
    print(response.json())


def get_users():
    url = "http://139.224.192.64:5901/api/users/"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyNjk2MzcwLCJpYXQiOjE2NDgzNzYzNzAsImp0aSI6ImUyMGMxZDg5OGY3MjQzNGJiZDQxY2I3NjdjMTBmN2JlIiwidXNlcl9pZCI6MX0.qCZr4FJXI5nepH-1-89-rWQVIe4qJbcLsH5VHS_1ddE"
    }
    response = requests.get(url=url, headers=headers)
    pprint(response.json())


def user_update():
    url = "http://139.224.192.64:5901/api/users/3/"
    headers = {
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyNjk2MzcwLCJpYXQiOjE2NDgzNzYzNzAsImp0aSI6ImUyMGMxZDg5OGY3MjQzNGJiZDQxY2I3NjdjMTBmN2JlIiwidXNlcl9pZCI6MX0.qCZr4FJXI5nepH-1-89-rWQVIe4qJbcLsH5VHS_1ddE"
    }
    data = {'success': True,
            'data': {'url': 'http://139.224.192.64:5901/api/users/3/', 'first_name': 'zsh', 'last_name': 'zshh',
                     'username': 'zhu', 'email': 'zhu@zhu.ccom', 'is_active': 1, 'groups': [], 'is_staff': 0,
                     'is_superuser': 0, 's_id': '1002'}}
    response = requests.put(url=url, headers=headers, json=data)
    print(response.json())


def test_login():
    url = "http://139.224.192.64:5901/api/token/"
    # headers = {
    #     "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUyNjk2MzcwLCJpYXQiOjE2NDgzNzYzNzAsImp0aSI6ImUyMGMxZDg5OGY3MjQzNGJiZDQxY2I3NjdjMTBmN2JlIiwidXNlcl9pZCI6MX0.qCZr4FJXI5nepH-1-89-rWQVIe4qJbcLsH5VHS_1ddE"
    # }
    data = {
        "username": "admin",
        "password": "1234567",
    }
    response = requests.post(url=url, data=data)
    print(response.status_code)
    pprint(response.json())


if __name__ == '__main__':
    # student_add()
    # subject_add()
    # overall_add()
    # design_add()
    # get_users()
    # user_update()
    # user_add()
    test_login()