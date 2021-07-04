from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html', {'name':'Hi there this is Abdul Zoha'})