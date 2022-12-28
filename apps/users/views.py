from django.contrib.sessions.models import Session
from django.utils.timezone import make_aware
from datetime import datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from apps.users.models import User
from apps.users.authentication_mixins import Authentication
from apps.users.api.serializers.serializers import UserTokenSerializer


class RefreshToken(Authentication,APIView):

	def get(self, *args, **kwargs):
		print(self.user)
		try:
			token_user,_ = Token.objects.get_or_create(user = self.user)
			user = UserTokenSerializer(token_user.user)
			return Response({'token':token_user.key, 'user': user.data}, status = status.HTTP_200_OK)
		except:
			return Response({'error': 'Credenciales enivadas incorrectamente'}, status = status.HTTP_400_BAD_REQUEST)


class Login(ObtainAuthToken):

	def post(self, request, *args, **kwargs):
		login_serialize = self.serializer_class(data = request.data, context = {'request':request})
		if login_serialize.is_valid():
			print(login_serialize.validated_data['user'])
			user = login_serialize.validated_data['user']
			if user.is_active:
				token, created =  Token.objects.get_or_create(user = user)
				user_serializer = UserTokenSerializer(user)
				if created:
					return Response({
						'token': token.key,
						'user': user_serializer.data,
						'message':'Inicio de sesión exitoso'
						}, status = status.HTTP_200_OK)
				else:
					
					"""
					token.delete()
					token = Token.objects.create(user = user)
					return Response({
						'token': token.key,
						'user': user_serializer.data,
						'message':'Inicio de sesión exitoso'
					}, status = status.HTTP_200_OK)"""
					return Response({'error':'Ya se ha iniciado sesión con este usuario'}, status = status.HTTP_409_CONFLICT)
			else:
				return Response({'error':'Este usuario no puede iniciar sesión'}, status = status.HTTP_401_UNAUTHORIZED)
		else:
			return Response({'error':'Nombre de usuario o contraseña incorrecta'}, status = status.HTTP_400_BAD_REQUEST)


class Logout(APIView):

	def post(self, request, *args, **kwargs):
		try:
			token = request.data.get('token')
			print(token)
			token = Token.objects.filter(key = token).first()

			if token:
				user = token.user
				all_sessions = Session.objects.filter(expire_date__gte = make_aware(datetime.now()))
				if all_sessions.exists():
					for session in all_sessions:
						session_data = session.get_decoded()
						if user.id == int(session_data.get('_auth_user_id')):
							session.delete()
				token.delete()
				token_message = "Token eliminado"
				return Response({'token_message':token_message}, status = status.HTTP_200_OK)
			return Response({'error':'No se ha encontrado un usuario con estas credenciales'},status = status.HTTP_400_BAD_REQUEST)

		except:
			return Response({'error':'No se ha encontrado un token en la peticion'},status = status.HTTP_409_CONFLICT)