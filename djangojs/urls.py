# -*- coding: utf-8 -*-
import sys

from os.path import join, isdir

from django.urls import re_path
from django.views.i18n import JavaScriptCatalog
from djangojs.conf import settings
from djangojs.views import UrlsJsonView, ContextJsonView, JsInitView


def js_info_dict():
    js_info_dict = {
        'packages': [],
    }

    for app in settings.INSTALLED_APPS:
        if settings.JS_I18N_APPS and app not in settings.JS_I18N_APPS:
            continue
        if settings.JS_I18N_APPS_EXCLUDE and app in settings.JS_I18N_APPS_EXCLUDE:
            continue
        if app not in sys.modules:
            __import__(app)
        module = sys.modules[app]
        for path in module.__path__:
            if isdir(join(path, 'locale')):
                js_info_dict['packages'].append(app)
                break
    # Convert list to string for compatibility with django 4.2
    js_info_dict['packages'] = '+'.join(js_info_dict['packages'])
    return js_info_dict


urlpatterns = (
    re_path(r'^init\.js$', JsInitView.as_view(), name='django_js_init'),
    re_path(r'^urls$', UrlsJsonView.as_view(), name='django_js_urls'),
    re_path(r'^context$', ContextJsonView.as_view(), name='django_js_context'),
    re_path(r'^translation$', JavaScriptCatalog.as_view(), js_info_dict(), name='js_catalog'),
)
