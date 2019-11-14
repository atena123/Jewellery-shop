from django.shortcuts import render

# Create your views here.
def contact(request):
    "A view that dispalays the contact page"
    return render(request, "contact.html")
