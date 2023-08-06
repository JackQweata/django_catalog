from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from pytils.translit import slugify

from catalog.models import Product, BlogPost


class ProductsListView(ListView):
    model = Product


def contacts(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'catalog/contacts.html', context)


class ProductDetailView(DetailView):
    model = Product


class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'catalog/blog_post_list.html'
    queryset = BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'catalog/blog_post_detail.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'catalog/blog_post_u_c.html'
    fields = ('title', 'content', 'preview_image', 'is_published',)
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        if form.is_valid():
            new_nat = form.save()
            new_nat.slug = slugify(new_nat.title)
            new_nat.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        self.object = super().get_context_data(**kwargs)
        self.object['title'] = 'Создать пост'
        return self.object


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'content', 'preview_image', 'is_published',)
    template_name = 'catalog/blog_post_u_c.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        self.object = super().get_context_data(**kwargs)
        self.object['title'] = 'Изменить пост'
        return self.object


class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'catalog/blog_post_delete.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    success_url = reverse_lazy('posts')
