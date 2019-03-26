from django.shortcuts import render, redirect 
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Image
import datetime as dt
from .forms import NewImageForm, PicturesLetterForm, ProfileForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required




@login_required(login_url='/accounts/login/')
def pictures_of_day(request):
    date = dt.date.today()
    pictures = Image.objects.all()
    return render(request, 'all-pictures/today-pictures.html', {'pictures':pictures})


# def past_days_pictures(request, past_date):
#     try:
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()
#         assert False

#     if date == dt.date.today():
#         return redirect(pictures_today)

#     pictures = Image.days_pictures(date)
#     return render(request, 'all-pictures/past-pictures.html',{"date": date,"pictures":pictures})

@login_required(login_url='/accounts/login/')
def pictures_today(request):
    if request.method == 'POST':
        form = PicturesLetterForm(request.POST)
        if form.is_valid():
            print('valid')
        form = PicturesLetterForm(request.POST)
    else:
        form = NewsLetterForm()

        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = PicturesRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('pictures_today')
        else:
            form = PicturesForm()
    return render(request, 'all-pictures/today-pictures.html', {"pictures":pictures,"PicturesForm":form})

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-pictures/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pictures/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile=current_user
            image.save()
        return redirect('picturesToday')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user=current_user
            profile.save()
        return redirect('picturesToday')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def view_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user=current_user
            profile.save()
        return redirect('view-profile')

    else:
        form = ProfileForm()
    return render(request, 'view-profile.html')