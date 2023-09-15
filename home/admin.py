from django.contrib import admin
from .models import Category, TableFile
from import_export.admin import ImportExportModelAdmin

class SidenavAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

admin.site.register(Category, SidenavAdmin)
class TableFileAdmin(ImportExportModelAdmin):
    list_display = ('file_name','date_created','date_modified')

@admin.register(TableFile)
class TableFileAdmin(ImportExportModelAdmin):
    list_display = ('file_name','date_created','date_modified')

 