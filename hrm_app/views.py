from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Department,User,Role
from .forms import DepartmentForm, RoleForm,UserForm

def dashboard(request):
    return render(request, 'dashboard.html')



def department(request):
    departments = Department.objects.all()
    for department in departments:
        department.status_text = "Active" if department.status else "Inactive"
    return render(request, 'Department.html', {'departments': departments})

def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Department added successfully!")
            return redirect('/department')
    else:
        form = DepartmentForm()
    return render(request, 'add_department.html', {'form': form})






# Update Department View
def update_department(request, dept_id):
    department = get_object_or_404(Department, pk=dept_id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, "Department updated successfully!")
            return redirect('/department')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'update_department.html', {'form': form, 'department': department})

# Delete Department (Soft Delete)
def delete_department(request, dept_id):
    department = get_object_or_404(Department, pk=dept_id)
    if request.method == 'POST':
        department.status = False  # Mark as inactive
        department.save()
        messages.warning(request, "Department marked as inactive. Please reassign employees.")
        return redirect('/department')
    return render(request, 'delete_department.html', {'department': department})

def upcoming_events(request):
    return render(request, 'upcoming_events.html')


def roless(request):
    roles = Role.objects.all()
    return render(request, 'roles.html',{'roles':roles})

# Add Role View
def add_role(request): 
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Role added successfully!")
            return redirect('roless')  # Use the named URL
    else:
        form = RoleForm()
    return render(request, 'add_role.html', {'form': form})


# Update Role View
def update_role(request, role_id):
    role = get_object_or_404(Role, pk=role_id)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            messages.success(request, "Role updated successfully!")
            return redirect('roless')  # Redirect to the roles page
    else:
        form = RoleForm(instance=role)
    return render(request, 'update_role.html', {'form': form, 'role': role})

# Delete Role View
def delete_role(request, role_id):
    role = get_object_or_404(Role, pk=role_id)
    if request.method == 'POST':
        role.status = False  # Mark as inactive
        role.save()
        messages.warning(request, "Role marked as inactive.")
        return redirect('/roles')
    return render(request, 'delete_role.html', {'role': role})


def employee(request):
    users = User.objects.select_related('role_id', 'dept_id', 'reporting_manager_id').all()

    for user in users:
        user.status_text = "Active" if user.is_active else "Inactive"
        user.role_id_text = user.role_id.role_name if user.role_id else "No Role Assigned"
        user.department_text = user.dept_id.dept_name if user.dept_id else "No Department Assigned"
        user.reporting_manager_text = f"{user.reporting_manager_id.first_name} {user.reporting_manager_id.last_name}" if user.reporting_manager_id else "No Reporting Manager"

    return render(request, 'employee.html', {'users': users})


def add_employee(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully!")
            return redirect('/employee')
    else:
        form = UserForm()
    return render(request, 'add_employee.html', {'form': form})

# Update Employee View
def update_employee(request, employee_id):
    user = get_object_or_404(User, pk=employee_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee Details updated successfully!")
            return redirect('/employee')
    else:
        form = UserForm(instance=user)
    return render(request, 'update_employee.html', {'form': form, 'user': user})

def delete_employee(request, employee_id):
    user = get_object_or_404(User, pk=employee_id)
    if request.method == 'POST':
        user.is_active = False  # Mark as inactive
        user.save()
        messages.warning(request, "Employee marked as inactive.")
        return redirect('/employee')
    return render(request, 'delete_employee.html', {'user': user})