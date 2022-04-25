from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

RATING = (
    ('A', 'okay'),
    ('AA', 'Good'),
    ('AAA', 'Great')
)
class Author(models.Model):
    name = models.CharField(max_length=50)
    poems = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'pk': self.id})

class poem(models.Model):
    name = models.CharField(max_length=100)
    published = models.DateField(blank="true")
    image = models.URLField
    authors = models.ManyToManyField(Author)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'poem_id': self.id})
    def __str__(self):
        return self.name

    
class Read(models.Model):
    read = models.BooleanField()
    date = models.DateField()
    rating = models.CharField(max_length=1, choices=RATING, default=RATING[2][0])
    poem = models.ForeignKey(poem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()} on {self.date}"