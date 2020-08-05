from django.apps import AppConfig


class JawanndennConfig(AppConfig):
    name = "jawanndenn"
    verbose_name = "Jawandenn"

    def ready(self):
        import jawanndenn.signals  # noqa
