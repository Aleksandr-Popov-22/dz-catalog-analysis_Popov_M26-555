import math

def main():
  print('its main')

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
  sum_rating = 0
  for item in movies:
    sum_rating += item['rating']
  return round(sum_rating/len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
  year = []
  year_sum = 0
  for item in movies:
    year.append(item['year'])
    year_sum += item['year']
  year.sort()
  aver_year = current_year - year_sum/len(year)
  return (current_year - year[0], current_year - year[-1], math.ceil(aver_year))

def duration_in_hours(minutes):
  hours = minutes // 60
  min = minutes % 60
  return f"{hours}ч {min}м"

def rating_tier(rating):
    if rating >= 9:
        return 'шедевр'
    elif rating >= 7:
        return 'хорошо'
    else:
        return 'средне' if rating >= 5 else 'слабо'

def decade_label(year):
  match year:
    case _ if year > 2020 :
      return 'новые'
    case _ if year <= 2020 and year >= 2015:
      return 'недавние'
    case _ if year < 2015 :
      return 'старые'

def print_non_comedy_titles(movies):
  for item in movies:
    if 'comedy' in item['genres']:
      continue
    print(normalize_title(item['title']))   

def find_first_masterpiece(movies):
  item = 0
  while item < len(movies):
    if movies[item]['rating'] > 9.0 :
      print(movies[item]['title'])
      break
    item += 1
  else:
    print('Шедевров не найдено')

def count_long_movies(movies, threshold=120):
  sum = 0
  for mov in movies:
    if mov['duration_min'] > threshold:
      sum += 1
  print(f'Фильмов, длиннее {threshold} минут {sum}')

def normalize_title(title):
  str = ''
  words = title.split()
  for word in words:
    str += word[0].upper() + word[1:].lower() + ' '
  return str.strip()

def make_slug(title):
  str = ''
  words = title.split()
  for word in words:
    str += word.lower() + ' '
  return str.strip().replace(' ', '-')

def format_report_line(movie):
  return f'"{normalize_title(movie['title'])}" ({movie['year']}) - {movie['rating']}/10, {duration_in_hours(movie['duration_min'])}, жанры: {', '.join(sorted(movie['genres']))}'

def titles_sorted_by_rating(movies):
  sort_list = sorted(movies, key=lambda movie:movie['rating'], reverse=True)
  return [normalize_title(mov['title']) for mov in sort_list]

def top_n_by_rating(movies, n=3):
  list_tuple = []
  sort_list = sorted(movies, key=lambda movie:movie['rating'], reverse=True)
  for i in range(min(n, len(movies))):
    list_tuple.append((normalize_title(sort_list[i]['title']), sort_list[i]['rating']))
  return list_tuple

def count_by_genre(movies):
  dict_genres = {}
  for mov in movies:
    for gen in mov['genres']:
      dict_genres[gen] = dict_genres.get(gen, 0) + 1
  return dict_genres


def actor_filmography(movies):
  dict_actors = {}

  for mov in movies:
    for actor in mov['actors']:
      if actor not in dict_actors:
        dict_actors[actor] = []
      dict_actors[actor].append(normalize_title(mov['title']))
  return dict_actors

def good_film(movies):
  return {normalize_title(mov['title']): mov['rating'] for mov in movies if mov['rating'] > average_rating(movies)}

def all_genres(movies):
  all_gen = set()
  for mov in movies:
    all_gen.update(mov['genres'])
  return all_gen

def common_actors(movie1, movie2):
  return set(movie1['actors']) & set(movie2['actors'])


def genres_only_in_one(movies_a, movies_b):
    a = set()
    b = set()
    for mov in movies_a:
        a.update(mov['genres'])
    for mov in movies_b:
        b.update(mov['genres'])
    return a - b

def iter_high_rated(movies, min_rating=8.0):
  for mov in movies:
    if mov['rating'] >= min_rating:
      yield mov

for movie in iter_high_rated(movies):
    print(format_report_line(movie))


sum(m["duration_min"] for m in movies if m["rating"] > 7)

if __name__ == "__main__":
    main()
