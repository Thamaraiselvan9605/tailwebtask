from django import forms
from django.core.exceptions import ValidationError
from .models import StudentsData


class StudentsDataForm(forms.ModelForm):
    class Meta:
        model = StudentsData
        fields = ['student_name', 'subject', 'marks']

    def clean_student_name(self):
        name = self.cleaned_data.get('student_name')
        if not name:
            raise ValidationError("Student name is required.")
        if len(name) < 3:
            raise ValidationError("Student name must be at least 3 characters.")
        return name

    def clean_subject(self):
        subject = self.cleaned_data.get('subject')
        if not subject:
            raise ValidationError("Subject is required.")
        return subject

    def clean_marks(self):
        marks = self.cleaned_data.get('marks')
        if marks is None:
            raise ValidationError("Marks are required.")
        if not isinstance(marks, int):
            raise ValidationError("Marks must be an integer.")
        if marks < 0 or marks > 100:
            raise ValidationError("Marks must be between 0 and 100.")
        return marks



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Username'})
    )
    password = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username.isalnum():
            raise ValidationError("Username should be alphanumeric.")
        if len(username) < 4:
            raise ValidationError("Username must be at least 4 characters.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6:
            raise ValidationError("Password must be at least 6 characters.")
        return password
