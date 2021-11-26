from django.shortcuts import render


def header(request, title, *args, **kwargs):
    context = {
        'title': title,
    }
    return render(request, 'shared/_headerReferences.html', context)



def home_page(request):
    return render(request, 'home_page.html')
