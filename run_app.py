from core.export import *


if __name__ == '__main__':
    #* DDos: http://127.0.0.1:8000/pbkdf2_sha256390000jwfsotswr778gvfsh7wj7fnjacn7hmzwxfbd9cjxpabqqinw0ug2gvi494rrg8m/detail-lessons/1/list-detaillesson-of-lesson/


    url="http://127.0.0.1:8000/pbkdf2_sha256390000jwfsotswr778gvfsh7wj7fnjacn7hmzwxfbd9cjxpabqqinw0ug2gvi494rrg8m/detail-lessons/1/list-detaillesson-of-lesson/"
    DDos.number_request = 52
    DDos.DDos_basic(url=url)