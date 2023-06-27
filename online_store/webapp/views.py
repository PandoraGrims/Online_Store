from django.shortcuts import render, redirect, get_object_or_404

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
        category = request.POST.get("category")
        print(type(category))
        good = Good.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            category=request.POST.get("category"),
            price=request.POST.get("price"),
            created_at=request.POST.get("created_at"),
            image_url=request.POST.get("image_url"),
        )

    return render(request, "index.html")


def good_view(request, *args, pk, **kwargs):
    good = get_object_or_404(Good, id=pk)
    return render(request, "good.html", {"good": good})


def delete_good(request):
    good_id = request.GET.get("id")
    good = get_object_or_404(Good, id=good_id)
    good.delete()
    return redirect('good_list')
