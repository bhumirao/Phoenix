from django.shortcuts import render,HttpResponse
from . import urls


from pymongo import MongoClient
client=MongoClient('mongodb+srv://User:hello7648@cluster0.awzcbhw.mongodb.net/test')
#client =MongoClient("localhost", 27017)
#Define Database
db = client['phoenix']
#Define Collection
collection = db['project']

# Create your views here.
'''
def landing(request):
    return render(request,'index.html')
    '''

def landing(request):
    return render(request,'landing.html')

