from django.db import models

from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    TYPE_OF_EX = (
    ('ST', 'Stomach'),
    ('BA', 'Back'),
    ('LE', 'Legs'),
    ('AR', 'Arms'),
    ('WH', 'Whole'),
    )
    type_of_exercise = models.CharField(max_length=2, choices=TYPE_OF_EX)
    TYPE_OF_LEVEL = (
    ('L', 'Light'),
    ('M', 'Medium'),
    ('H', 'Hard'),
    )
    level = models.CharField(max_length=1, choices=TYPE_OF_LEVEL)
    created_date = models.DateTimeField(
            default=timezone.now)

#    published_date = models.DateTimeField(
#            blank=True, null=True)

#    def publish(self):
#        self.published_date = timezone.now()
#        self.save()

    def __str__(self):
        return self.title
