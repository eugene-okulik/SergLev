import requests

'''
Создание объекта
'''


def post_object():
    body = {
        "name": 'Ice Peack',
        "data": {
            "color": "black",
            "size": "small"
        }
    }
    headers = {'content-type': 'application/json'}
    post_response = requests.post(
        'http://objapi.course.qa-practice.com/object',
        json=body,
        headers=headers
    ).json()
    print(post_response)


post_object()

'''
Изменение объекта с помощью метода PUT
'''


def put_object():
    body = {
        "name": 'Ice Peack',
        "data": {
            "color": "yellow",
            "size": "very very big"
        }
    }
    headers = {'content-type': 'application/json'}

    #  проверка объекта перед изменением
    get_response_before = requests.get(
        'http://objapi.course.qa-practice.com/object/2809',
        headers=headers
    ).json()
    print(get_response_before)

    put_response = requests.put(
        'http://objapi.course.qa-practice.com/object/2809',
        json=body,
        headers=headers
    ).json()
    print(put_response)


put_object()

'''
Изменение объекта с помощью метода PATCH
'''


def patch_object():
    body = {
        "name": 'Ice Peack',
        "data": {
            "color": "black",
            "size": "very very small"
        }
    }
    headers = {'content-type': 'application/json'}

    #  проверка объекта перед изменением
    get_response_before = requests.get(
        'http://objapi.course.qa-practice.com/object/2809',
        headers=headers
    ).json()
    print(get_response_before)

    patch_response = requests.patch(
        'http://objapi.course.qa-practice.com/object/2809',
        json=body,
        headers=headers
    ).json()
    print(patch_response)


patch_object()

'''
Удаление объекта
'''


def del_object():
    headers = {'content-type': 'application/json'}

    #  проверка объекта перед удалением
    get_response_before_del = requests.get(
        'http://objapi.course.qa-practice.com/object/2805',
        headers=headers
    ).json()
    print(get_response_before_del)

    requests.delete(
        'http://objapi.course.qa-practice.com/object/2805',
        headers=headers)

    #  проверка объекта после удаления
    get_response_after_del = requests.get(
        'http://objapi.course.qa-practice.com/object/2805',
        headers=headers
    )
    print(get_response_after_del)


del_object()
