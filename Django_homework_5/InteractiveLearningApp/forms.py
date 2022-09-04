from django import forms
from .models import Lesson, Language, Discussion, UserProfile, InfoCourse, TestQuiz


class LessonForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LessonForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Lesson
        exclude = ("user",)


class LanguageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LanguageForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Language
        exclude = ("user",)


class DiscussionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DiscussionForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Discussion
        exclude = ("user",)


class UserProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = UserProfile
        exclude = ("user",)


class InfoCourseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InfoCourseForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = InfoCourse
        exclude = ("user",)


class TestQuizForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TestQuizForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = TestQuiz
        exclude = ("user1",)