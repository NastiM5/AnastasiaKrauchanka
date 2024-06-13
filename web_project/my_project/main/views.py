from django.shortcuts import render, redirect
from .models import Price, Review, Author
import datetime
from .forms import ReviewForm
from .forms import BotForm
from django.contrib.auth.decorators import login_required
from telegram import Bot
import requests




def test(request):
    now = datetime.datetime.now()
    return render(request, 'test.html', {"my_time":now})


def price_list(request):
    prices = Price.objects.all()
    return render(request, 'price_list.html', {'prices': prices})



@login_required
def review_list(request):
    reviews = Review.objects.all()
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        
        if form.is_valid():
            post_entry = form.save(commit=False)
            post_entry.issued = datetime.datetime.now()
            post_entry.author = request.user


            form.save()
            post_entry = form.save()
            return redirect('review_list')
        
        else:
            
            form = ReviewForm(initial={'author': request.user})
        
        

    return render(request, 'reviews.html', {'reviews': reviews, 'form': form})












def send_message_to_telegram_bot(message):
    bot_token = '7193958987:AAGT32MyPYRx7fFWcZrm9NLPcm7WIPGGd-0'
    chat_id = '-1002065792111'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
    response = requests.get(url)
    return response.json()


def bot_form(request):
    if request.method == 'POST':
        form = BotForm(request.POST)
        if form.is_valid():
            form.save()
            message = '{}'.format(form.cleaned_data)
            send_message_to_telegram_bot(message)
           # url = 'https://api.telegram.org/bot<7193958987:AAGT32MyPYRx7fFWcZrm9NLPcm7WIPGGd-0>/sendMessage'
            #data = {
                #'chat_id': '<-1002065792111>',
               # 'text': f"Новые данные: {form.cleaned_data}"
           # }
           # response = requests.post(url, data=data)
            
            return redirect('success_page')
           
    else:
        form = BotForm()
    return render(request, 'test.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html')



