from django.contrib import admin

from .models import(
    About,
    ProfessionalSummary,
)

# Register your models here.
class ProfessionalSummaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    readonly_fields = ['created', 'updated']


class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'description']
    readonly_fields = ['created', 'updated']


admin.site.register(ProfessionalSummary, ProfessionalSummaryAdmin)
admin.site.register(About, AboutAdmin)
