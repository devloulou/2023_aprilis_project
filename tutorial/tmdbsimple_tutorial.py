import tmdbsimple as tmdb
from tmdbsimple import Movies, Changes

tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'

search = tmdb.Search()

response = search.movie(query='Prey')['results'][0]

from urllib.request import urlopen
web_url = "https://image.tmdb.org/t/p/original"
image_path = web_url + response['poster_path']

image = urlopen(image_path).read()

# print(image[0:100])
with open('test.jpg', "wb") as poster:
    poster.write(image)



# sol = tmdb.Movies(id=response['id'])
# for item in sol.reviews()['results']:
#     print(item)

# for item in sol.credits()['cast']:
#     print(item)
# print(response)

#/ujr5pztc1oitbe7ViMUOilFaJ7s.jpg

#https://image.tmdb.org/t/p/original/ujr5pztc1oitbe7ViMUOilFaJ7s.jpg
#https://image.tmdb.org/t/p/original/hYZhHMhQjITs9mziAH8gHsUA8Eb.jpg