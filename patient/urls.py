
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    
    path('', views.home,name="home"),
    path('signup/', views.SignUp,name="signup"),
    path('login/', views.login,name="login"),
    path('consult/', views.consult,name="consult"),
    path('covid/', views.covid,name="covid"),
    path('result/', views.result,name="result"),
    path('check/',views.check,name="check"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.logout,name="logout"),
    path('disease/',views.disease,name="disease"),
    path('covidInfo/',views.covidInfo,name="covidInfo"),
    path('selfAssess/',views.selfAssess,name="selfAssess"),
    path('UserLab/',views.UserLab,name="UserLab"),
    path('Linkupdate/',views.Linkupdate,name="Linkupdate"),
    path('update/<userid>/',views.update,name="update"),
    path('profile/',views.profile,name="profile"),
    path('feedback/',views.feedback,name="feedback"),
    path('book/',views.book,name="book"),
    path('bookLab/',views.bookLab,name="bookLab"),
    path('seeBooking/',views.seeBooking,name="seeBooking"),
    path('seeList/',views.seeList,name="seeList"),
    path('forgot/',views.forgot,name="forgot"),
    path('forgotPassword/',views.forgotPassword,name="forgotPassword"),
    path('otpCheck/',views.otpCheck,name="otpCheck"),
    path('blogarrive/',views.blogarrive,name="blogarrive"),
    path('blogform/',views.blogform,name="blogform"),
    path('blogEntry/<userid>/',views.blogEntry,name="blogEntry"),
    path('yourBlog/',views.yourBlog,name="yourBlog"),
    path('yourBlog/readBlog/<blogid>',views.readBlog,name="readBlog"),
    path('allBlog/',views.allBlog,name="allBlog"),
    path('allBlog/readBlog/<blogid>',views.readBlog,name="readBlog"),
    path('diseaseApi/',views.diseaseList.as_view()),
    path('mumbaiApi/',views.mumbaiList.as_view()),
    path('puneApi/',views.puneList.as_view()),
    path('labApi/',views.labBookList.as_view()),
    path('MessageApi/',views.MessageList.as_view()),
    path('PatientMessageApi/',views. PatientMessageList.as_view()),
    path('lab/',include("lab.urls")),
    path('doctor/',include("doctor.urls")),
    # Consult Doctor...
    path('displayDoc/<str:category>/', views.displayDoc,name="displayDoc"), 
    path('sendRequest/<int:doc_id>/<str:category>/', views.sendRequest,name="sendRequest"), 
    path('seeRequest/', views.seeRequest,name="seeRequest"), 
    path('Patientinbox/', views.Patientinbox,name="Patientinbox"), 
    path('Dmessage/<int:did>', views.Dmessage,name="Dmessage"), 
    path('Dmessage/SendDocMssg/', views.SendDocMssg,name="SendDocMssg"), 
    path('myChat/', views.myChat,name="myChat"), 
    path('antibody/', views.antibody,name="antibody"), 
    path('getPrescription/', views.getPrescription,name="getPrescription"), 

   
   
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
