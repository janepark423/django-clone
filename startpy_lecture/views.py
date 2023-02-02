from django.shortcuts import render
from .models import myText

# Create your views here.

def home_list(request) :
    texts = myText.objects.filter(category="html")

    # texts1 = "1번 타이틀"
    # texts2 = "2번 타이틀"

    return render(request, 'startpy_lecture/home_list.html', {'texts1': texts})
