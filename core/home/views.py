from django.shortcuts import render
# from django.http import HttpResponse
from django.views import View
import random 

def index(request):
    lucky_number = random.randint(1 , 999)
    Vegetables = ["Potato🥔","Tomato🍅","Chili🌶️","Onion🧅","Carrot🥕"]
    Person_age=19
    cities= [
        {"name":"Mumbai","population":"19,000,000","country":"India"},
        {"name":"New York","population":"20,000,000","country":"USA"},
        {"name":"Calcutta","population":"15,000,000","country":"India"},
        {"name":"Chicago","population":"7,000,000","country":"USA"},
        {"name":"Tokyo","population":"33,000,000","country":"Japan"},
    ]
    context = {"cities":cities , "lucky_number" : lucky_number , "Vegetables" : Vegetables , "Person_age" : Person_age  }

    
    return render(request, "home/index.html")

def contact(request):
    return render(request, "home/contact.html")

def about(request):
    return render(request, "home/about.html")

# def dynamic_url(request):
#     print(f"This is the value that we got in the func-->{id}")
#     return render(request, 'home/dynamic_url', context ={"id": id , "name": name})

def project(request):
    lucky_number=random.randin(100,999)
    context2= {"lucky_number":lucky_number}
    return render(request, "home/project.html",context2)



# Create your views here.
# def index(request):
#     return render(request, "home/index.html")

# def about(request):
#     return HttpResponse("Hi.. From Django Server | This is an <b>About Page</b> <br> <p> This page can be used to see the about section </p> ")

# def contact(request):
#     return HttpResponse("Hi.. From Django Server | This is a <b>Contact Page</b> <br> <p> This page can be used to see the Contact section </p>")


# class HomeView(View):
#     template_name="index.html"
#     def get(self, request):
#         return render(request, self.template_name)
#     def post(self, request):
#         return render(request, self.template_name)
