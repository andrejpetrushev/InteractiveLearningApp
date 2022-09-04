"""Django_homework_5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from InteractiveLearningApp.views import discussions, discussion, userprofile, index, info_courses, login, register, \
    foreign_language, foreign_languages, homepage, program_languages, quizzes, quiz_results, knowledge_check, js_c_php, \
    info_fgn_langs, html_css_java, c_swift_python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', index, name="index"),
                  path('discussions/', discussions, name="discussions"),
                  path('add/discussion/', discussion, name="discussion"),
                  path('userprofile/', userprofile, name="userProfile"),
                  path('infocourses/', info_courses, name="info_courses"),
                  path('login/', login, name="login"),
                  path('register/', register, name="register"),
                  path('foreignlanguage/', foreign_language, name="foreign_language"),
                  path('foreignlanguages/', foreign_languages, name="foreign_languages"),
                  path('homepage/', homepage, name="homepage"),
                  path('programlanguages/', program_languages, name="program_languages"),
                  path('quizzes/', quizzes, name="quizzes"),
                  path('quizresults/', quiz_results, name="quiz_results"),
                  path('knowledgecheck/', knowledge_check, name="knowledge_check"),
                  path('javascript&c++&php/', js_c_php, name="javascript_c++_php"),
                  path('informaticsforeignlanguages/', info_fgn_langs, name="informatics_foreign_languages"),
                  path('htmlcssjava/', html_css_java, name="html_css_java"),
                  path('cswiftpython/', c_swift_python, name="c_swift_python"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
