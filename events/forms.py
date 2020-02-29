from django import forms
from .models import Ticket
import phonenumbers

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket

        fields = ('name','email','phone_number','attendees')

    def clean(self):
        cleaned_data = super(TicketForm,self).clean()

        gotten_phone_number = cleaned_data.get('phone_number')

        if gotten_phone_number[:4] == '+254':
            string_to_phonenumber = phonenumbers.parse(gotten_phone_number,"KE")

            print(len(gotten_phone_number))

            if phonenumbers.is_possible_number(string_to_phonenumber) != True or len(gotten_phone_number)!=13:

                print("This is not a valid phone number!")
                raise forms.ValidationError('This is not a valid Kenyan phone number!')
        elif gotten_phone_number[:2]=="07":

            without_zero = gotten_phone_number[1:]

            add_country_code = '+254'+without_zero

            string_to_phonenumber = phonenumbers.parse(add_country_code,'KE')

            if phonenumbers.is_possible_number(string_to_phonenumber) != True or len(add_country_code)!=13:

                raise forms.ValidationError("This is not a valid Kenyan phone number!")
        else:

            raise forms.ValidationError("This is not a valid Kenyan phone number!")

        return cleaned_data


        