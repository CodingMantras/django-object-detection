# Generated by Django 3.2.12 on 2022-08-06 12:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import modelmanager.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MLModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date and Time')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modification Date and Time')),
                ('name', models.CharField(help_text='Name for the machine learning model', max_length=100, verbose_name='Name')),
                ('pth_file', models.FileField(help_text='Allowed extensions are: .pt, .pth', upload_to=modelmanager.models.model_upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pt', 'pth'])], verbose_name='Upload Model Pt/Pth File')),
                ('class_filename', models.CharField(help_text='Name for the class file', max_length=100, null=True, verbose_name='Class FileName')),
                ('class_file', models.FileField(help_text='Ml Model classes file. Allowed extensions are: .txt, .names, .yaml', upload_to=modelmanager.models.model_classfile_upload_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['txt', 'TXT', 'names', 'names', 'yaml', 'YAML'])], verbose_name='Ml Model Classes file')),
                ('description', models.TextField(verbose_name="Model's description")),
                ('version', models.CharField(blank=True, max_length=51, null=True, verbose_name='Ml Model Version')),
                ('public', models.BooleanField(default=False)),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mlmodels', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='mlmodel',
            constraint=models.UniqueConstraint(fields=('name', 'uploader'), name='unique_model_by_user'),
        ),
    ]
