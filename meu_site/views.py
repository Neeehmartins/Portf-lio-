from django.shortcuts import render

# Create your views here.
def home(request):
    conhecimentos = ['HTML', 'CSS', 'JavaScript', 'Python', 'Django',
    'Git', 'Cantar', 'Jogar tênis']

    return render(request,'index.html',
    {'conhecimentos':conhecimentos})
