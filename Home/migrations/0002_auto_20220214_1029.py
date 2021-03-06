# Generated by Django 3.2.7 on 2022-02-14 18:29

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=froala_editor.fields.FroalaField(),
        ),
    ]
