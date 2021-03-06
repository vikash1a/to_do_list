# Generated by Django 3.0.3 on 2020-05-25 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this task', primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter task name', max_length=200)),
                ('due_date', models.DateField(help_text='Enter due date')),
                ('date_created', models.DateField()),
                ('status', models.CharField(blank=True, choices=[('n', 'New'), ('p', 'Progress'), ('c', 'Completed')], default='n', help_text='Task status', max_length=1)),
                ('label', models.CharField(blank=True, choices=[('p', 'Personal'), ('w', 'Work'), ('s', 'Shopping'), ('o', 'Others')], default='p', help_text='Label', max_length=1)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
