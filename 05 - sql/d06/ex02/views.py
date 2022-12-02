from django.http import HttpResponse
import psycopg2
from django.conf import settings
from django.shortcuts import render
from . import movies as m


def connect_to_db():
    try:
        connection = psycopg2.connect(
            database=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
    except Exception as err:
        return err
    return connection


def init(request):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute("""
        create table if not exists ex02_movies  (
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


def populate(request):
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        insert_cmd = '''
            insert into ex02_movies 
            (episode_nb, title, director, producer, release_date) 
            values 
            (%s, %s, %s, %s, %s);
        '''
        res = []
        for i in m.movies:
            try:
                cursor.execute(
                    insert_cmd, [
                        i['episode_nb'],
                        i['title'],
                        i['director'],
                        i['producer'],
                        i['release_date']
                    ])
                connection.commit()
                res.append('ok')
            except Exception as err:
                res.append(err)
                return HttpResponse(str(i) + "<br>" for i in res)
    except Exception as err:
        return HttpResponse(err)
    return HttpResponse(str(i) + "<br>" for i in res)


def display(request):
    try:
        connect = connect_to_db()
        cursor = connect.cursor()

        cursor.execute('select * from ex02_movies;')
        movies = cursor.fetchall()
        return render(request, 'ex02/index.html', {'movies': movies})
    except:
        return HttpResponse('No data available')
