from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=50)
    venue = models.CharField(max_length=100)
    date = models.DateField()
    timeStart = models.TimeField()
    timeEnd = models.TimeField()
    img = models.ImageField(upload_to='static/img',null=True)
    about = models.CharField(max_length=1000)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def save_event(self):
        self.save()

    def delete_event(self):
        self.delete()

    @classmethod
    def get_events(cls):
        all_events = cls.objects.all()
        return all_events

    @classmethod
    def get_single_event(cls,event_id):
        single_event = cls.objects.get(id=event_id)
        return single_event
    @classmethod
    def update_event(cls,id, update):
        event_update = cls.objects.filter(id=id).update(events=update)
        return event_update

class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(null=False, blank=False,unique=True,)
    ticket_number = models.UUIDField(default=uuid.uuid4,editable=False)
    payment_code = models.CharField(max_length=255)
    attendees = models.IntegerField(null=False)

    def __str__(self):
        return self.name + "  " + str(self.ticket_number)

    @classmethod
    def get_tickets(cls):
        tickets = cls.objects.all()
        return tickets

    @classmethod
    def get_single_ticket(cls,ticket_id):
        single_ticket = cls.objects.get(id=ticket_id)
        return single_ticket