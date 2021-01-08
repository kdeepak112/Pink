from django.contrib import admin
from .models import patient
from .models import diseaseApi , mumbai,pune,ahemdabad,bengaluru,hyderabad,chennai,labBook,diseaseData,blog,PatientMessage
# Register your models here.

admin.site.register(patient)
admin.site.register(diseaseApi)
admin.site.register(mumbai)
admin.site.register(pune)
admin.site.register(ahemdabad)
admin.site.register(chennai)
admin.site.register(bengaluru)
admin.site.register(hyderabad)
admin.site.register(labBook)
admin.site.register(diseaseData)
admin.site.register(PatientMessage)

@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    class Media:
        js = ('tiny.js',)
        

