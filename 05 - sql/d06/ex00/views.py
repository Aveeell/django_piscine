from django.http import HttpResponse
import psycopg2
from django.conf import settings

def init(request):
    try:
        connection = psycopg2.connect(
            database=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cursor = connection.cursor()
        cursor.execute("""
        create table if not exists ex00_movies  (
        title varchar(64) not null unique, 
        episode_nb int primary key,
        opening_crawl text,
        director varchar(32) not null,
        producer varchar(128) not null,
        release_date date not null
        );
        """)
        cursor.execute('commit')
    except Exception as err:
        return HttpResponse(err)
    return HttpResponse('<h1>ok</h1>')
