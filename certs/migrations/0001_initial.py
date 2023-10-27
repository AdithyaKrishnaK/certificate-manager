# Generated by Django 4.2.6 on 2023-10-27 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=255)),
                ('owner', models.EmailField(max_length=254)),
                ('expiry', models.DateField()),
                ('private_key', models.FileField(upload_to='uploads/private_keys')),
                ('certificate', models.FileField(upload_to='uploads/certs')),
            ],
        ),
        migrations.CreateModel(
            name='CertificateRenewal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]