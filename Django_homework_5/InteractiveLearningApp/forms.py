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
        fields = "__all__"


class LanguageForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LanguageForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Language
        fields = "__all__"


class DiscussionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DiscussionForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Discussion
        exclude = ("author",)
        fields = ['title', 'date']


class UserProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = UserProfile
        exclude = ("user",)
        fields = ['email', 'password']


class InfoCourseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InfoCourseForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = InfoCourse
        fields = "__all__"


class TestQuizForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TestQuizForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = TestQuiz
        exclude = ("user1",)
        fields = ['question', 'answer', 'result', 'percents']


class createuserform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(createuserform, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            print(field)
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = UserProfile
        exclude = ("user",)
