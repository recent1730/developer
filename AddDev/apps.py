from django.apps import AppConfig


class AdddevConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AddDev'


    def ready(self):
        import AddDev.signals
