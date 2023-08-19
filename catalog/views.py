from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from pytils.translit import slugify
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, BlogPost, Version


def contacts(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'catalog/contacts.html', context)


class ProductsListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'catalog/form_create_update.html'
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        FormSet = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        with transaction.atomic():
            if form.is_valid():
                self.object = form.save()
                if formset.is_valid():
                    formset.instance = self.object
                    formset.save()

        return super().form_valid(form)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/form_create_update.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        FormSet = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        with transaction.atomic():
            if form.is_valid():
                self.object = form.save()
                if formset.is_valid():
                    formset.instance = self.object
                    formset.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/page_delete.html'


# blog
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'catalog/blog/blog_post_list.html'
    queryset = BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'catalog/blog/blog_post_detail.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'catalog/form_create_update.html'
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
    template_name = 'catalog/form_create_update.html'
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
    template_name = 'catalog/page_delete.html'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'
    success_url = reverse_lazy('posts')
