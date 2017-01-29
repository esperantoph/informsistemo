from django.apps import AppConfig


class WebsiteConfig(AppConfig):
    name = 'informsistemo.website'
    verbose_name = "Website"

    def ready(self):
        """Override this to put in:
            Website system checks
            Website signal registration
        """
        pass
