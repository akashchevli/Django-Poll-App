# Generated by Django 3.1.4 on 2020-12-10 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_poll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pollquestion',
            name='user',
        ),
        migrations.RemoveField(
            model_name='voting',
            name='choice_id',
        ),
        migrations.RemoveField(
            model_name='voting',
            name='question_id',
        ),
        migrations.RemoveField(
            model_name='voting',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='PollChoice',
        ),
        migrations.DeleteModel(
            name='PollQuestion',
        ),
        migrations.DeleteModel(
            name='Voting',
        ),
    ]
