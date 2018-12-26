# Generated by Django 2.1 on 2018-09-18 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True)),
                ('position', models.PositiveSmallIntegerField(default=0)),
                ('visible_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True)),
                ('rating', models.PositiveSmallIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('present_date', models.DateTimeField(auto_now_add=True)),
                ('main_img', models.ImageField(upload_to='product_image')),
                ('left_img', models.ImageField(upload_to='product_image')),
                ('middle_img', models.ImageField(upload_to='product_image')),
                ('right_img', models.ImageField(upload_to='product_image')),
                ('description', models.TextField()),
                ('short_description', models.CharField(max_length=150)),
                ('count_size_s', models.PositiveSmallIntegerField()),
                ('count_size_m', models.PositiveSmallIntegerField(verbose_name=models.PositiveSmallIntegerField())),
                ('count_size_l', models.PositiveSmallIntegerField(verbose_name=models.PositiveSmallIntegerField())),
            ],
        ),
        migrations.CreateModel(
            name='ProductSex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, unique=True)),
                ('position', models.PositiveSmallIntegerField(default=0)),
                ('visible_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16, unique=True)),
                ('position', models.PositiveSmallIntegerField(default=0)),
                ('visible_name', models.CharField(max_length=32)),
                ('parrent_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductCategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSubSubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True)),
                ('position', models.PositiveSmallIntegerField(default=0)),
                ('visible_name', models.CharField(max_length=32)),
                ('parent_sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductSubCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='productitem',
            name='sub_sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductSubSubCategory'),
        ),
        migrations.AddField(
            model_name='productitem',
            name='tags',
            field=models.ManyToManyField(to='mainapp.Tags'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='sex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductSex'),
        ),
    ]