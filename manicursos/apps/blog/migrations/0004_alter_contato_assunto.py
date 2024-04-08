# Generated by Django 5.0.3 on 2024-04-08 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_contato_assunto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='assunto',
            field=models.CharField(choices=[('rec', 'Reclamação'), ('duv', 'Dúvidas'), ('cri', 'Critica'), ('aju', 'Ajuda'), ('out', 'Outro')], default='rec', max_length=3),
        ),
    ]