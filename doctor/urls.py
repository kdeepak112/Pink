
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    
    
   path('', views.docHome,name="docHome"), 
   path('DocRegister/', views.DocRegister,name="DocRegister"), 
   path('docLogin/', views.docLogin,name="docLogin"), 
   path('docDashboard/', views.docDashboard,name="docDashboard"), 
   path('docLogout/', views.docLogout,name="docLogout"), 
   path('seePatient/', views.seePatient,name="seePatient"), 
   path('patientConfirm/<str:reqid>', views.patientConfirm,name="patientConfirm"), 
   path('patientDelete/<str:reqid>', views.patientDelete,name="patientDelete"), 
   path('Docinbox/', views.Docinbox,name="Docinbox"), 
   path('prescriptions/', views.prescriptions,name="prescriptions"), 
   path('prescriptions/uploadPrescription/<int:pid>', views.uploadPrescription,name="uploadPrescription"), 
   path('myConversations/', views.myConversations,name="myConversations"), 
   path('Pmessage/<int:pid>', views.Pmessage,name="Pmessage"), 
   path('Pmessage/sendMssg/<int:pid>', views.sendMssg,name="sendMssg"), 
   
   
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
