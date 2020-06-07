from django.db import models

# Create your models here.
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this task')
    name = models.CharField(max_length=200, help_text='Enter task name')
    due_date=models.DateField(help_text='Enter due date , format - mm/dd/yyyy ')
    date_created=models.DateField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    
    STATUS = (
        ('n', 'New'),
        ('p', 'Progress'),
        ('c', 'Completed'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='n',
        help_text='Task status',
    )
    LABEL = (
        ('p', 'Personal'),
        ('w', 'Work'),
        ('s', 'Shopping'),
        ('o', 'Others'),
    )

    label = models.CharField(
        max_length=1,
        choices=LABEL,
        blank=True,
        default='p',
        help_text='Task Label',
    )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name})'
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('task-detail', args=[str(self.id)])

