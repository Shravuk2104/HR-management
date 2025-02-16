# Generated by Django 5.1.5 on 2025-02-16 05:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm_app', '0006_performancereview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('leaveid', models.AutoField(primary_key=True, serialize=False)),
                ('leave_type', models.CharField(choices=[('SL', 'Sick Leave'), ('CL', 'Casual Leave'), ('PL', 'Privilege Leave'), ('LWP', 'Leave Without Pay')], max_length=10)),
                ('reason', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('total_days', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approver', to='hrm_app.user')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrm_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveQuota',
            fields=[
                ('quotaid', models.AutoField(primary_key=True, serialize=False)),
                ('leave_type', models.CharField(choices=[('SL', 'Sick Leave'), ('CL', 'Casual Leave'), ('PL', 'Privilege Leave'), ('LWP', 'Leave Without Pay')], max_length=10)),
                ('total_quota', models.IntegerField()),
                ('used_quota', models.IntegerField(default=0)),
                ('remain_quota', models.IntegerField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrm_app.user')),
            ],
        ),
    ]
