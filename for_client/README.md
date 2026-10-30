# PSUSphere Client

This directory contains the pull-based client configuration for the published
PSUSphere Docker image.

## Run

```bash
docker compose pull
docker compose up -d
```

Open <http://localhost:8000/>.

The Compose file pulls `erlybird21/psusphere:latest`; it does not build from
source. If a `SECRET_KEY` is not supplied, the container generates one and
stores it in the named volume.

## Useful commands

```bash
docker compose ps
docker compose logs -f web
docker compose stop
docker compose start
docker compose down
```

To remove the isolated database and all container data:

```bash
docker compose down -v
```

This deletes the named volume and cannot be undone.

## Superuser

```bash
docker compose exec web python manage.py createsuperuser
```
