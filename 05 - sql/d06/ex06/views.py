from django.http import HttpResponse
import psycopg2
from django.conf import settings
from django.shortcuts import render, redirect
from . import movies as m
from . import form
from django.views import View


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
        cursor.execute('''
        create table if not exists ex06_movies  (
            title varchar(64) not null unique, 
            episode_nb int primary key,
            opening_crawl text,
            director varchar(32) not null,
            producer varchar(128) not null,
            release_date date not null,
            created timestamp not null default now(),
            updated timestamp not null default now()
        );
        
        CREATE OR REPLACE FUNCTION update_change timestamp_column()
        RETURNS TRIGGER AS $$
        BEGIN
        NEW.updated = now();
        NEW.created = OLD.created;
        RETURN NEW;
        END;
        $$ language 'plpgsql';
        CREATE TRIGGER update_films_change timestamp BEFORE UPDATE
        ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
        update_change timestamp_column();
        ''')
        cursor.execute('commit')
    except Exception as err:
        return HttpResponse(err)
    return HttpResponse('<h1>ok</h1>')


def populate(request):
    res = []
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        insert_cmd = f'''
            insert into ex06_movies 
            (episode_nb, title, director, producer, release_date) 
            values 
            (%s, %s, %s, %s, %s) on conflict do nothing;
        '''

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
                return HttpResponse(err)
    except Exception as err:
        return HttpResponse(err)
    return HttpResponse(i + '<br>' for i in res)


def display(request):
    try:
        connect = connect_to_db()
        cursor = connect.cursor()
        cursor.execute('select * from ex06_movies;')
        movies = cursor.fetchall()
        return render(request, 'ex06/display.html', {'movies': movies})
    except Exception as err:
        return HttpResponse('No data available')


class Update(View):
    connect = connect_to_db()
    cursor = connect.cursor()

    def get(self, request):
        try:
            self.cursor.execute('select * from ex06_movies;')
            movies = self.cursor.fetchall()
            remove_form = form.UpdateForm(choices=((i[0], i[0]) for i in movies))
            return render(request, 'ex06/update.html', {'form': remove_form})
        except Exception as err:
            return HttpResponse(err)

    def post(self, request):
        try:
            self.cursor.execute('select title from ex06_movies;')
            movies = self.cursor.fetchall()
            choices = ((i[0], i[0]) for i in movies)
            update_form = form.UpdateForm(choices, request.POST)
            if update_form.is_valid():
                try:
                    self.cursor.execute('update ex06_movies set opening_crawl = %s where title = %s',
                                        [update_form.cleaned_data['opening_crawl'], update_form.cleaned_data['title']])
                    self.connect.commit()
                except Exception as err:
                    return HttpResponse(err)
            return redirect(request.path)
        except Exception as err:
            return HttpResponse(err)
