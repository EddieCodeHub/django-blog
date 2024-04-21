from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    app configuration for the blog app

    **Attributes**
    - default_auto_field: the default auto field for the app
    - name: the name of the app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
