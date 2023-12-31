from django.urls import path
from . import views
from authentication.views import login_view, logout_view, register_user, profile
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name="logout"),
    path('register/', register_user, name="register"),
    path('profile/', profile, name="profile"),

    path('sidenavcreate/', views.sidenavcreate, name='sidenavcreate'),
    path('folder/', views.create_folder, name='folder'),

    path('create_file/', views.create_file, name='create_file'),
    path('file_list/', views.file_list, name='file_list'),
    path('edit_file/<int:pk>/', views.edit_file, name='edit_file'),
    path('delete_file/<int:pk>/', views.delete_file, name='delete_file'),


    path('import_data/', views.import_data, name='import_data'),
    path('export_data/', views.export_data, name='export_data'),
    path('add_data/', views.add_data, name='add_data'),
    path('record/', views.record, name='records'),

    path('remove_data/<int:pk>/', views.remove_data, name='remove_data'),
    path('edit_data/<int:pk>/', views.edit_data, name='edit_data'),

    path('manage_user/', views.manage_user, name='manage_user'),
    path('remove_user/<int:pk>/', views.remove_user, name='remove_user'),
    path('edit_user/<int:pk>/', views.edit_user, name='edit_user'),
    path('search/', views.global_search, name='global_search'),

    path('download/<int:file_id>/', views.download_file, name='download_file'),

    path('pdf/', views.show_files_by_type, {'file_type': 'pdf'}, name='show_pdf_files'),
    path('excel/', views.show_files_by_type, {'file_type': 'excel'}, name='show_excel_files'),
    path('word/', views.show_files_by_type, {'file_type': 'word'}, name='show_word_files'),
    path('audio/', views.show_files_by_type, {'file_type': 'audio'}, name='show_audio_files'),
    path('video/', views.show_files_by_type, {'file_type': 'video'}, name='show_video_files'),
    path('image/', views.show_files_by_type, {'file_type': 'image'}, name='show_image_files'),
    path('ppt/', views.show_files_by_type, {'file_type': 'ppt'}, name='show_ppt_files'),




]
