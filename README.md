# Django/create-react-app integration

This project is an example of binding a **Django 2** back-end with a **create-react-app** client view.

## Setup and run

1.  Install **package dependencies**: `apt-get install python3-django stunnel4`
1.  Install **python dependencies**: `pip3 install python3-django pipenv`
1.  Clone repo: `git clone https://github.com/marksmall/djangoreact.git`
1.  `cd djangoreact`
1.  Enter virtual environment: `pipenv shell`
1.  Install python deps: `pipenv install`
1.  Install client deps: `cd client && yarn install && yarn build && cd ..`
1.  Migrate models: `$PROJ_ROOT/manage.py migrations`
1.  Start servers: `,/https.sh`

**NOTE:** Only install `stunnel4` if you want to test using **HTTPS** by running `$PROJ_ROOT/https.sh`. Otherwise, start django as normal: `$PROJ_ROOT/manage.py runserver`.

## Files of interest

### settings.py

Change the `DIRS` line of `TEMPLATES`, so the correct `index.html` (in `build` directory) is used in the `TemplateView`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'client/build')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Add `STATICFILES_DIRS` list so the correct client assets are used (add other directories if assets needed for other django apps):

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'client/build/static')
]
```

### views.py

Add new `TemplateView` to refer to the `build` directory `index.html` file:

```python
from django.views.generic import TemplateView


class FrontendAppView(TemplateView):
    template_name = 'index.html'
```

### urls.py

Add a new catch-all pattern:

```python
re_path('.*', TemplateView.as_view(template_name='index.html')),
```

**NOTE:** This must come after all other views, so routing on the client-side (via react-router, although not implemented) can work.
