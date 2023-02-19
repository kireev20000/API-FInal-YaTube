WARNING: Running pip as root will break packages and permissions. You should install packages reliably by using venv: https://pip.pypa.io/warnings/venv
----------------------- Проверка flake8 пройдена -----------------------

Traceback (most recent call last):
  File "/usr/local/bin/pytest", line 8, in <module>
    sys.exit(console_main())
  File "/usr/local/lib/python3.7/site-packages/_pytest/config/__init__.py", line 185, in console_main
    code = main()
  File "/usr/local/lib/python3.7/site-packages/_pytest/config/__init__.py", line 143, in main
    config = _prepareconfig(args, plugins)
  File "/usr/local/lib/python3.7/site-packages/_pytest/config/__init__.py", line 319, in _prepareconfig
    pluginmanager=pluginmanager, args=args
  File "/usr/local/lib/python3.7/site-packages/pluggy/hooks.py", line 286, in __call__
    return self._hookexec(self, self.get_hookimpls(), kwargs)
  File "/usr/local/lib/python3.7/site-packages/pluggy/manager.py", line 93, in _hookexec
    return self._inner_hookexec(hook, methods, kwargs)
  File "/usr/local/lib/python3.7/site-packages/pluggy/manager.py", line 87, in <lambda>
    firstresult=hook.spec.opts.get("firstresult") if hook.spec else False,
  File "/usr/local/lib/python3.7/site-packages/pluggy/callers.py", line 203, in _multicall
    gen.send(outcome)
  File "/usr/local/lib/python3.7/site-packages/_pytest/helpconfig.py", line 100, in pytest_cmdline_parse
    config: Config = outcome.get_result()
  File "/usr/local/lib/python3.7/site-packages/pluggy/callers.py", line 80, in get_result
    raise ex[1].with_traceback(ex[2])
  File "/usr/local/lib/python3.7/site-packages/pluggy/callers.py", line 187, in _multicall
    res = hook_impl.function(*args)
  File "/usr/local/lib/python3.7/site-packages/_pytest/config/__init__.py", line 1003, in pytest_cmdline_parse
    self.parse(args)
  File "/usr/local/lib/python3.7/site-packages/_pytest/config/__init__.py", line 1283, in parse
    self._preparse(args, addopts=addopts)
  File "/usr/local/lib/python3.7/site-packages/_pytest/config/__init__.py", line 1192, in _preparse
    early_config=self, args=args, parser=self._parser
  File "/usr/local/lib/python3.7/site-packages/pluggy/hooks.py", line 286, in __call__
    return self._hookexec(self, self.get_hookimpls(), kwargs)
  File "/usr/local/lib/python3.7/site-packages/pluggy/manager.py", line 93, in _hookexec
    return self._inner_hookexec(hook, methods, kwargs)
  File "/usr/local/lib/python3.7/site-packages/pluggy/manager.py", line 87, in <lambda>
    firstresult=hook.spec.opts.get("firstresult") if hook.spec else False,
  File "/usr/local/lib/python3.7/site-packages/pluggy/callers.py", line 208, in _multicall
    return outcome.get_result()
  File "/usr/local/lib/python3.7/site-packages/pluggy/callers.py", line 80, in get_result
    raise ex[1].with_traceback(ex[2])
  File "/usr/local/lib/python3.7/site-packages/pluggy/callers.py", line 187, in _multicall
    res = hook_impl.function(*args)
  File "/usr/local/lib/python3.7/site-packages/pytest_django/plugin.py", line 349, in pytest_load_initial_conftests
    _setup_django()
  File "/usr/local/lib/python3.7/site-packages/pytest_django/plugin.py", line 235, in _setup_django
    django.setup()
  File "/usr/local/lib/python3.7/site-packages/django/__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "/usr/local/lib/python3.7/site-packages/django/apps/registry.py", line 91, in populate
    app_config = AppConfig.create(entry)
  File "/usr/local/lib/python3.7/site-packages/django/apps/config.py", line 224, in create
    import_module(entry)
  File "/usr/local/lib/python3.7/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1006, in _gcd_import
  File "<frozen importlib._bootstrap>", line 983, in _find_and_load
  File "<frozen importlib._bootstrap>", line 967, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 677, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 728, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/usr/local/lib/python3.7/site-packages/django_filters/__init__.py", line 4, in <module>
    from .filters import *
  File "/usr/local/lib/python3.7/site-packages/django_filters/filters.py", line 12, in <module>
    from .conf import settings
  File "/usr/local/lib/python3.7/site-packages/django_filters/conf.py", line 5, in <module>
    from .utils import deprecate
  File "/usr/local/lib/python3.7/site-packages/django_filters/utils.py", line 10, in <module>
    from django.db.models.fields import FieldDoesNotExist
ImportError: cannot import name 'FieldDoesNotExist' from 'django.db.models.fields' (/usr/local/lib/python3.7/site-packages/django/db/models/fields/__init__.py)