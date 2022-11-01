
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt


from home.models import postEnquiry

from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://User:hello7648@cluster0.awzcbhw.mongodb.net/test')

# Define Database

db = client['phoenix']


# Define Collection
collection = db['project']

# Create your views here.


def landing(request):
    return render(request, 'landing.html')


def calendar(request):
    return render(request, 'calendar.html')


def login(request):
    return render(request, 'login.html')

def forum(request):
    return render(request, 'form.html')

def thank(request):
    return render(request, 'thank.html')




def savePost(request):
    if request.method=="POST":
        title=request.POST.get('title')
        type=request.POST.get('type')
        date=request.POST.get('date')
        descr=request.POST.get('description')
        en=postEnquiry(title=title,type=type,date=date,description=descr)
        en.save()

        return render(request, '<h1 align=center>Thanks a bunch for filling that out. It means a lot to us,<br> just like you do! We really appreciate you giving us a moment of your time today. Thanks for being you :)</p>')



# Create your views here.
def home_view(request):

    # cheking the request
    if request.method == 'POST':

        # passing the form data to LoginForm
        user_details = UserForm(request.POST)

        # validating the user_details with is_valid() method
        if user_details.is_valid():

            # writing data to the database
            user_details.save()

            # redirect to another page with success message
            return HttpResponse("Data submitted successfully")

        else:

            # redirect back to the user page with errors
            return render(request, 'validation/home.html', {'form': user_details})

        
