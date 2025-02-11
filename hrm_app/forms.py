from django import forms
from .models import Department,Role,User
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, UserCreationForm
from django.contrib.auth import get_user_model


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name', 'description']
        widgets = {
            'dept_name':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','rows':4}),
        }

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role_name', 'description']
        widgets = {
            'role_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'role_name': 'Role Name',
            'description': 'Description',
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email',
            'mobile', 'role', 'department', 'reporting_manager', 'date_of_joining','username','password'
        ]
        widgets = {
            
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(),  # Masked input for passwords
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_joining': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    role = forms.ModelChoiceField(
        queryset=Role.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Role"  # Optional: Placeholder for dropdown
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Department"  # Optional: Placeholder for dropdown
    )
    reporting_manager = forms.ModelChoiceField(
        queryset=User.objects.filter(is_active=True),  # Optional: Only active users
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,
        empty_label="Select Reporting Manager"  # Optional: Placeholder for dropdown
    )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=100, 
        required=True, 
        widget=forms.TextInput(attrs={'placeholder': 'Enter Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}), 
        required=True
    )

class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=100, 
        required=True, 
        widget=forms.EmailInput(attrs={'placeholder': 'Enter Registered Email'})
    )

class SetNewPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter New Password'}), 
        required=True
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm New Password'}), 
        required=True
    )

from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_title', 'task_description', 'task_priority', 'start_date', 'end_date', 'task_type']
        widgets = {
            'task_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
            'task_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter task description', 'rows': 3}),
            'task_priority': forms.Select(
                choices=[('', 'Select Task Priority')] + list(Task.PRIORITY_CHOICES),
                attrs={'class': 'form-control'}
            ),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'task_type': forms.Select(
                choices=[('', 'Select Task Type')] + list(Task.TASK_TYPE_CHOICES),
                attrs={'class': 'form-control'}
            ),
        }


