from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect

from webapp.models import Good, Category


def good_list_view(request):
    goods = Good.objects.order_by("-created_at")
    context = {"goods": goods}
    return render(request, "index.html", context)


def good_create_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "create_good.html", {"categories": categories})
    else:
        category = get_object_or_404(Category, pk=request.POST.get("category"))
        good = Good.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            category=category,
            price=request.POST.get("price"),
            created_at=request.POST.get("created_at"),
            image_url=request.POST.get("image_url"),
        )

    return redirect("good_view", pk=good.pk)


def good_view(request, *args, pk, **kwargs):
    good = get_object_or_404(Good, id=pk)
    return render(request, "good.html", {"good": good})


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
