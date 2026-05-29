"""Vercel build script: apply database migrations before deploy."""

import os


def main():
    if not os.environ.get('DATABASE_URL'):
        print('DATABASE_URL not set; skipping migrations.')
        return

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_system.settings')

    import django

    django.setup()

    from django.core.management import call_command

    call_command('migrate', '--noinput', verbosity=1)
    print('Database migrations applied successfully.')


if __name__ == '__main__':
    main()
