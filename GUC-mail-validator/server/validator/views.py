import imp
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MailSerializer


class Validator(APIView):
    # Post Endpoint:
    def post(self, request):
        # JSON data passed to serializer.
        serializer = MailSerializer(data=request.data)
        # Check if the mail is a valid GUC mail.
        if (serializer.is_valid()):
            return Response(data={"Validity": "Valid GUCmail"}, status=status.HTTP_200_OK)
        return Response(data={"Validity": serializer.errors["mail"][0]}, status=status.HTTP_406_NOT_ACCEPTABLE)
