from django.shortcuts import render, redirect
from django.core.validators import EmailValidator
from .models import *
from shop.models import Produit
from .forms import ContactForm
# Create your views here.
def index(request):
    # presentation = Presentation.objects.filter()[:2]
    slider = Sliders.objects.filter()[:1]
    velo = Trouver_le_velo.objects.filter()[:1]
    our_products = Our_products.objects.all()
    product = Category_product.objects.filter()[:1]
    feeback = Feeback.objects.all()
    top = Our_products.objects.all()
    news = News.objects.all()
    pub = Pub.objects.all()
    produit = Produit.objects.get(id=1)
    print(slider)
    datas = {
        # 'presentation':presentation,
        'velo':velo,
        'product':product,
        'news':news,
        'pub':pub,
        'top':top,
        'our_products':our_products,
        'feeback':feeback,
        'produit':produit,
        'slider':slider
        
    }
    
    return render(request, 'website/index.html', datas)

def about(request):
    
    presentation = Presentation.objects.filter(status=True)[:2]
    team = Team.objects.filter(status=True)[:4]
    social = SocialAccount.objects.filter(status=True)[:4]

    data = {
        'presentation' : presentation,
        'team' : team,
        'social' : social,
    }
    
    return render(request, 'website/about.html', data)

def contact(request):

    presentation = Presentation.objects.filter(status=True).last
    social = SocialAccount.objects.filter(status=True)[:4]
    print(presentation)
    contact_form = ContactForm(request.POST or None)
    
    if request.method == 'POST':
        if contact_form.is_valid():
            contact_form.save()
            contact_form = ContactForm()

    data = {
        'presentation' : presentation,
        'social' : social,
        'contact_form': contact_form
    }
    
    return render(request, 'website/contacts.html', data) 

def news_letter(request):
    if request.method == 'POST':
        newsletter = request.POST.get('newsletter')
        if newsletter:
            nl = NewsLetter.objects.create(email=newsletter)
            nl.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))   




