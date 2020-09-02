from django.forms import Form, CharField, Textarea


class VacancyCreateForm(Form):
    description = CharField(max_length=1024, widget=Textarea)
