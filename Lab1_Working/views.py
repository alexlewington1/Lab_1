from django.shortcuts import render

# index page render
def index(response):
    return render(response, 'index.html')

# contact page render
def contact(response):
    return render(response, 'contact.html')

# books page render
def books(response):
    return render(response, 'books.html')
