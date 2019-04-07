# Generated by Django 2.1.7 on 2019-04-07 07:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid5, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('attachment', models.FileField(upload_to='attachments/')),
            ],
        ),
    ]
