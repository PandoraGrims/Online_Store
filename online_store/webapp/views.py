from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Good


def good_list_view(request):
    goods = Good.objects.order_by("-data_field")
    context = {"goods": goods}
    return render(request, "index.html", context)


def good_create_view(request):
    if request.method == "GET":
        return render(request, "create_good.html")
    else:
        good = Good.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            created_at=request.POST.get("created_at"),
            category=request.POST.get("category"),
            price=request.POST.get("price"),
            image_url=request.POST.get("image_url"),
        )

    return redirect("good_view", pk=good.pk)


def good_view(request, *args, pk, **kwargs):
    good = get_object_or_404(Good, id=pk)
    return render(request, "good.html", {"good": good})


def delete_good(request):
    good_id = request.GET.get("id")
    good = get_object_or_404(Good, id=good_id)
    good.delete()
    return redirect('good_list')
