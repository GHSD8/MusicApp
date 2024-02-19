from django.db import models

class Song(models.Model):
    title = models.TextField()
    artist = models.TextField()
    image = models.ImageField(upload_to='songs_image/')
    audio_file = models.FileField(upload_to='songs/')
    album = models.ForeignKey('Album',on_delete=models.SET_NULL, null=True,blank=True)


    def __str__(self):
        return self.title

    class META:
        ordering = ["title"]


class Album(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
