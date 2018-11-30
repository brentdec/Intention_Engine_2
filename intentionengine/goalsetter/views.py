from django.shortcuts import render

# Create your views here.
#from goalsetter.models import Goals
from goalsetter.models import Inspiration

# def index(request):
#     latest_goal_list = Goals.objects.order_by('-start_date')[:5]
#     context = {'latest_goal_list': latest_goal_list}
#     return render(request, 'goalsetter/index2.html', context)

def index(request):
    inspiration_text = Inspiration.objects.filter(inspire_id__exact=100)
    return render(request, 'goalsetter/index.html', {'inspiration_text':inspiration_text})