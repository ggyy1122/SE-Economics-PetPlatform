from django.apps import AppConfig

class FavoritesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'favorites'

    def ready(self):
        # 导入信号处理函数
        import favorites.signals
