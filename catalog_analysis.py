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


def demonstrate_cycles(movies):
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

def normalize_title(title):
    words = []
    
    for word in title.lower().split():
        normalized_word = word[0].upper() + word[1:]
        words.append(normalized_word)
    
    return " ".join(words)

def make_slug(title):
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )

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

def count_by_genre(movies):
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts

def actor_filmography(movies):
    filmography = {}

    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []

            filmography[actor].append(movie["title"])

    return filmography

average = average_rating(movies)
above_average = {
    movie["title"]: movie["rating"]
    for movie in movies
    if movie["rating"] > average
}

def all_genres(movies):
    genres = set()

    for movie in movies:
        genres.update(movie["genres"])

    return genres

def common_actors(movie1, movie2):
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])

    return actors1 & actors2

def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)

    return genres_a - genres_b

def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

def demonstrate_generator(movies):
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))
    
total_duration = sum(
    movie["duration_min"]
    for movie in movies
    if movie["rating"] > 7
)

def build_report(movies):
    print("ОТЧЁТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")

    ages = catalog_age_stats(movies)
    print(f"Средний возраст фильмов: {ages[2]} лет")

    print("\nТоп-3 фильма:")

    top_movies = sorted(
        movies,
        key=lambda movie: movie["rating"],
        reverse=True,
    )[:3]
    
    for movie in top_movies:
        print(f"{format_report_line(movie)}")

    print("\nФильмов по жанрам:")

    genre_counts = count_by_genre(movies)
    sorted_genres = sorted(
        genre_counts.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    for genre, count in sorted_genres:
        print(f"{genre} — {count}")

    print("\nВсе жанры каталога:", ", ".join(sorted(all_genres(movies))))

build_report(movies)