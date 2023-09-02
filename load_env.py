import environ
from pathlib import Path

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = Path(__file__).resolve().parent

# Take environment variables from .env file
environ.Env.read_env(BASE_DIR.joinpath('.env'))

DJANGO_SETTINGS_MODULE = env('DJANGO_SETTINGS_MODULE', default='app.config.settings.dev')

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

# CACHES = {
#     # Read os.environ['CACHE_URL'] and raises
#     # ImproperlyConfigured exception if not found.
#     #
#     # The cache() method is an alias for cache_url().
#     'default': env.cache(),

#     # read os.environ['REDIS_URL']
#     'redis': env.cache_url('REDIS_URL')
# }