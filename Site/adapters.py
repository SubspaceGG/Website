from allauth.exceptions import ImmediateHttpResponse
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth.models import User
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        return False

    def pre_social_login(self, request, sociallogin):
        if sociallogin.is_existing:
            return
        if 'email' not in sociallogin.account.extra_data:
            logger.info("'Email' field not in extra_data")
            raise ImmediateHttpResponse(HttpResponse('Email missing from social login - cannot verify user.'))
        try:
            email = sociallogin.account.extra_data['email'].lower()
            user = User.objects.get(email=email)

        except User.DoesNotExist:
            logger.info(f"User associated with {email} does not exist - preventing login.")
            raise ImmediateHttpResponse(HttpResponse('Must have pre-existing account for social login.'))

        sociallogin.connect(request, user)
