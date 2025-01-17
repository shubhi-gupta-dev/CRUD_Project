# Generated by Django 5.1.3 on 2024-11-15 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_student_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=60)),
                ('pdesc', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='myimage')),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
