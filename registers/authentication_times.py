from rest_framework.authentication import TokenAuthentication

from rest_framework.exceptions import AuthenticationFailed

from django.conf import settings

from django.utils import timezone

from datetime import timedelta

class ExpiringTokenAuthentication(TokenAuthentication):

    def expires_in(self,token):
        time_elapsed = timezone.now() - token.created
        left_time = timedelta(seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed
        return left_time

    def is_token_expired(self,token):
        return self.expires_in(token) < timedelta(seconds=0)

    def token_expire_handler(self,token):

        is_expire = self.is_token_expired(token)

        if is_expire:
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user = user)

        return token

    def authenticate_credentials(self, key):
        user = None,None
        try:
            token = self.get_model().objects.select_related('user').get(key=key)
            token = self.token_expire_handler(token)
            user = token.user
        except self.get_model().DoesNotExist:
            pass

        return user
