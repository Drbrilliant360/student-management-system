from django import forms
from apps.student.models import Course
from apps.accounts.models import User


class CourseForm(forms.ModelForm):
    instructor = forms.ModelChoiceField(
        queryset=User.objects.filter(role='staff'),
        required=False,
        empty_label="Unassigned"
    )
    
    class Meta:
        model = Course
        fields = ['code', 'name', 'description', 'credits', 'instructor', 'is_active']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., CS101'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Course Description'}),
            'credits': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10}),
            'instructor': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
