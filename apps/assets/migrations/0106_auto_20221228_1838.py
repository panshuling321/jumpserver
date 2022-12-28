# Generated by Django 3.2.14 on 2022-12-28 10:38

import common.db.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0105_auto_20221220_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetBaseAutomation',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=128, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('org_id',
                 models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('is_periodic', models.BooleanField(default=False, verbose_name='Periodic perform')),
                ('interval', models.IntegerField(blank=True, default=24, null=True, verbose_name='Cycle perform')),
                ('crontab', models.CharField(blank=True, max_length=128, null=True, verbose_name='Regularly perform')),
                ('type', models.CharField(max_length=16, verbose_name='Type')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
            ],
            options={
                'verbose_name': 'Asset automation task',
            },
        ),
        migrations.CreateModel(
            name='AutomationExecution',
            fields=[
                ('org_id',
                 models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('status', models.CharField(default='pending', max_length=16, verbose_name='Status')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('date_start', models.DateTimeField(db_index=True, null=True, verbose_name='Date start')),
                ('date_finished', models.DateTimeField(null=True, verbose_name='Date finished')),
                ('snapshot', common.db.fields.EncryptJsonDictTextField(blank=True, default=dict, null=True,
                                                                       verbose_name='Automation snapshot')),
                ('trigger', models.CharField(choices=[('manual', 'Manual trigger'), ('timing', 'Timing trigger')],
                                             default='manual', max_length=128, verbose_name='Trigger mode')),
                ('automation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='executions',
                                                 to='assets.assetbaseautomation', verbose_name='Automation task')),
            ],
            options={
                'verbose_name': 'Automation task execution',
            },
        ),
        migrations.RemoveField(
            model_name='accountbackupplanexecution',
            name='plan',
        ),
        migrations.AlterUniqueTogether(
            name='commandfilter',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='commandfilter',
            name='assets',
        ),
        migrations.RemoveField(
            model_name='commandfilter',
            name='nodes',
        ),
        migrations.RemoveField(
            model_name='commandfilter',
            name='user_groups',
        ),
        migrations.RemoveField(
            model_name='commandfilter',
            name='users',
        ),
        migrations.RemoveField(
            model_name='commandfilterrule',
            name='filter',
        ),
        migrations.RemoveField(
            model_name='commandfilterrule',
            name='reviewers',
        ),
        migrations.RemoveField(
            model_name='gathereduser',
            name='asset',
        ),
        migrations.AlterModelOptions(
            name='asset',
            options={'ordering': ['name'],
                     'permissions': [('refresh_assethardwareinfo', 'Can refresh asset hardware info'),
                                     ('test_assetconnectivity', 'Can test asset connectivity'),
                                     ('push_assetaccount', 'Can push account to asset'),
                                     ('match_asset', 'Can match asset'), ('add_assettonode', 'Add asset to node'),
                                     ('move_assettonode', 'Move asset to node')], 'verbose_name': 'Asset'},
        ),
        migrations.CreateModel(
            name='GatherFactsAutomation',
            fields=[
                ('assetbaseautomation_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='assets.assetbaseautomation')),
            ],
            options={
                'verbose_name': 'Gather asset facts',
            },
            bases=('assets.assetbaseautomation',),
        ),
        migrations.CreateModel(
            name='PingAutomation',
            fields=[
                ('assetbaseautomation_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='assets.assetbaseautomation')),
            ],
            options={
                'verbose_name': 'Ping asset',
            },
            bases=('assets.assetbaseautomation',),
        ),
        migrations.AddField(
            model_name='assetbaseautomation',
            name='assets',
            field=models.ManyToManyField(blank=True, to='assets.Asset', verbose_name='Assets'),
        ),
        migrations.AddField(
            model_name='assetbaseautomation',
            name='nodes',
            field=models.ManyToManyField(blank=True, to='assets.Node', verbose_name='Nodes'),
        ),
    ]
