from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect

from webapp.models import Good, Category

from webapp.form import GoodForm


def good_list_view(request):
    goods = Good.objects.order_by("-created_at")
    form = GoodForm()
    context = {"goods": goods, "form": form}
    return render(request, "index.html", context)


def good_update(request, pk):
    good = get_object_or_404(Good, id=pk)
    if request.method == "GET":
        form = GoodForm(initial={"title": good.title,
                                 "category": good.category,
                                 "description": good.description,
                                 "price": good.price,
                                 "remainder": good.remainder,
                                 "image_url": good.image_url,
                                 })
        return render(request, "good_update.html", {"form": form})
    else:
        form = GoodForm(data=request.POST)
        if form.is_valid():
            good.title = request.POST.get("title")
            good.category = request.POST.get("category")
            good.description = request.POST.get("description")
            good.price = request.POST.get("price")
            good.remainder = request.POST.get("remainder")
            good.image_url = request.POST.get("image_url")
            good.save()
            return redirect("good")
        else:
            return render(request, "good_update.html", {"form": form})


def good_create_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        form = GoodForm()
        return render(request, "create_good.html", {"categories": categories, "form": form})
    else:
        form = GoodForm(data=request.POST)
        if form.is_valid():
            good = Good.objects.create(title=form.cleaned_data.get('title'),
                                       category=form.cleaned_data.get('category'),
                                       description=form.cleaned_data.get('description'),
                                       price=form.cleaned_data.get('price'),
                                       remainder=form.cleaned_data.get('remainder'),
                                       image_url=form.cleaned_data.get('image_url'),
                                       )
            return redirect("index")
        else:
            return render(request, "create_good.html", {"form": form})


def good_view(request, *args, pk, **kwargs):
    good = get_object_or_404(Good, id=pk)
    return render(request, "good.html", {"good": good})


def category_view(request):
    categories = Category.objects.order_by("-title")
    context = {"categories": categories}
    return render(request, "category_view.html", context)


def delete_good(request, pk):
    good = get_object_or_404(Good, id=pk)
    if request.method == "GET":
        return render(request, "delete_good.html", {"good": good})
    else:
        good.delete()
        return redirect("index")


def category_add_view(request):
    if request.method == "GET":
        return render(request, "category_add.html")
    if request.method == 'POST':
        Category.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
        )
        return HttpResponseRedirect("/")
