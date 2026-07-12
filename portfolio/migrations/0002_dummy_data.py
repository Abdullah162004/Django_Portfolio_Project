from django.db import migrations


def add_dummy_data(apps, schema_editor):
    Skill = apps.get_model('portfolio', 'Skill')
    Project = apps.get_model('portfolio', 'Project')

    Skill.objects.create(name='HTML', level=90)
    Skill.objects.create(name='CSS', level=85)
    Skill.objects.create(name='Python', level=80)
    Skill.objects.create(name='Django', level=75)
    Skill.objects.create(name='SQLite', level=70)
    Skill.objects.create(name='Bootstrap', level=65)

    Project.objects.create(
        title='Portfolio Website',
        description='A personal portfolio website built with Django, featuring a home page, projects page, and a working contact form.',
        technology='Django, HTML, CSS, SQLite',
        project_link='https://github.com/'
    )
    Project.objects.create(
        title='Calculator App',
        description='A simple calculator web application that performs basic arithmetic operations.',
        technology='Python, Django',
        project_link='https://github.com/'
    )
    Project.objects.create(
        title='Blog Website',
        description='A blog platform where users can read and browse articles stored in a database.',
        technology='Django, SQLite, Bootstrap',
        project_link='https://github.com/'
    )


def remove_dummy_data(apps, schema_editor):
    Skill = apps.get_model('portfolio', 'Skill')
    Project = apps.get_model('portfolio', 'Project')
    Skill.objects.all().delete()
    Project.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_dummy_data, remove_dummy_data),
    ]
