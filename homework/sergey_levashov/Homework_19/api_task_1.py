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

    # получение id из созданного объекта
    new_object = post_response.get('id')

    #  проверка объекта после создания
    get_response = requests.get(
        f'http://objapi.course.qa-practice.com/object/{new_object}',
        headers=headers
    )
    get_response_json = get_response.json()

    assert get_response.status_code == 200, "Ошибка: ожидался статус 200"
    assert get_response_json.get('id') == new_object, "Ошибка: ID не совпадают"


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

    put_response = requests.put(
        'http://objapi.course.qa-practice.com/object/2816',
        json=body,
        headers=headers
    )

    put_response_json = put_response.json()
    assert put_response.status_code == 200, "Ошибка: ожидался статус 200"

    # получение id из объекта
    put_object_id = put_response_json.get('id')

    # Проверка объекта после изменения PUT
    get_response_after = requests.get(
        f'http://objapi.course.qa-practice.com/object/{put_object_id}',
        headers=headers
    )
    assert get_response_after.status_code == 200, "Ошибка: ожидался статус 200"


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

    patch_response = requests.patch(
        'http://objapi.course.qa-practice.com/object/2809',
        json=body,
        headers=headers
    )
    print(patch_response)
    patch_response_json = patch_response.json()
    assert patch_response.status_code == 200, "Ошибка: ожидался статус 200"

    # получение id из объекта
    patch_object_id = patch_response_json.get('id')

    # Проверка объекта после изменения PATCH
    get_response_after = requests.get(
        f'http://objapi.course.qa-practice.com/object/{patch_object_id}',
        headers=headers
    )
    assert get_response_after.status_code == 200, "Ошибка: ожидался статус 200"


patch_object()

'''
Удаление объекта
'''


def del_object():
    headers = {'content-type': 'application/json'}

    #  проверка объекта перед удалением
    get_response_before_del = requests.get(
        'http://objapi.course.qa-practice.com/object/2802',
        headers=headers
    ).json()
    print(get_response_before_del)

    # получение id из ответа
    get_response_id = get_response_before_del.get('id')

    del_response = requests.delete(
        f'http://objapi.course.qa-practice.com/object/{get_response_id}',
        headers=headers)
    assert del_response.status_code == 200, "Ошибка: ожидался статус 200"

    #  проверка объекта после удаления
    get_response_after_del = requests.get(
        f'http://objapi.course.qa-practice.com/object/{get_response_id}',
        headers=headers
    )
    print(get_response_after_del)
    assert get_response_after_del.status_code == 404, "Ошибка: ожидался статус 404"


del_object()
