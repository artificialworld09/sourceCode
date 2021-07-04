"""
urls.py
    urlpatterns = [
    path('', views.homepage),
]

views.py
    from django.shortcuts import render
    def homepage(request):
        # return render(request, 'index.html')

        return render(request, 'index.html', {'name':'Hi there this is Abdul Zoha'})

settings.py
    'DIRS': ['templates'],

index.html
    <br>
    {{name}}
"""