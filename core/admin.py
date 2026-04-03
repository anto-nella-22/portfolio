from django.contrib import admin
from django.utils.html import format_html
from .models import Project, Skill, Testimonial


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_short_description', 'tech_stack', 'live_url', 'github_url', 'image_preview')
    search_fields = ('title', 'description', 'tech_stack')
    list_filter = ('tech_stack',)
    ordering = ('-id',)
    readonly_fields = ('image_preview',)

    def get_short_description(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    get_short_description.short_description = 'Description'

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;" />', obj.image.url)
        return 'No image'
    image_preview.short_description = 'Image Preview'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'icon_preview')
    search_fields = ('name',)
    list_filter = ('level',)
    ordering = ('name',)
    readonly_fields = ('icon_preview',)

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.icon.url)
        return 'No icon'
    icon_preview.short_description = 'Icon Preview'


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'get_short_text', 'photo_url')
    search_fields = ('name', 'role', 'text')
    list_filter = ('role',)
    ordering = ('name',)

    def get_short_text(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    get_short_text.short_description = 'Testimonial Text'


# Register your models here.
