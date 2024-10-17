from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Song, Singer, Comment
from django.db.models import Q
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
import time


def song_list(request):
    song_list = Song.objects.all()
    paginator = Paginator(song_list, 100) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'music/song_list1.html', {'page_obj': page_obj})

def song_detail(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    comments = Comment.objects.filter(song=song).order_by('-created_at')

    if request.method == 'POST':
        text = request.POST.get('text')
        Comment.objects.create(song=song, text=text, created_at=timezone.now())
        return HttpResponseRedirect(reverse('song_detail', args=[song_id]))

    return render(request, 'music/song_detail1.html', {'song': song, 'comments': comments})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    song_id = comment.song.pk
    if request.method == 'POST':
        comment.delete()
        return HttpResponseRedirect(reverse('song_detail', args=[song_id]))

    return redirect('song_detail', song_id=song_id)


def singer_list(request):
    singer_list = Singer.objects.all()
    paginator = Paginator(singer_list, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'music/singer_list1.html', {'page_obj': page_obj})

def singer_detail(request, singer_id):
    singer = get_object_or_404(Singer, pk=singer_id)
    songs = Song.objects.filter(singer=singer)
    return render(request, 'music/singer_detail1.html', {'singer': singer, 'songs': songs})

def search(request):
    start_time = time.time()
    
    query = request.GET.get('q')
    search_type = request.GET.get('type')
    results = []
    elapsed_time = 0

    if query and search_type:
        
        if search_type == 'song':
            results = Song.objects.filter(Q(title__icontains=query) | Q(singer__singer_name__icontains=query) | Q(lyrics__icontains=query))
        elif search_type == 'singer':
            results = Singer.objects.filter(Q(singer_name__icontains=query) | Q(summ__icontains=query))

        

    paginator = Paginator(results, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) if results else None
    end_time = time.time()
    elapsed_time = end_time - start_time
    return render(request, 'music/search_result1.html', {
        'page_obj': page_obj,
        'query': query,
        'search_type': search_type,
        'elapsed_time': elapsed_time
    })