from django.contrib import admin
from MainAp.models import Company,Developer,Education,Contact
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'created_at')
    search_fields = ('name', 'email', 'phone', 'subject')
    list_filter = ('created_at',)

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'city', 'country', 'available_for_hire', 'experience_years')
    search_fields = ('name', 'email', 'city', 'skills')
    list_filter = ('employment_type', 'available_for_hire', 'country')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry_type', 'city', 'country', 'email', 'is_active', 'established_date')
    search_fields = ('name', 'city', 'country', 'email')
    list_filter = ('industry_type', 'country', 'is_active')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_year', 'end_year', 'python_developer')
    search_fields = ('degree', 'institution', 'python_developer__name')