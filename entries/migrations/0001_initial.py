# Generated by Django 3.2.25 on 2024-04-11 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallDataInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_id', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_name', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_comment', models.TextField(blank=True, null=True)),
                ('lead_post', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_city', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_business', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_homepage', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_emails', models.JSONField(blank=True, default=list, null=True)),
                ('lead_inn', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_kpp', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_created_at', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_updated_at', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_deleted_at', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_parent_lead_id', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_tags', models.JSONField(blank=True, default=list, null=True)),
                ('lead_phones', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_id', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_comment', models.TextField(blank=True, null=True)),
                ('contact_post', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_city', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_business', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_homepage', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_emails', models.JSONField(blank=True, default=list, null=True)),
                ('contact_inn', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_kpp', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_created_at', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_updated_at', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_deleted_at', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_parent_lead_id', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_tags', models.JSONField(blank=True, default=list, null=True)),
                ('contact_address', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_phones', models.CharField(blank=True, max_length=255, null=True)),
                ('call_id', models.CharField(blank=True, max_length=255, null=True)),
                ('call_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('call_source', models.CharField(blank=True, max_length=255, null=True)),
                ('call_direction', models.CharField(blank=True, max_length=255, null=True)),
                ('call_params', models.JSONField(blank=True, default=dict, null=True)),
                ('call_lead_id', models.CharField(blank=True, max_length=255, null=True)),
                ('call_organization_id', models.CharField(blank=True, max_length=255, null=True)),
                ('call_user_id', models.CharField(blank=True, max_length=255, null=True)),
                ('call_started_at', models.CharField(blank=True, max_length=255, null=True)),
                ('call_connected_at', models.CharField(blank=True, max_length=255, null=True)),
                ('call_ended_at', models.CharField(blank=True, max_length=255, null=True)),
                ('call_reason', models.CharField(blank=True, max_length=255, null=True)),
                ('call_duration', models.IntegerField(blank=True, null=True)),
                ('call_scenario_id', models.CharField(blank=True, max_length=255, null=True)),
                ('call_result_id', models.CharField(blank=True, max_length=255, null=True)),
                ('call_incoming_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('call_recording_url', models.URLField(blank=True, null=True)),
                ('call_call_type', models.CharField(blank=True, max_length=255, null=True)),
                ('call_region', models.CharField(blank=True, max_length=255, null=True)),
                ('call_local_time', models.CharField(blank=True, max_length=255, null=True)),
                ('call_call_project_id', models.CharField(blank=True, max_length=255, null=True)),
                ('call_call_project_title', models.CharField(blank=True, max_length=255, null=True)),
                ('call_scenario_result_group_id', models.CharField(blank=True, max_length=255, null=True)),
                ('call_scenario_result_group_title', models.CharField(blank=True, max_length=255, null=True)),
                ('call_result_result_id', models.CharField(blank=True, max_length=255, null=True)),
                ('call_result_result_name', models.CharField(blank=True, max_length=255, null=True)),
                ('call_result_comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FieldIds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bitrix_field_name', models.CharField(max_length=255)),
                ('bitrix_field_id', models.IntegerField()),
                ('bitrix_field_value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FormFieldIds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_id', models.CharField(max_length=255)),
                ('field_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FormResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_id', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_name', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_comment', models.TextField(blank=True, null=True)),
                ('lead_post', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_city', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_business', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_homepage', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_emails', models.JSONField(blank=True, default=list, null=True)),
                ('lead_inn', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_kpp', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_created_at', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_updated_at', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_deleted_at', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_parent_lead_id', models.CharField(blank=True, max_length=255, null=True)),
                ('lead_tags', models.JSONField(blank=True, default=list, null=True)),
                ('lead_phones', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_id', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_comment', models.TextField(blank=True, null=True)),
                ('contact_post', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_city', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_business', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_homepage', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_emails', models.JSONField(blank=True, default=list, null=True)),
                ('contact_inn', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_kpp', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_created_at', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_updated_at', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_deleted_at', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_parent_lead_id', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_tags', models.JSONField(blank=True, default=list, null=True)),
                ('contact_address', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_phones', models.CharField(blank=True, max_length=255, null=True)),
                ('call_id', models.CharField(blank=True, max_length=255, null=True)),
                ('call_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('call_source', models.CharField(blank=True, max_length=255, null=True)),
                ('call_direction', models.CharField(blank=True, max_length=255, null=True)),
                ('call_params', models.JSONField(blank=True, default=dict, null=True)),
                ('call_lead_id', models.CharField(blank=True, max_length=255, null=True)),
                ('call_organization_id', models.CharField(blank=True, max_length=255, null=True)),
                ('call_user_id', models.CharField(blank=True, max_length=255, null=True)),
                ('call_started_at', models.CharField(blank=True, max_length=255, null=True)),
                ('call_connected_at', models.CharField(blank=True, max_length=255, null=True)),
                ('call_ended_at', models.CharField(blank=True, max_length=255, null=True)),
                ('call_reason', models.CharField(blank=True, max_length=255, null=True)),
                ('call_duration', models.IntegerField(blank=True, null=True)),
                ('call_scenario_id', models.CharField(blank=True, max_length=255, null=True)),
                ('call_result_id', models.CharField(blank=True, max_length=255, null=True)),
                ('call_incoming_phone', models.CharField(blank=True, max_length=255, null=True)),
                ('call_recording_url', models.URLField(blank=True, null=True)),
                ('call_call_type', models.CharField(blank=True, max_length=255, null=True)),
                ('call_region', models.CharField(blank=True, max_length=255, null=True)),
                ('call_local_time', models.CharField(blank=True, max_length=255, null=True)),
                ('call_call_project_id', models.CharField(blank=True, max_length=255, null=True)),
                ('call_call_project_title', models.CharField(blank=True, max_length=255, null=True)),
                ('call_scenario_result_group_id', models.CharField(blank=True, max_length=255, null=True)),
                ('call_scenario_result_group_title', models.CharField(blank=True, max_length=255, null=True)),
                ('form_response', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IntegrationsData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('stage_id', models.CharField(max_length=255)),
                ('tg_bot_id', models.CharField(max_length=255)),
                ('google_spreadsheet_id', models.CharField(max_length=255)),
                ('sheet_name', models.CharField(max_length=255)),
                ('previous_sheet_names', models.CharField(blank=True, max_length=255)),
                ('skorozvon_scenario_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ScenarioIds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scenario_id', models.CharField(max_length=255)),
                ('scenario_name', models.CharField(max_length=255)),
            ],
        ),
    ]