from django.contrib import admin
from . models import Result
# Register your models here.

class resultAdmin(admin.ModelAdmin):
    list_display = ('id','student_id','student_name','students_father_name','students_mother_name','bangla','math','english','science','social','religuion')

        
    
    

admin.site.register(Result,resultAdmin)
