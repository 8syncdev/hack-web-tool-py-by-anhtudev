'''
    Tác giả: Nguyễn Phương Anh Tú
    - Liên hệ: 0767449819
    - Định nghĩa các phương thức cơ bản cho việc giao tiếp với API
    - Các phương thức cơ bản bao gồm: GET, POST, PUT, DELETE
'''
import requests
from typing import *
from core.interface.i_action_https import IActionHttps



class BaseAttacksMethods(IActionHttps):
    url: str = ""
    parse_option : Literal["json", "text"] = "json"
    proxies = {
        'http': '',
    }


    @staticmethod
    def _get(url: str, options: dict = {}) -> requests.Response:
        data = requests.get(url, **options, proxies=BaseAttacksMethods.proxies)
        if BaseAttacksMethods.parse_option == "json":
            print(data.json())
            return data.json()
        print(data.text)
        return data.text

    @staticmethod
    def _post(url: str, options: dict = {}) -> requests.Response:
        data = requests.post(url, **options, proxies=BaseAttacksMethods.proxies)
        if BaseAttacksMethods.parse_option == "json":
            print(data.json())
            return data.json()
        print(data.text)
        return data.text
    
    @staticmethod
    def _put(url: str, options: dict = {}) -> requests.Response:
        data = requests.put(url, **options, proxies=BaseAttacksMethods.proxies)
        if BaseAttacksMethods.parse_option == "json":
            print(data.json())
            return data.json()
        print(data.text)
        return data.text
    
    @staticmethod
    def _delete(url: str, options: dict = {}) -> requests.Response:
        data = requests.delete(url, **options, proxies=BaseAttacksMethods.proxies)
        if BaseAttacksMethods.parse_option == "json":
            print(data.json())
            return data.json()
        print(data.text)
        return data.text
    
    @staticmethod
    def _patch(url: str, options: dict = {}) -> requests.Response:
        data = requests.patch(url, **options, proxies=BaseAttacksMethods.proxies)
        if BaseAttacksMethods.parse_option == "json":
            print(data.json())
            return data.json()
        print(data.text)
        return data.text
    

    