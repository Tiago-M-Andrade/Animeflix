from .models import Anime, Categorie

def allcategories(request):
    recent = Anime.objects.all().order_by('-creation_date')[0:12]
    most_watched = Anime.objects.all().order_by('-num_views')[0:12]
    drama = Categorie.objects.filter(category='DRAMA').order_by('-creation_date')
    supernatural = Categorie.objects.filter(category='SUPERNATURAL').order_by('-creation_date')
    horror = Categorie.objects.filter(category='HORROR').order_by('-creation_date')
    mystery = Categorie.objects.filter(category='MYSTERY').order_by('-creation_date')
    comedy = Categorie.objects.filter(category='COMEDY').order_by('-creation_date')
    romance = Categorie.objects.filter(category='ROMANCE').order_by('-creation_date')
    action = Categorie.objects.filter(category='ACTION').order_by('-creation_date')
    fantasy = Categorie.objects.filter(category='FANTASY').order_by('-creation_date')
    ecchi = Categorie.objects.filter(category='ECCHI').order_by('-creation_date')
    adventure = Categorie.objects.filter(category='ADVENTURE').order_by('-creation_date')
    anime_list = Anime.objects.all()
    return {"recent":recent, "most_watched":most_watched,
            "anime_list":anime_list, "allcat": (action,adventure,comedy,
                                                drama,ecchi,fantasy,
                                                horror,mystery,romance,
                                                supernatural)}