from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    surname = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    password = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name + " " + self.surname


class TestQuiz(models.Model):
    question = models.CharField(max_length=50)
    answer = models.TextField(null=True, blank=True)
    result = models.CharField(max_length=75)
    percents = models.ImageField(upload_to="result_images/", null=True, blank=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Lesson(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(null=True, blank=True)
    quizzes = models.ForeignKey(TestQuiz, on_delete=models.CASCADE, null=True, blank=True)
    external_links = models.URLField()

    def __str__(self):
        return self.title


class Grammar(models.Model):
    lessons = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)


class Vocabulary(models.Model):
    lessons = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)


class Conversation(models.Model):
    lessons = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)


class Listening(models.Model):
    lessons = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)


class Speaking(models.Model):
    lessons = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)


class Language(models.Model):
    grammar = models.ForeignKey(Grammar, on_delete=models.CASCADE, null=True, blank=True)
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE, null=True, blank=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, null=True, blank=True)
    listening = models.ForeignKey(Listening, on_delete=models.CASCADE, null=True, blank=True)
    speak = models.ForeignKey(Speaking, on_delete=models.CASCADE, null=True, blank=True)


class Languages(models.Model):
    languages = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)


class InfoCourse(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="course_images/", null=True, blank=True)
    lessons = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Courses(models.Model):
    informatics = models.ForeignKey(InfoCourse, on_delete=models.CASCADE, null=True, blank=True)
    foreign_languages = models.ForeignKey(Languages, on_delete=models.CASCADE, null=True, blank=True)


class Discussion(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    opinion = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Forum(models.Model):
    discussions = models.ForeignKey(Discussion, on_delete=models.CASCADE, null=True, blank=True)