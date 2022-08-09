from django.shortcuts import render


def index(request):
    return render(request, 'paginas/home.html')


def sobre(request):
    return render(request, 'paginas/traj_pessoal.html')


def profissional(request):
    return render(request, 'paginas/traj_profissional.html')
