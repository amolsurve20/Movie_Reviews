from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Review, Movie
from .forms import ReviewForm
import datetime


def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def movie_list(request):
    movie_list = Movie.objects.order_by('-name')
    context = {'movie_list':movie_list}
    return render(request, 'reviews/movie_list.html', context)


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    form = ReviewForm()
    return render(request, 'reviews/movie_detail.html', {'movie': movie, 'form': form})


def add_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.movie = movie
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:movie_detail', args=(movie.id,)))
    
    return render(request, 'reviews/movie_detail.html', {'movie': movie, 'form': form})