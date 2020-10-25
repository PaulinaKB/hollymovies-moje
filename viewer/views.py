from django.shortcuts import render
from django.http import HttpResponse
from viewer.models import Movie
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import FormView
from viewer.forms import MovieForm
# Create your views here.



class MovieCreateView(FormView):
  template_name = 'form.html'
  form_class = MovieForm


class MoviesView(ListView):
  template_name = 'movies.html'
  model = Movie



# class MoviesView(TemplateView):
#   template_name = 'movies.html'
#   extra_context = {'movies': Movie.objects.all()}


# class MoviesView(View):
#   def get(self, request):
#     return render(
#       request, template_name='movies.html',
#       context={'movies': Movie.objects.all()}
#     )


#
# def movies(request):
#     return render(
#         request, template_name='movies.html',
#         context={'movies': Movie.objects.all()}
#     )

# def hello(request, s0):
#   s1 = request.GET.get('s1', '')
#   return render(
#     request, template_name='hello.html',
#     context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
#   )



# def hello(request, s0):
#     s1 = request.GET.get('s1', '')
#     return HttpResponse(f'Hello, {s0} and {s1} world!')
#

# def hello(request):
#     return HttpResponse('Hello, world!')