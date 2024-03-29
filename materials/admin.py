from django.contrib import admin

from materials.models import Course, Lesson


@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'owner',)


@admin.register(Lesson)
class AdminLesson(admin.ModelAdmin):
    list_display = ('course', 'title', 'description', 'image', 'url_video', 'owner',)
