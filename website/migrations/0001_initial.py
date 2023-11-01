# Generated by Django 4.2.6 on 2023-10-30 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('publisher', models.CharField(max_length=90)),
                ('book_name', models.CharField(max_length=90)),
                ('class_name', models.CharField(max_length=90)),
                ('price', models.IntegerField(max_length=50)),
                ('quantity', models.IntegerField(max_length=50)),
                ('sales', models.IntegerField(max_length=50)),
                ('balance', models.IntegerField(max_length=50)),
            ],
        ),
    ]
