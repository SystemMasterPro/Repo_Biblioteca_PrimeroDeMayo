from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from rest_framework.authtoken.models import Token

from registers.serializers import UserTokenSerializer

from django.contrib.sessions.models import Session

from datetime import datetime

from registers.authentication_models import Authenticate



class UserToken(Authenticate, APIView):

    def get(self,request,*args,**kwargs):
        try:
            user_token = Token.objects.get(user=self.user)
            user = UserTokenSerializer(self.user)
            return Response({
                'token': user_token.key,
                'user': user.data 
            })
        except:
            return Response({'error':'Credenciales enviadas incorrectas'},status=status.HTTP_400_BAD_REQUEST)


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        login_serializer = self.serializer_class(data = request.data, context={'request': request})

        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']

            if user.user_active:
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)

                if created:
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio Exitoso'
                    }, status=status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(
                        expire_date_gte=datetime.now())

                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()

                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio Exitoso'
                    }, status=status.HTTP_201_CREATED)
                    # --> Utilizar esto cuando no querramos que se manejen por sesiones, para ello borramos el codigo anterior
                    # return Response({'error':'YA SE HA INICIADO SESION CON ESTE USUARIO'}, status=status.HTTP_409_CONFLICT) 
            else:
                return Response({'error': 'Este usuario esta suspendido'}, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response({'error': 'Usuario o contraseña no validos!'}, status=status.HTTP_400_BAD_REQUEST)

        # return Response({'mensaje': 'Hola desde Response'}, status=status.HTTP_200_OK)


class Logout(APIView):

    def post(self, request, *args, **kwargs):
        try:
            token = request.GET.get('token')
            print(token)
            token = Token.objects.filter(key = token).first()
            if token:
                print("TOKEN RECONOCIDO")
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()
                session_message = "Sesiones de usuario eliminadas."
                token_message = "Token eliminado."
                return Response({'token_message': token_message, 'session_message': session_message},
                            status=status.HTTP_200_OK)
            return Response({
            'error': 'No se ha encontrado el usuario con estas credenciales.'
            }, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({
                'error':'No se ha encontrado token en la peticion.'
            }, status = status.HTTP_409_CONFLICT)
