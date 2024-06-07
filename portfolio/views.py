from django.shortcuts import render,redirect ,get_object_or_404
from .models import Person 
from .forms import PersonForm

# Create your views here.
def home_view(request): 
    return render(request, "index.html")

def portfolio_view(request): 
    portfolio = Person.objects.all() 
    return render(request, "portfolio.html", {"portfolio":portfolio})

def portfolio_detail_view(request, id): 
    portfolio = get_object_or_404(Person, id=id)
    return render(request, "portfolio_detail.html", {"portfolio":portfolio})

def addportfolio_view(request):    
    form = PersonForm(request.POST or None)
    
    if form.is_valid():
        portfolio = form.save(commit=False)
        portfolio.author = request.user
        portfolio.save()
        form.save()
         
        return redirect("portfolio")
    context = {"form":form}
    
    return render(request, "addportfolio.html", context)

def portfolio_update_view(request, id):
    portfolio = get_object_or_404(Person, id=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=portfolio) 
    if form.is_valid(): 
        portfolio.save() 
        return redirect("portfolio")
    context = {"form":form}
    return render(request, "addportfolio.html", context)

def portfolio__delete__view(request, id):
    portfolio = get_object_or_404(Person, id=id)
    portfolio.delete() 
    return redirect("portfolio")