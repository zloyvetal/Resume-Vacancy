from django.forms import Form, CharField, Textarea


class ResumeCreateForm(Form):
    description = CharField(max_length=1024, widget=Textarea)
