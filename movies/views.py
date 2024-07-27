import csv
from django.shortcuts import render
from django.conf import settings
import os

def display(request):
    csv_file_path = os.path.join(settings.BASE_DIR, 'movies', 'imdb.csv')
    data = []
    ratings = []

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  
        rating_index = header.index('IMDB_Rating')  

        for row in reader:
            data.append(row)
            
            try:
                ratings.append(float(row[rating_index]))
            except ValueError:
                pass  
    total_movies = len(data)
    if ratings:
        average_rating = sum(ratings) / len(ratings)
        min_rating = min(ratings)
        max_rating = max(ratings)
    else:
        average_rating = min_rating = max_rating = None

    context = {
        'header': header,
        'data': data,
        'total_movies': total_movies,
        'average_rating': average_rating,
        'min_rating': min_rating,
        'max_rating': max_rating,
    }

    return render(request, 'display.html', context)
