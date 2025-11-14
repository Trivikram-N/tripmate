from django.shortcuts import render
from .models import Place, Category
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def places(request):
    
    # Get all categories (only names)
    categories = Category.objects.values_list('name', flat=True)

    # Get all places
    places = Place.objects.all()

    context = {
        "categories": categories,
        "places": places,
    }

    return render(request, 'index.html', context)



@login_required
def liked_places(request):
    liked = request.user.details.liked_places.all()
    return render(request, "liked.html", {"liked": liked})



def like_place(request, place_id):

    # If user is NOT logged in — return JSON so JS can redirect
    if not request.user.is_authenticated:
        return JsonResponse({"auth": False})

    user_details = request.user.details
    place = get_object_or_404(Place, id=place_id)

    # Toggle like
    if place in user_details.liked_places.all():
        user_details.liked_places.remove(place)
        liked = False
    else:
        user_details.liked_places.add(place)
        liked = True

    return JsonResponse({"liked": liked, "auth": True})



def destination_details(request, place_name):
    place = get_object_or_404(Place, title=place_name)
    return render(request, 'details.html', {'place': place})