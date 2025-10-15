import random
import string # Хранилище стринговых символов

import requests


class CreateUrlEndpoint:
    status_code = None
    id = None
    def __init__(self):
        self.url = 'http://172.16.3.87:7070/api'

    def get_auth_token(self):
        url = f'{self.url}/common/auth'
        payload = {'login': 0, 'password': 321}
        response = requests.post(url, json=payload)
        response.raise_for_status() # Проверка, что ответ успешен
        return response

    def get_list_profiles(self):
        url = f'{self.url}/profiles'
        token = self.get_auth_token().text
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверка, что ответ успешен
        return response

    def create_new_profile(self, name, description):
        url = f'{self.url}/profiles'
        token = self.get_auth_token().text
        payload = {"name": name, "description": description}
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post(url, json=payload, headers=headers)
        self.id = response.json()['id']
        return response

    def delete_profile(self):
        id_for_delete = self.id
        url = f'{self.url}/profiles/{id_for_delete}'
        token = self.get_auth_token().text
        headers = {'Authorization': f'Bearer {token}'}
        requests.delete(url, headers=headers)
        return None