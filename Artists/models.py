from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=250)
    dp = models.ImageField(upload_to='static/profiles')

    def __str__(self):
        return self.name

    def save_artist(self):
        self.save()

    def delete_artist(self):
        self.delete()

    @classmethod
    def get_artists(cls):
        all_artists = cls.object.all()
        return all_artists

    @classmethod
    def get_single_artist(cls,artist_id):
        single_artist = cls.object.get(id=artist_id)

    @classmethod
    def update_artist(cls,id,update):
        artist_update = cls.objects.filter(id=id).update(artists=update)
        return artist_update

    