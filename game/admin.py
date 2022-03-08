from django.contrib import admin

from .models import (
    EducationalPurposedProject,
    GameCarousel,
    GameDetail, 
    MyProject
)

class GameCarouselInline(admin.StackedInline):
    model = GameCarousel
    extra = 0


class GameDetailInline(admin.StackedInline):
    model = GameDetail
    extra = 0


class GameProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'release_date', 'created', 'updated']
    readonly_fields = ['created', 'updated']
    inlines = [GameDetailInline, GameCarouselInline]


# Register your models here.
admin.site.register(EducationalPurposedProject, GameProjectAdmin)
admin.site.register(MyProject, GameProjectAdmin)