from django.http import HttpResponse
import psycopg2
from django.conf import settings
from django.shortcuts import render


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
        create table ex08_planets(
            id serial primary key,
            name varchar(64) unique not null,
            climate varchar,
            diameter int,
            orbital_period int,
            population bigint,
            rotation_period int,
            surface_water real,
            terrain varchar(128)
            );
        
        create table ex08_people(
            id serial primary key,
            name varchar(64) unique not null,
            birth_year varchar(32),
            gender varchar(32),
            eye_color varchar(32),
            hair_color varchar(32),
            height int,
            mass real,
            homeworld varchar(64) references ex08_planets(name)
            );
        ''')
        cursor.execute('commit')
    except Exception as err:
        return HttpResponse(err)
    return HttpResponse('<h1>ok</h1>')


def parsing_planet(line: str):
    line = line.split('	')
    planet = {
        'name': line[0].strip() if line[0].strip() != 'NULL' else None,
        'climate': line[1].strip() if line[1].strip() != 'NULL' else None,
        'diameter': line[2].strip() if line[2].strip() != 'NULL' else None,
        'orbital_period': line[3].strip() if line[3].strip() != 'NULL' else None,
        'population': line[4].strip() if line[4].strip() != 'NULL' else None,
        'rotation_period': line[5].strip() if line[5].strip() != 'NULL' else None,
        'surface_water': line[6].strip() if line[6].strip() != 'NULL' else None,
        'terrain': line[7].strip() if line[7].strip() != 'NULL' else None,
    }
    return planet


def parsing_people(line: str):
    line = line.split('	')
    people = {
        'name': line[0].strip() if line[0].strip() != 'NULL' else None,
        'birth_year': line[1].strip() if line[1].strip() != 'NULL' else None,
        'gender': line[2].strip() if line[2].strip() != 'NULL' else None,
        'eye_color': line[3].strip() if line[3].strip() != 'NULL' else None,
        'hair_color': line[4].strip() if line[4].strip() != 'NULL' else None,
        'height': line[5].strip() if line[5].strip() != 'NULL' else None,
        'mass': line[6].strip() if line[6].strip() != 'NULL' else None,
        'homeworld': line[7].strip() if line[7].strip() != 'NULL' else None,
    }
    return people


def populate(request):
    res = []
    try:
        connection = connect_to_db()
        cursor = connection.cursor()
        try:
            with open('ex08/planets.csv') as f:
                planets = [parsing_planet(line) for line in f.readlines()]
            with open('ex08/people.csv') as f:
                people = [parsing_people(line) for line in f.readlines()]
        except Exception as e:
            return HttpResponse(e)

        insert_cmd_planet = """
            insert into ex08_planets
            (name, climate, diameter, orbital_period, population, rotation_period, surface_water,terrain)
            values
            (%s, %s, %s, %s, %s, %s, %s, %s);
            """
        insert_cmd_people = """
            insert into ex08_people
            (name, birth_year, gender, eye_color, hair_color, height, mass, homeworld)
            values
            (%s, %s, %s, %s, %s, %s, %s, %s);
            """

        for i in planets:
            try:
                cursor.execute(
                    insert_cmd_planet, [
                        i['name'],
                        i['climate'],
                        i['diameter'],
                        i['orbital_period'],
                        i['population'],
                        i['rotation_period'],
                        i['surface_water'],
                        i['terrain'],
                    ])
                connection.commit()
                res.append('ok')
            except Exception as err:
                return HttpResponse(err)

        for i in people:
            try:
                cursor.execute(
                    insert_cmd_people, [
                        i['name'],
                        i['birth_year'],
                        i['gender'],
                        i['eye_color'],
                        i['hair_color'],
                        i['height'],
                        i['mass'],
                        i['homeworld'],
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
        cursor.execute("""
            SELECT
                ex08_people.name,
                ex08_people.homeworld,
                ex08_planets.climate
            FROM
                ex08_planets
                RIGHT JOIN ex08_people
                ON
                    ex08_people.homeworld = ex08_planets.name
                    where
                        ex08_planets.climate
                        LIKE '%windy%'
                ORDER BY ex08_planets.name;
            """)
        info = cursor.fetchall()
        return render(request, 'ex08/display.html', {'info': info})
    except Exception as err:
        return HttpResponse('No data available')
