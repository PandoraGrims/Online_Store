from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect

from webapp.models import Good, Category

from webapp.form import GoodForm, CategoryForm


def good_list_view(request):
    goods = Good.objects.order_by("-created_at")
    context = {"goods": goods}
    return render(request, "index.html", context)


# def good_create_view(request):
#     if request.method == "GET":
#         categories = Category.objects.all()
#         return render(request, "create_good.html", {"categories": categories})
#     else:
#         category = get_object_or_404(Category, pk=request.POST.get("category"))
#         good = Good.objects.create(
#             title=request.POST.get("title"),
#             description=request.POST.get("description"),
#             category=category,
#             price=request.POST.get("price"),
#             created_at=request.POST.get("created_at"),
#             image_url=request.POST.get("image_url"),
#         )
#
#     return redirect("good_view", pk=good.pk)


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


def delete_good(request, good_id):
    good = get_object_or_404(Good, pk=good_id)
    context = {"good": good}
    return render(request, "index.html", context)


def category_add_view(request):
    if request.method == "GET":
        return render(request, "category_add.html")
    if request.method == 'POST':
        Category.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
        )
        return HttpResponseRedirect("/")
