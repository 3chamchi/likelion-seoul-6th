from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post

PAGE_KEYWORD = 'page'
PAGE_SIZE = 10
PAGE_DEFAILT_NUMBER = 1
ORDERING = ['-id']

def get_ordering():
    ordering = ORDERING
    return ordering

def get_queryset(model):
    queryset = model.objects.all()

    ordering = get_ordering()
    if ordering:
        if isinstance(ordering, str):
            ordering = (ordering,)
        queryset = queryset.order_by(*ordering)

    return queryset

def paginate_queryset(object_list, page, size=PAGE_SIZE):
        paginator = Paginator(object_list, size)
        pagenation = paginator.get_page(page)
        object_list = pagenation.object_list
        return pagenation, object_list


def index(request):
    post_list = get_queryset(Post)
    
    page = request.GET.get(PAGE_KEYWORD, PAGE_DEFAILT_NUMBER)
    pagenation, object_list = paginate_queryset(post_list, page)

    context = { 'posts': object_list, 'pagenation' : pagenation }
    return render(request, 'index.html', context)