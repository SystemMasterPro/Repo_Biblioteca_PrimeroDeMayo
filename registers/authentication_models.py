from rest_framework.authentication import get_authorization_header

from registers.authentication_times import ExpiringTokenAuthentication

from rest_framework.response import Response

from rest_framework.renderers import JSONRenderer

from rest_framework import status

class Authenticate(object):

    user = None

    def get_user(self,request):
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
            except:
                return None
            token_expire = ExpiringTokenAuthentication()
            user = token_expire.authenticate_credentials(token)
            if user != None:
                self.user = user
                return user
        return None

    def dispatch(self, request, *args, **kwargs):
        
        user = self.get_user(request)

        if user is not None:

            # if type(user) == str:
            #     response = Response(
            #         {'error': user, 'expired': self.user_token_expired}, status=status.HTTP_400_BAD_REQUEST)
            #     response.accepted_renderer = JSONRenderer()
            #     response.accepted_media_type = 'application/json'
            #     response.renderer_context = {}
            #     return response

            # if not self.user_token_expired:
            return super().dispatch(request, *args, **kwargs)

        response = Response({'error': 'No se han enviado las credenciales.'}, status=status.HTTP_400_BAD_REQUEST)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response

    
