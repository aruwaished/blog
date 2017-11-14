from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def random(request):
    return render(request, 'random.html')

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Awesome, you just added a blog post!")
        return redirect("more:list")
    context = {
        "form": form
    }
    return render(request, 'post_create.html', context)

def post_update(request, post_slug):
    item = Post.objects.get(slug=post_slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        messages.info(request, "Hey, you just changed a blog post!")
        return redirect("more:detail", post_slug=item.slug)
    context = {
        "form": form,
        "item":item,
    }
    return render(request, 'post_update.html', context)

def post_delete(request, post_slug):
    Post.objects.get(slug=post_slug).delete()
    messages.warning(request, "Noooooooooo!")
    return redirect("more:list")

def some_function(request):
    some_dictionary = {
        "some_key": "with a random value",
    }
    return render(request, "something.html", some_dictionary)


def post_list(request):
    objects = Post.objects.all()
    # objects = Post.objects.all().order_by('title', 'id')
    paginator = Paginator(objects, 5)

    number = request.GET.get('page')

    try:
        objects = paginator.page(number)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    context = {
        "post_items": objects,
    }
    return render(request, "list.html", context)

def post_detail(request, post_slug):
    item = get_object_or_404(Post, slug=post_slug)
    context = {
        "item": item,
    }
    return render(request, "detail.html", context)

