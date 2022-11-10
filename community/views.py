from django.contrib import messages
from django.shortcuts import render, redirect
from community.models import Memory
from django.views.generic import CreateView
from community.forms import CommunityForm


def community_list(request):
    posts = Memory.objects.all().order_by('-pk')
    return render(
        request,
        'community/column.html',
        {
            'posts': posts,
        }
    )


def column_detail(request, pk):
    post = Memory.objects.get(pk=pk)

    return render(
        request,
        'community/column_detail.html',
        {
            'post': post,
        }
    )


def column_new(request):
    if request.method == "GET":
        form = CommunityForm()
    else:
        form = CommunityForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, "메모리 생성")
            return redirect(post)
            # return redirect(f"/diary/{post.pk}/")

    return render(request, "community/column_new.html", {
        "form": form,
    })


def memory_edit(request, pk):
    memory = Memory.objects.get(pk=pk)

    if request.method == "POST":
        form = CommunityForm(request.POST, instance=memory)
        if form.is_valid():
            # form.cleaned_data
            memory = form.save()
            messages.success(request, "메모리를 저장했습니다.")
            # return redirect(f"/diary/{memory.pk}/")
            # return redirect(memory.get_absolute_url())
            return redirect(memory)
    else:
        form = CommunityForm(instance=memory)
    return render(request, "community/column_new.html", {
        "form": form,
    })


def memory_delete(request, pk):
    memory = Memory.objects.get(pk=pk)
    # TODO: delete memory
    # delete memory
    if request.method == "POST":
        memory.delete()
        messages.success(request, "메모리를 삭제했습니다.")
        return redirect("/diary/")

    return render(request, "diary/memory_comfirm_delete.html", {
        'memory': memory,
    })
