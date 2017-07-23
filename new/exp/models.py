from django.db import models
from .validators import validate_file_extension


class Image(models.Model) :
    title = models.CharField(max_length=20)
    img = models.ImageField()
    time = models.DateTimeField()
    verify = models.BooleanField()

    def __str__(self) :
        return self.title

class XML(models.Model) :
    title = models.CharField(max_length=20)
    xml = models.FileField(validators=[validate_file_extension])
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self) :
        return self.title

    class Meta :
        ordering = ('title',)

# Create your models here.
