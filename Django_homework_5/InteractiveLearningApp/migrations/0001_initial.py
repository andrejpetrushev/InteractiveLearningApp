# Generated by Django 4.1 on 2022-08-22 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('opinion', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Grammar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField(blank=True, null=True)),
                ('external_links', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='TestQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50)),
                ('answer', models.TextField(blank=True, null=True)),
                ('result', models.CharField(max_length=75)),
                ('percents', models.ImageField(blank=True, null=True, upload_to='result_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lessons', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InteractiveLearningApp.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('surname', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
                ('password', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Speaking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lessons', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InteractiveLearningApp.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='Listening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lessons', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InteractiveLearningApp.lesson')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='quizzes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InteractiveLearningApp.testquiz'),
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InteractiveLearningApp.language')),
            ],
        ),
        migrations.AddField(
            model_name='language',
            name='conv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InteractiveLearningApp.lesson'),
        ),
        migrations.AddField(
            model_name='language',
            name='grammar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InteractiveLearningApp.grammar'),
        ),
        migrations.AddField(
            model_name='language',
            name='listening',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InteractiveLearningApp.listening'),
        ),
        migrations.AddField(
            model_name='language',
            name='speak',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InteractiveLearningApp.speaking'),
        ),
        migrations.AddField(
            model_name='language',
            name='vocabulary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InteractiveLearningApp.vocabulary'),
        ),
        migrations.CreateModel(
            name='InfoCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='course_images/')),
                ('lessons', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InteractiveLearningApp.lesson')),
            ],
        ),
        migrations.AddField(
            model_name='grammar',
            name='lessons',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InteractiveLearningApp.lesson'),
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discussions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InteractiveLearningApp.discussion')),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foreign_languages', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InteractiveLearningApp.languages')),
                ('informatics', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InteractiveLearningApp.infocourse')),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lessons', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InteractiveLearningApp.lesson')),
            ],
        ),
    ]
