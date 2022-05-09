from django.test import TestCase
from django.urls import reverse, resolve
from .views import HomePageView
from .views import ArticleDetail, ArticleList, ArticleCategoryList

# Create your tests here.


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, HomePageView)


    def test_article_url_status_code(self):
        view = resolve('/articles')
        self.assertEquals(view.func.view_class, ArticleList)

    def test_category_view_status_code(self):
        url = reverse('articles-category-list', args=('name',))
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        
    def test_category_url_status_code(self):
        view = resolve('/articles/category/<slug>')
        self.assertEquals(view.func.view_class, ArticleCategoryList)

        
    def test_category_url_status_code(self):
        view = resolve('/articles/<year>/<month>/<day>/<slug>')
        self.assertEquals(view.func.view_class, ArticleDetail)
