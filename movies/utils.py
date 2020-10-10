from datetime import datetime


def generate_genre_id():
    now = datetime.now()
    id = now.strftime('%Y%m%d%H%M%S')
    return 'g' + id


def generate_movie_id():
    now = datetime.now()
    id = now.strftime('%Y%m%d%H%M%S')
    return 'm' + id
