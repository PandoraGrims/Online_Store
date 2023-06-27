from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from webapp.models import Good


def good_list_view(request):
    goods = Good.objects.order_by("-updated_at")
    context = {"goods": goods}
    return render(request, "index.html", context)


def good_create_view(request):
    if request.method == "GET":
        return render(request, "create_good.html")
    else:
        Good.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
        )
        return HttpResponseRedirect("/")


def goods_view(request):
    good_id = request.GET.get("id")
    good = Good.objects.get(id=good_id)
    return render(request, "good.html", {"good": good})


def delete_good(request):
    good_id = request.GET.get("id")
    good = Good.objects.get(id=good_id)
    good.delete()
    return redirect('good_list')
