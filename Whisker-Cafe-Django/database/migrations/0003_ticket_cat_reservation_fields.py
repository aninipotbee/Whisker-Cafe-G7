from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("database", "0002_loginthrottle_event_actor_ticket_assignee_and_more")]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="cat_name",
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name="ticket",
            name="guest_count",
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name="ticket",
            name="session_time",
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
