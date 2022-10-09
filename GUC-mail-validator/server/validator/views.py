import imp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MailSerializer


class Validator(APIView):
    def post(self, request):
        serializer = MailSerializer(data=request.data)
        if (serializer.is_valid()):
            return Response(data={"Validity": "Valid GUCmail"}, status=status.HTTP_200_OK)
        return Response(data={"Validity": serializer.errors["mail"][0]}, status=status.HTTP_406_NOT_ACCEPTABLE)
