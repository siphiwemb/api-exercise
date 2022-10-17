# Generated by Django 3.1.4 on 2022-03-07 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Titanic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('survived', models.IntegerField(blank=True, db_column='Survived', null=True)),
                ('pclass', models.IntegerField(blank=True, db_column='Pclass', null=True)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('sex', models.TextField(blank=True, db_column='Sex', null=True)),
                ('age', models.IntegerField(blank=True, db_column='Age', null=True)),
                ('siblings_spousesaboard', models.IntegerField(blank=True, db_column='Siblings/SpousesAboard', null=True)),
                ('parents_childrenaboard', models.IntegerField(blank=True, db_column='Parents/ChildrenAboard', null=True)),
                ('fare', models.IntegerField(blank=True, db_column='Fare', null=True)),
            ],
            options={
                'db_table': 'titanic',
                'managed': False,
            },
        ),
    ]
