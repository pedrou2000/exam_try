from django.shortcuts import render
from .models import Usuario, Tweet, Retweet

# Create your views here.

def usuarios_1002(request):
    user_1002 = list(Usuario.objects.filter(id = 1002))[0]
    twetts_user_1002 = list(Tweet.objects.filter(usuario = user_1002))
    retweets = []
    for tweett in twetts_user_1002:
        retweets += list(Retweet.objects.filter(tweet = tweett))

    context = {}
    context['retweets'] = retweets
    context['error'] = 0
    if len(retweets) == 0:
        context['error'] = 1
    
    return render(request, 'usuario.html', context=context)
    

