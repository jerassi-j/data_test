from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import item, rating

def index(request):
    items = item.objects.all()
    context = {'item_list': items}
    return render(request, 'rec/i_list.html', context)

def item_detail(request, itemid):
    data = get_object_or_404(item, pk=itemid)
    data_detail = {'item':data}
    return render(request, 'rec/i_detail.html', data_detail)

def rating_list(request):
    ratings = rating.objects.all()
    context = {'rating_list': ratings}
    return render(request, 'rec/r_list.html', context)

def rating_detail(request, r_id):
    data = get_object_or_404(rating, pk=r_id)
    data_detail = {'rating':data}
    return render(request, 'rec/r_detail.html', data_detail)

import math
def cal_average(u_list):
    return math.avg(u_list)

def rec_cf_test(request):
    # sql = "select userid from rating"
    # cursor = connection.cursor()
    return render(request, 'rec/rec_test_page.html')

import csv
def data_insert(request):

    # with open('/Users/jerassi/Desktop/ml-latest-small/movies.csv', newline='') as data:
    #     data_reader = csv.DictReader(data)
    #     for row in data_reader:
    #         item.objects.create(
    #             itemid=row['movieId'],
    #             title=row['title'],
    #             genres=row['genres'],
    #         )
    #
    # with open('/Users/jerassi/Desktop/ml-latest-small/ratings.csv', newline='') as data:
    #     data_reader = csv.DictReader(data)
    #     for row in data_reader:
    #         rating.objects.create(
    #             r_id=row['r_id'],
    #             userid=row['userId'],
    #             itemid=row['movieId'],
    #             rating=row['rating'],
    #             timestamp=row['timestamp'],
    #         )
    return render(request, 'rec/data_insert.html')
