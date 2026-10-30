#!/bin/sh
set -eu

mkdir -p /data

if [ -z "${SECRET_KEY:-}" ]; then
    SECRET_KEY_FILE="${SECRET_KEY_FILE:-/data/secret_key}"
    if [ ! -s "$SECRET_KEY_FILE" ]; then
        python -c "import secrets; print(secrets.token_urlsafe(50))" > "$SECRET_KEY_FILE"
    fi
    SECRET_KEY="$(cat "$SECRET_KEY_FILE")"
    export SECRET_KEY
fi

python manage.py migrate --noinput

exec "$@"
