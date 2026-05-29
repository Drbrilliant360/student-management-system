"""Vercel build script: collect static assets and apply migrations."""

import os


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_system.settings')

    import django

    django.setup()

    from django.core.management import call_command

    call_command('collectstatic', '--noinput', verbosity=1)
    print('Static files collected successfully.')

    if os.environ.get('DATABASE_URL'):
        call_command('migrate', '--noinput', verbosity=1)
        print('Database migrations applied successfully.')
    else:
        print('DATABASE_URL not set; skipping migrations.')


if __name__ == '__main__':
    main()
