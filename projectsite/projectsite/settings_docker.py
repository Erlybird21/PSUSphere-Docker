"""Docker-specific Django settings for PSUSphere.

The base settings are intentionally kept unchanged for the original
PythonAnywhere deployment. This module only overrides what is required to run
inside an isolated local container.
"""

import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured

from .settings import *  # noqa: F401,F403


def env_bool(name, default=False):
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


DEBUG = env_bool("DEBUG", True)

ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")
    if host.strip()
]
if not ALLOWED_HOSTS:
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

if not env_bool("USE_SQLITE", True):
    raise ImproperlyConfigured(
        "Docker settings require USE_SQLITE=true to keep the container database isolated."
    )

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.environ.get("SQLITE_PATH", "/data/db.sqlite3"),
    }
}

SECRET_KEY = os.environ.get("SECRET_KEY", "").strip()
if not SECRET_KEY:
    secret_key_file = Path(
        os.environ.get("SECRET_KEY_FILE", "/data/secret_key")
    )
    if secret_key_file.is_file():
        SECRET_KEY = secret_key_file.read_text(encoding="utf-8").strip()
if not SECRET_KEY:
    raise ImproperlyConfigured(
        "SECRET_KEY is not set and the configured SECRET_KEY_FILE does not exist."
    )

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

SITE_ID = 1
