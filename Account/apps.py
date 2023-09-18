from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Account'

    def ready(self) -> None:
        import Account.signals
        return super().ready()