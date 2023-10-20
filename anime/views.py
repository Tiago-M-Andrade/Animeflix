from django.shortcuts import redirect, reverse
from .models import Anime, Episode, Categorie, User
from .forms import ProfileCreationForm, FormHome
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(FormView):
    template_name = 'homepage.html'
    form_class = FormHome

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('anime:animes')
        else:
            return super().get(request, *args, **kwargs)
        
    def get_success_url(self):
        email = self.request.POST.get('username')
        users_by_email = User.objects.filter(email=email)
        users_by_username = User.objects.filter(username=email)
        if users_by_email or users_by_username:
            return reverse('anime:login')
        else:
            return reverse('anime:createaccount')


class CreateAccount(FormView):
    template_name = 'createaccount.html'
    form_class = ProfileCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('anime:login')

class HomeAnimes(LoginRequiredMixin, ListView):
    template_name = 'homeanimes.html'
    model = Anime

class ProfileEdit(LoginRequiredMixin, UpdateView):
    template_name = 'profileedit.html'
    model = User
    fields = ['user_image', 'first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('anime:animes')

class AnimeDetail(LoginRequiredMixin, DetailView):
    template_name = 'animedetails.html'
    model = Anime

    def get(self, request, *args, **kwargs):
        anime = self.get_object()
        anime.num_views += 1
        anime.save()
        user = request.user
        user.watched_movies.add(anime)
        user.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AnimeDetail, self).get_context_data(**kwargs)
        filtered_anime = Anime.objects.filter(id=self.get_object().id)
        related_animes = Categorie.objects.filter(name=self.get_object().id)
        categories = Categorie.objects.all()
        context["related"] = related_animes
        context['current_anime'] = filtered_anime
        context['catnofilter'] = categories
        return context

class PlayAnime(LoginRequiredMixin, DetailView):
    template_name = 'playanime.html'
    model = Anime

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        episodeid = self.kwargs['pk2']
        filtered_anime = Anime.objects.filter(id=pk)
        related_animes = Categorie.objects.filter(name=filtered_anime.first().pk)
        episodelist = Episode.objects.filter(anime=pk)
        context['episode_list'] = episodelist
        context['episodeid'] = episodeid
        context['related'] = related_animes
        context['current_anime'] = filtered_anime
        return context

class SearchAnime(LoginRequiredMixin, ListView):
    template_name = 'searchanime.html'
    model = Anime

    def get_queryset(self):
        search_term = self.request.GET.get('q')
        if search_term:
            object_list = Anime.objects.filter(title__icontains=search_term)
            return object_list
        else:
            None