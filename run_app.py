from core.export import *


if __name__ == '__main__':
    url="http://127.0.0.1:8000/pbkdf2_sha256390000jwfsotswr778gvfsh7wj7fnjacn7hmzwxfbd9cjxpabqqinw0ug2gvi494rrg8m/detail-lessons/1/list-detaillesson-of-lesson/"
    Dos.number_request = 32
    Dos.dos(url=url)