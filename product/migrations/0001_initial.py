# Generated by Django 4.2.7 on 2023-12-04 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('slug', models.SlugField()),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subs', to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('img', models.ImageField(null=True, upload_to='images')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('review', models.IntegerField(default=0)),
                ('category', models.ManyToManyField(blank=True, related_name='catt', to='product.category')),
                ('color', models.ManyToManyField(related_name='products', to='product.color')),
                ('size', models.ManyToManyField(blank=True, related_name='products', to='product.size')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Information_1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='informations', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='AttributeMain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributs', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='AttributDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('attribute_main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributsdetaill', to='product.attributemain')),
            ],
        ),
    ]
