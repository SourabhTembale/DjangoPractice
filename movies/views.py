import csv
from django.shortcuts import render
from django.conf import settings
import os

def display(request):
    csv_file_path = os.path.join(settings.BASE_DIR, 'movies', 'imdb.csv')
    data = []
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  
        for row in reader:
            data.append(row)
    
    context = {
        'header': header,
        'data': data,
    }
    return render(request, 'display.html', context)
