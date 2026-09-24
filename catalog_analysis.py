import math

movies = [
    {"title": "The Dune Chronicles",
    "year": 2021,
    "genres": {"sci-fi", "drama"},
    "rating": 8.6,
    "duration_min": 155,
    "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
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
    total = 0
    for movie in movies:
        total += movie["rating"]
    return round(total / len(movies), 1)

def catalog_age_stats(movies, current_year = 2026):
    ages = []
    
    for movie in movies:
        age = current_year - movie["year"]
        ages.append(age)
        
    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))
    
    return oldest, newest, average

def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"

def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"

def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"

print(average_rating(movies)) 
print(catalog_age_stats(movies))
print(duration_in_hours(movies[0]["duration_min"]))
print(rating_tier(9.2))
print(rating_tier(4.8))
print(decade_label(2021))
print(decade_label(2020))
print(decade_label(2015))
print(decade_label(2014))

for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    print(movie["title"])
    
index = 0
while index < len(movies):
    movie = movies[index]
    if movie["rating"] > 9.0:
        print(movie["title"])
        break
    index += 1
else:
    print("Шедевров не найдено")
    
def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count

print(count_long_movies(movies))

def normalize_title(title):
    words = []
    
    for word in title.lower().split():
        normalized_word = word[0].upper() + word[1:]
        words.append(normalized_word)
    
    return " ".join(words)
    
print(normalize_title(movies[2]["title"]))

def make_slug(title):
    return title.lower().replace(" ", "-")

print(make_slug(normalize_title(movies[7]["title"])))

def format_report_line(movie):
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )

print(format_report_line(movies[7]))

def titles_sorted_by_rating(movies):
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True,
    )
    titles = []
    for movie in sorted_movies:
        titles.append(movie["title"])
    return titles

print(titles_sorted_by_rating(movies)[:3])



def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True,
    )

    top_movies = sorted_movies[:n]
    result = []

    for movie in top_movies:
        result.append((movie["title"], movie["rating"]))

    return result

print(top_n_by_rating(movies))