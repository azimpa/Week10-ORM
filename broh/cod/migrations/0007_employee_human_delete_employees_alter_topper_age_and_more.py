# Generated by Django 4.2.3 on 2023-07-10 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cod', '0006_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Teacher Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, verbose_name='Gender')),
                ('age', models.IntegerField(verbose_name='Age')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
        migrations.AlterField(
            model_name='topper',
            name='age',
            field=models.IntegerField(verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='topper',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='topper',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='topper',
            name='name',
            field=models.CharField(max_length=15, verbose_name='Teacher Name'),
        ),
    ]