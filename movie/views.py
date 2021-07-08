import requests
from rest_framework import viewsets
from .models import Movie, Director, Actor
from .serializers import MovieSerializer
from django.db.models import Q

# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    
    serializer_class = MovieSerializer 

    def get_queryset(self): 

        queryset = Movie.objects.all()
        title = self.request.query_params.get('title')

        if title:
            queryset = handle_title(title)

        return queryset


def handle_title(title):
    queryset = Movie.objects.filter(Q(title__icontains=title) | Q(title_original__icontains=title))
    check = queryset.filter(Q(title=title) | Q(title_original=title))
    if not check.exists(): 
        return fetch_and_save(title)

def fetch_and_save(title): 

    url = 'https://openapi.naver.com/v1/search/movie.json?display=100&query={}'.format(title)
    headers = {
        "X-Naver-Client-id" : "1JDddDdv4ttRSpRRKt2i",
        'X-Naver-Client-Secret': 'aDqrH1vNO_'
    }
    start = 1

    res = requests.get(url+'&start={}'.format(start), headers=headers).json() 

    if 'items' not in res:
        return Movie.objects.all().filter(Q(title__icontains=title) | Q(title_original__icontains=title))

    movies = []
    movies.append(res['items'])
    total = res['total'] 
    while total > start + 100:
        start += 100
        res = requests.get(url+'&start={}'.format(start), headers=headers).json() 
        movies.append(res['items'])
        
        
    for m in movies:
        t = m['title'].replace('<b>','') 
        t = t.replace('</b>','')
        image = m['image']
        title_original = m['subtitle']
        year = m['pubDate']

        if not year:
           continue


        if not image:
           continue

        rating = float(m['userRating']) 

        if rating in (10.0, 0.0):
           continue

        directors = list(map(str,str(m['director'])[:-1].split('|')))
        directors = list(filter(lambda x: len(x)>0, directors))
        actors = list(map(str,str(m['actor'])[:-1].split('|')))
        actors = list(filter(lambda x: len(x)>0,actors)) 

        if Movie.objects.filter(title=t,year=year, rating=rating).exists():
            continue 

        for d in directors: 
            new_director = Director.objects.filter(name=d)
            if not new_director.exists():
                new_director = Director(name=d)
                new_director.save()
        for a in actors: 
            new_actor = Actor.objects.filter(name=a)
            if not new_actor.exists():
                new_actor = Actor(name=a)
                new_actor.save()
        new_movie = Movie(title=t,
                         title_original=title_original,
                         year=year,
                         rating=rating,
                          image=image
                         )
        new_movie.save()
        print('movie {} was added'.format(t))
        for d in directors:
            director = Director.objects.get(name=d)
            new_movie.directors.add(director)
        for a in actors:
            actor = Actor.objects.get(name=a)
            new_movie.actors.add(actor) 

    return Movie.objects.all().filter(Q(title__icontains=title) | Q(title_original__icontains=title)) 







