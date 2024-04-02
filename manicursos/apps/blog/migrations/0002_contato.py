# Generated by Django 5.0.3 on 2024-04-02 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.IntegerField(choices=[(1, 'Reclamação'), (2, 'Dúvidas'), (3, 'Critica'), (4, 'Ajuda'), (5, 'Outro')])),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('mensagem', models.TextField()),
            ],
        ),
    ]