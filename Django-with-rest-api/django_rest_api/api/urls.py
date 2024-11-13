from django.urls import path
from . import views, api_views
from django.conf.urls.static import static

urlpatterns = [
    # HTML CRUD URLs
    path('tour/', views.TourListView.as_view(), name='tour_list'),
    path('tour/create/', views.TourCreateView.as_view(), name='tour_create'),
    path('tour/<int:pk>/update/', views.TourUpdateView.as_view(), name='tour_update'),
    path('tour/<int:pk>/delete/', views.TourDeleteView.as_view(), name='tour_delete'),

    # API URLs
    path('api/tour/', api_views.TourListCreateAPI.as_view(), name='tour-list-create-api'),
    path('api/tour/<int:pk>/', api_views.TourListDetailAPI.as_view(), name='tour-detail-api'),
    path('api/tourdetails/', api_views.TourDetailsListCreateAPI.as_view(), name='tourdetails-list-create'),
    path('api/tourdetails/<int:pk>/', api_views.TourDetailsDetailAPI.as_view(), name='tourdetails-detail'),
    path('api/tourdetails/by-title/<int:title_id>/', api_views.TourDetailsByTitleAPI.as_view(), name='tourdetails-by-title'),
]
