from django.urls import path
from . import views


app_name="main"

urlpatterns=[
    path('',views.IndexView.as_View(),name="home"),
    path('contact/', views.ContactView.as_View(), name="contact"),
    path('portfolio/', views.PortfolioView.as_View(), name="portfolios"),
    path('portfolio/<slug:slug>', views.PortfolioDetailView.as_View(), name="portfolio"),
    path('blog/', views.BlogView.as_View(), name="blogs"),
    path('blog/<slug:slug>', views.BlogDetailView.as_View(), name="blog"),
]
