from django.contrib import admin
from .models import *


# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "surname",)
    list_filter = ("email",)
    search_fields = ("name",)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(UserProfile, UserProfileAdmin)


class TestQuizAdmin(admin.ModelAdmin):
    list_display = ("question", "answer",)
    list_filter = ("result",)

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(TestQuiz, TestQuizAdmin)


class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "text",)
    list_filter = ("title",)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Lesson, LessonAdmin)


class GrammarAdmin(admin.ModelAdmin):
    list_filter = ("lessons",)


admin.site.register(Grammar, GrammarAdmin)


class VocabularyAdmin(admin.ModelAdmin):
    list_filter = ("lessons",)


admin.site.register(Vocabulary, VocabularyAdmin)


class ConversationAdmin(admin.ModelAdmin):
    list_filter = ("lessons",)


admin.site.register(Conversation, ConversationAdmin)


class ListeningAdmin(admin.ModelAdmin):
    list_filter = ("lessons",)


admin.site.register(Listening, ListeningAdmin)


class SpeakingAdmin(admin.ModelAdmin):
    list_filter = ("lessons",)


admin.site.register(Speaking, SpeakingAdmin)


class LanguageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Language, LanguageAdmin)


class LanguagesAdmin(admin.ModelAdmin):
    list_filter = ("languages",)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Languages, LanguagesAdmin)


class CoursesAdmin(admin.StackedInline):
    model = Courses
    extra = 0


# admin.site.register(Courses, CoursesAdmin)


class InfoCourseAdmin(admin.ModelAdmin):
    list_display = ("title", "content",)
    list_filter = ("title",)
    inlines = [CoursesAdmin, ]


admin.site.register(InfoCourse, InfoCourseAdmin)


class DiscussionAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    list_filter = ("title",)


admin.site.register(Discussion, DiscussionAdmin)


class ForumAdmin(admin.ModelAdmin):
    list_filter = ("discussions",)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Forum, ForumAdmin)
