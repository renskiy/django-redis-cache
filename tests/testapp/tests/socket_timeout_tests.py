# -*- coding: utf-8 -*-
try:
    from django.test import override_settings
except ImportError:
    from django.test.utils import override_settings
from django.test import TestCase

from redis.exceptions import ConnectionError
from tests.testapp.tests.base_tests import SetupMixin

LOCATION = "127.0.0.1:6382"


@override_settings(
    CACHES={
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': LOCATION,
            'OPTIONS': {
                'DB': 15,
                'PASSWORD': 'yadayada',
                'PARSER_CLASS': 'redis.connection.HiredisParser',
                'PICKLE_VERSION': -1,
                'SOCKET_TIMEOUT': 0,
            },
        },
    }
)
class SocketTimeoutTestCase(SetupMixin, TestCase):

    def tearDown(self):
        pass

    def test_socket_timeout(self):
        self.reset_pool()
        cache = self.get_cache()
        with self.assertRaises(ConnectionError):
            cache.set('aaaaa', 'a')
