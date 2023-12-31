# Generated by Django 4.2.2 on 2023-07-09 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Salary', models.IntegerField(default=0)),
                ('Bonus', models.IntegerField(default=0)),
                ('Phone', models.IntegerField(default=0)),
                ('DOJ', models.DateField()),
                ('Dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_app.department')),
                ('Desg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_app.designation')),
            ],
        ),
    ]
