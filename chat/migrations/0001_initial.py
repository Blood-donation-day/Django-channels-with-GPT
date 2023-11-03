# Generated by Django 4.2.1 on 2023-11-03 05:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RolePlayingRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('en-US', 'English'), ('ja-JP', 'Japanese'), ('zh-CN', 'Chinese'), ('es-ES', 'Spanish'), ('fr-FR', 'French'), ('de-DE', 'German'), ('ru-RU', 'Russian')], default='en-US', max_length=10, verbose_name='대화 언어')),
                ('level', models.SmallIntegerField(choices=[(1, '초급'), (2, '고급')], default=1, verbose_name='레벨')),
                ('situation', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)], verbose_name='상황')),
                ('situation_en', models.CharField(blank=True, help_text='GPT 프롬프트에 직접적으로 활용됩니다. 비워두시면, 자동으로 번역됩니다.', max_length=100, verbose_name='상황 (영문)')),
                ('my_role', models.CharField(max_length=100, verbose_name='내 역할')),
                ('my_role_en', models.CharField(blank=True, help_text='GPT 프롬프트에 직접적으로 활용됩니다. 비워두시면, 자동으로 번역됩니다.', max_length=100, verbose_name='내 역할 (영문)')),
                ('gpt_role', models.CharField(max_length=100, verbose_name='GPT 역할')),
                ('gpt_role_en', models.CharField(blank=True, help_text='GPT 프롬프트에 직접적으로 활용됩니다. 비워두시면, 자동으로 번역됩니다.', max_length=100, verbose_name='GPT 역할 (영문)')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
