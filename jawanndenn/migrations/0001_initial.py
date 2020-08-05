import django.db.models.deletion
import django_extensions.db.fields
from django.db import migrations, models
from annoying.fields import AutoOneToOneField


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    apruebo, nulo, rechazo = "A", "N", "R"
    ALTERNATIVAS = [(apruebo, "Apruebo"), (nulo, "Nulo"), (rechazo, "Rechazo")]

    operations = [
        migrations.CreateModel(
            name="Poll",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        default=jawanndenn.models._get_random_sha256,
                        max_length=64,
                        unique=True,
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("equal_width", models.BooleanField(default=False)),
            ],
            options={
                "ordering": ("-modified", "-created"),
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PollOption",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.PositiveSmallIntegerField()),
                ("name", models.CharField(max_length=255)),
                (
                    "poll",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="options",
                        to="jawanndenn.Poll",
                    ),
                ),
            ],
            options={"unique_together": {("poll", "position")},},
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "user",
                    AutoOneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        to="jawanndenn.User",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ballot",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                ("voter_name", models.CharField(max_length=255)),
                (
                    "voter_user",
                    models.ForeignKey(
                        on_delete=models.CASCADE,
                        related_name="ballots",
                        to="jawanndenn.Profile",
                    ),
                ),
                (
                    "poll",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ballots",
                        to="jawanndenn.Poll",
                    ),
                ),
            ],
            options={
                "ordering": ("-modified", "-created"),
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Vote",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "choice",
                    models.CharField(max_length=2, choices=ALTERNATIVAS, default=nulo),
                ),
                (
                    "ballot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="votes",
                        to="jawanndenn.Ballot",
                    ),
                ),
                (
                    "option",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jawanndenn.PollOption",
                    ),
                ),
            ],
            options={"unique_together": {("ballot", "option")},},
        ),
"""         migrations.CreateModel(
            name="Consejo",
            fields=[
                ("nombre", models.CharField(max_length=50)),
                (
                    "miembros",
                    models.ManyToManyField(
                        to="jawanndenn.Profile", related_name="consejos"
                    ),
                ),
                ("futuros_miembros", models.TextField(editable=True, null=True)),
            ],
        ), """
    ]
