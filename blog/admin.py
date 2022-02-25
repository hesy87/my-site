from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from blog.models import Post,category,commnet

class postadmin (SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','Author','conted_view','status','created_date','published_date',)
    list_filter = ('status','Author',)
    ordering = ['-created_date']
    search_fields = ['title','content'] 
    summernote_fields = ('content',)

class commentadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','subject','approach','created_date','updated_date',)

admin.site.register(commnet,commentadmin)  
admin.site.register(category)
admin.site.register(Post,postadmin)
