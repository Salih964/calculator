from django import forms


class RegistrationForm(forms.Form):

    username=forms.CharField()

    password=forms.CharField()

    email=forms.EmailField()


class BmrForm(forms.Form):

    height=forms.IntegerField()

    weight=forms.IntegerField()

    age=forms.IntegerField()

    options=(
    ("male","male"),
    ("female", "female")
    )

    gender=forms.ChoiceField(choices=options)    

    choices=(
        (1,"Sedentary"),
        (2,"Lightlyactive"),
        (3,"ModerativelyActive"),
        (4,"VeryActive"),
        (5,"ExtraActive")
    )

    activity_level=forms.ChoiceField(choices=choices)


class TemperatureForm(forms.Form):

    temp_in_deg=forms.IntegerField(required=False)

    temp_in_fh=forms.IntegerField(required=False)


class BmiForm(forms.Form):

    height=forms.IntegerField()

    weight=forms.IntegerField()

    def clean(self):

        print("cleaning")
        
        cleaned_data=super().clean()

        height=cleaned_data.get("height")

        print(height)

        if int(height) > 200:

            self.add_error("height","invalid height")

