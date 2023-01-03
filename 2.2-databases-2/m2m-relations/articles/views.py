from django.shortcuts import render

from articles.models import Article, Scope, Tag


def articles_list(request):

    ordering = '-published_at'

    object_list = Article.objects.all().order_by(ordering)
    
    template = 'articles/news.html'
    context = {
        'object_list':object_list
    }
    return render(request, template, context)
