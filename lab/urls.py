
from django.urls import path
from . import views

urlpatterns = [

    
    path('', views.labHome,name="labHome"),
    path('labregister/', views.labregister,name="labregister"),
    path('labLogin/', views.labLogin,name="labLogin"),
    path('labDashboard/', views.labDashboard,name="labDashboard"),
    path('logoutLab/', views.logoutLab,name="logoutLab"),
    path('confirmBooking/', views.confirmBooking,name="confirmBooking"),
    path('confirmBooking/confirm/<userid>/', views.confirm,name="confirm"),
    path('labDashboard/uploadReport/<msg>', views.uploadReports,name="uploadReports"),
    path('labDashboard/uploadReport/upload/', views.upload,name="upload"),
    path('labDashboard/bookingStatus/<msg>/', views.bookingStatus,name="bookingStatus"),
    path('labDashboard/bookingStatus/<msg>/updateBooking/<userid>/', views.updateBooking,name="updateBooking"),
    path('labDashboard/deleteUser/<msg>', views.deleteUser,name="deleteUser"),
    path('labDashboard/deleteUser/deleteBooking/<userid>/', views.deleteBooking,name="deleteBooking"),
    path('userList/', views.userList,name="userList"),
   
    
    
  
    
   
   
    
]
