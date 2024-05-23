# Generated by Django 5.0.4 on 2024-05-23 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCV', '0002_rename_generalsettings_generalsetting'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', help_text='This is variable of setting.', max_length=254, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=254, verbose_name='Description')),
                ('file', models.ImageField(blank=True, default='', upload_to='images/', verbose_name='')),
            ],
        ),
        migrations.AlterModelOptions(
            name='generalsetting',
            options={'ordering': ('name',), 'verbose_name': 'General Setting', 'verbose_name_plural': 'General Settings'},
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='description',
            field=models.CharField(blank=True, default='', max_length=254, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='name',
            field=models.CharField(blank=True, default='', help_text='This is variable of setting.', max_length=254, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='parameters',
            field=models.CharField(blank=True, default='', max_length=254, verbose_name='Parameters'),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
    ]
