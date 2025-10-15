import pytest
from endpoints.create_url_endpoint import CreateUrlEndpoint
import random
import string # Хранилище стринговых символов

@pytest.fixture()
def create_url_endpoint():
    return CreateUrlEndpoint()

@pytest.fixture()
def random_string():
    return ''.join(random.choices(string.ascii_lowercase, k=10))

@pytest.fixture(autouse=True)
def create_and_delete_profile(create_url_endpoint, random_string):
    """Создание и удаление профиля"""
    name = random_string
    description = random_string
    create_url_endpoint.create_new_profile(name, description)
    print('\nПрофиль создан')
    yield
    create_url_endpoint.delete_profile()
    print('\nПрофиль удален')