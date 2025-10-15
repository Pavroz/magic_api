
def test_get_auth_token(create_url_endpoint):
    response = create_url_endpoint.get_auth_token()
    print(f'\nТокен авторизации: {response}')
    assert isinstance(response.text, str), "Токен должен быть строкой"
    print('Токен является строкой')
    assert len(response.text) > 0, "Токен пуст"
    print('Длины токена больше 0 символов')
    assert response.status_code == 200
    print('Код ответа 200')


def test_get_list_profiles(create_url_endpoint):
    response = create_url_endpoint.get_list_profiles()
    print(f'\n{response.json()}')
    assert response.status_code == 200
    print('Код ответа 200')
    assert isinstance(response.json(), list), f"Ожидался список, получен {type(response.json())}"
    print('Ответ - это список')
    # Проверка, что ответ является списком
    assert len(response.json()) > 1
    print('Длина списка больше 1')

# def test_create_and_delete_new_profile(create_url_endpoint, random_string):
#     name = random_string
#     description = random_string
#     response = create_url_endpoint.create_new_profile(name, description)
#     print(f'\n{response.json()}')
#     assert response.status_code == 201
#     print('Код ответа 201')
#     assert isinstance(response.json(), dict)
#     print('Ответ - словарь')
#     create_url_endpoint.delete_profile()
#     print('Профиль успешно удален')