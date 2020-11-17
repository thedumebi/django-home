from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db.models import Q

from .models import Ad, Comment, Fav
from .owner import OwnerCreateView, OwnerUpdateView, OwnerDeleteView, OwnerListView, OwnerDetailView
from .utils import dump_queries
from .forms import CommentForm, PictureForm

# Create your views here.
class AdListView(OwnerListView):
    #model = Ad
    template_name = "ads/ad_list.html"

    def get(self, request) :
        ad_list = Ad.objects.all()
        for ad in ad_list:
            ad.natural_updated = naturaltime(ad.updated_at)
        favorites = list()
        if request.user.is_authenticated:
            # rows = [{'id': 2}, {'id': 4} ... ]  (A list of rows)
            rows = request.user.favorite_ads.values('id')
            # favorites = [2, 4, ...] using list comprehension
            favorites = [ row['id'] for row in rows ]
        ctx = {'ad_list' : ad_list, 'favorites': favorites}
        return render(request, self.template_name, ctx)

class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'
    def get(self, request, pk):
        x = Ad.objects.get(id=pk)
        comments = Comment.objects.filter(ad=x).order_by('-updated_at')
        comment_ad = CommentForm()
        ctx = {'ad': x, 'comments': comments, 'comment_ad': comment_ad}
        return render(request, self.template_name, ctx)

class AdCreateView(OwnerCreateView):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')
    def get(self, request):
        form = PictureForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)
    
    def post(self, request):
        form = PictureForm(request.POST, request.FILES or None)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
        ad = form.save(commit = False)
        ad.owner = self.request.user
        ad.save()
        return redirect(self.success_url)

class AdUpdateView(OwnerUpdateView):
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:all')
    def get(self, request, pk):
        ad = get_object_or_404(Ad, id = pk, owner = self.request.user)
        form = PictureForm(instance=ad)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        ad = get_object_or_404(Ad, id=pk, owner = self.request.user)
        form = PictureForm(request.POST, request.FILES or None, instance = ad)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
        form.save()
        return redirect(self.success_url)

class AdDeleteView(OwnerDeleteView):
    model = Ad
    template_name = 'ads/ad_delete.html'
    success_url = reverse_lazy('ads:all')

class CommentCreate(LoginRequiredMixin, View):
    template_name = 'ads/ad_detail.html'
    """def post(self, request, pk):
        ad = get_object_or_404(Ad, id = pk)
        comm = Comment(text= request.POST['text'], owner = request.user, ad = ad)
        comm.save()
        return redirect(reverse_lazy('ads:ad_detail', args = [pk]))"""
    def post(self, request, pk):
        ad = get_object_or_404(Ad, id = pk)
        comments = Comment.objects.filter(ad=ad).order_by('-updated_at')
        comment_ad = CommentForm(request.POST)
        if not comment_ad.is_valid():
            ctx = {'ad': ad, 'comments': comments, 'comment_ad': comment_ad}
            return render(request, self.template_name, ctx)
        comment = comment_ad.save(commit = False)
        comment.owner = self.request.user
        comment.ad = ad
        comment.save()
        return redirect(reverse_lazy('ads:ad_detail', args = [pk]))

class CommentEdit(LoginRequiredMixin, View):
    template_name = 'ads/comment_edit.html'
    success_url = reverse_lazy('ads:ad_detail')
    def get(self, request, pk):
        comm = get_object_or_404(Comment, id=pk, owner = self.request.user)
        comment_ad = CommentForm(instance=comm)
        ad_id = comm.ad.id
        ad = get_object_or_404(Ad, id = ad_id)
        comments = Comment.objects.filter(ad=ad).order_by('-updated_at')
        ctx = {'comment_ad': comment_ad, 'comment':comm, 'ad_id':ad_id, 'ad':ad, 'comments':comments}
        return render(request, self.template_name, ctx)

    
    def post(self, request, pk):
        comm = get_object_or_404(Comment, id = pk)
        ad_id = comm.ad.id
        ad = get_object_or_404(Ad, id=ad_id)
        comments = Comment.objects.filter(ad=ad).order_by('-updated_at')
        comment_ad = CommentForm(request.POST)
        print(comment_ad)
        if not comment_ad.is_valid():
            ctx = {'comment_ad': comment_ad, 'comment':comm, 'ad_id':ad_id, 'ad':ad, 'comments':comments}
            return render(request, self.template_name, ctx)
        comm.text = request.POST['text']
        print(comm.text)
        comm.save()
        return redirect(reverse_lazy('ads:ad_detail', args = [ad_id]))
    

class CommentDelete(OwnerDeleteView):
    model = Comment
    fields = ['comment']
    template_name = 'ads/comment_delete.html'
    #success_url = reverse_lazy('ads:ad_detail')
    def get_success_url(self):
        ad= self.object.ad
        return reverse_lazy('ads:ad_detail', args=[ad.id])

def picture_file(request, pk):
    ad = get_object_or_404(Ad, id = pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

@method_decorator(csrf_exempt, name='dispatch')
class AddFavourite(LoginRequiredMixin, View):
    def post(slef, request, pk):
        ad = get_object_or_404(Ad, id=pk)
        fav = Fav(owner = request.user, ad = ad)
        try:
            fav.save()
        except IntegrityError as e:
            pass
        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavourite(LoginRequiredMixin, View):
    def post(self, request, pk):
        ad = get_object_or_404(Ad, id=pk)
        try:
            fav = Fav.objects.get(owner = request.user, ad=ad).delete()
        except Fav.DoesNotExist as e:
            pass
        return HttpResponse()
        
