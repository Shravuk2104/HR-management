# Generated by Django 5.1.5 on 2025-02-14 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm_app', '0005_task_taskassignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerformanceReview',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('review_title', models.CharField(max_length=100)),
                ('review_date', models.DateField()),
                ('review_period', models.CharField(choices=[('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Annual', 'Annual')], max_length=100)),
                ('rating', models.IntegerField(default=1)),
                ('comments', models.CharField(blank=True, max_length=300, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='hrm_app.user')),
                ('reviewed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='given_reviews', to='hrm_app.user')),
            ],
        ),
    ]
