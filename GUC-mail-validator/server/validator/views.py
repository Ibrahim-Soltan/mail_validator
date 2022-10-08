import imp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Validator(APIView):
    def get(self, request):
        return Response(data={"message": "hello"}, status=status.HTTP_200_OK)
