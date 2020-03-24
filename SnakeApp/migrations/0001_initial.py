# Generated by Django 2.2 on 2020-03-24 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('length', models.IntegerField()),
                ('venomous', models.BooleanField(default=False)),
            ],
        ),
    ]
