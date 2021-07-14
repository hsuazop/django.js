# -*- coding: utf-8 -*-

from djangojs.context_serializer import ContextSerializer


class SocialAuthContextMixin(object):
    '''Handle django_social_auth context specifics'''
    def process_social_auth(self, social_auth, data):
        """ Just force social_auth's LazyDict to be converted to a dict for the
            JSON serialization to work properly. """

        data['social_auth'] = dict(social_auth.items())


class SocialAuthContextSerializer(SocialAuthContextMixin, ContextSerializer):
    '''Already packed django_social_auth ContextSerializer'''
    pass
