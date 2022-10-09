import re
from rest_framework import serializers


def is_matching(mail):
    match = re.match("^[a-z]+[.][a-z]+@student[.]guc[.]edu[.]eg$", mail)
    return (len(mail) <= 254) and bool(match)


def is_guc_mail(value):
    if not is_matching(value):
        raise serializers.ValidationError('Invalid GUCmail')


class MailSerializer(serializers.Serializer):
    mail = serializers.CharField(validators=[is_guc_mail])
