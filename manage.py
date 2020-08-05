#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import sys

def _process_django_secret_key_file(filename):
    secret_key_encoding = "utf-8"
    try:
        with open(filename, encoding=secret_key_encoding) as f:
            secret_key = f.read()
    except FileNotFoundError:
        secret_key = _generate_random_printable_django_secret_key()
        with open(filename, "w", encoding=secret_key_encoding) as f:
            f.write(secret_key)
    return secret_key

def main():
    secret_key = _process_django_secret_key_file(
        os.path.expanduser("~/jawanndenn.secret_key")
    )

    os.environ["JAWANNDENN_SECRET_KEY"] = secret_key
    os.environ["JAWANNDENN_SQLITE_FILE"] = os.path.expanduser("~/jawanndenn.sqlite3")

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jawanndenn.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
