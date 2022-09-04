from django.shortcuts import render
from .models import Discussion, UserProfile, InfoCourse, Languages, TestQuiz
from .forms import DiscussionForm, UserProfileForm, InfoCourseForm, LanguageForm, TestQuizForm


# Create your views here.

def index(request):
    return render(request, 'index.html')


def discussions(request):
    queryset = Discussion.objects.filter(author=request.user).all()
    context = {"discussions": queryset, "form": DiscussionForm}
    return render(request, 'discussions.html', context=context)


def discussion(request):
    return render(request, 'discussion.html')


def userprofile(request):
    queryset = UserProfile.objects.filter(user=request.user).all()
    context = {"userProfile": queryset, "form": UserProfileForm}
    return render(request, 'userProfile.html', context=context)


def info_courses(request):
    queryset = InfoCourse.objects.filter(author=request.user).all()
    context = {"info_courses": queryset, "form": InfoCourseForm}
    return render(request, 'info_courses.html', context=context)


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def foreign_language(request):
    return render(request, 'foreign_language.html')


def foreign_languages(request):
    queryset = Languages.objects.filter(author=request.user).all()
    context = {"foreign_languages": queryset, "form": LanguageForm}
    return render(request, 'foreign_languages.html', context=context)


def homepage(request):
    return render(request, 'homepage.html')


def program_languages(request):
    queryset = Languages.objects.filter(author=request.user).all()
    context = {"foreign_languages": queryset, "form": LanguageForm}
    return render(request, 'foreign_languages.html', context=context)


def knowledge_check(request):
    return render(request, 'knowledge_check.html')


def quizzes(request):
    return render(request, 'quizzes.html')


def quiz_results(request):
    queryset = TestQuiz.objects.filter(user1=request.user).all()
    context = {"quizzes": queryset, "form": TestQuizForm}
    return render(request, 'quiz_results.html', context=context)


def js_c_php(request):
    return render(request, 'javascript&c++&php.html')


def info_fgn_langs(request):
    return render(request, 'informatics&foreign_languages.html')


def html_css_java(request):
    return render(request, 'html&css&java.html')


def c_swift_python(request):
    return render(request, 'c#(.net)&swift&python.html')

