from datetime import date
from django.contrib import admin
from django.db import models
from django.contrib.admin import SimpleListFilter
from .models import Task

#creating_new_admin_filter
class Overdue_Filter(SimpleListFilter):
    title = 'overdue'
    parameter_name="overdue_date"
    def lookups(self, request, model_admin):
        return (
                ('Over_Due', 'Over_Due'),
                )

    def queryset(self, request, queryset):
        if self.value() == "Over_Due":
            return queryset.filter(due_date__lt=date.today())
        return   queryset

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'due_date','status','owner')
    list_filter = [Overdue_Filter,'status','owner']
    search_fields = ['name', 'owner']


admin.site.register(Task,TaskAdmin)
