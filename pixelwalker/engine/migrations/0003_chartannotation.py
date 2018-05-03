# Generated by Django 2.0.1 on 2018-02-09 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0002_auto_20180208_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartAnnotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='Empty annotation', max_length=280)),
                ('display_type', models.IntegerField(choices=[(0, 'average'), (1, 'all_frames')], default=0)),
                ('group_by', models.IntegerField(choices=[(0, 'encoded_variant'), (1, 'definition'), (2, 'encoding_provider')], default=0)),
                ('assessment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='engine.Assessment')),
                ('metric_list', models.ManyToManyField(related_name='metric_list', to='engine.TaskType')),
            ],
        ),
    ]
