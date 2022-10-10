import re
from rest_framework import serializers


def is_matching(mail):
    # Check if the mail passed matches the Regex of a GUC mail.
    match = re.match("^[a-z]+[.][a-z]+@student[.]guc[.]edu[.]eg$", mail)
    # Return true if the mail matches the pattern and is composed < 254 characters.
    return (len(mail) <= 254) and bool(match)


def is_guc_mail(value):
    # If the mail is not valid raise error with adequate message.
    if not is_matching(value):
        raise serializers.ValidationError('Invalid GUCmail')


class MailSerializer(serializers.Serializer):
    # Apply validation to the mail attribute.
    mail = serializers.CharField(validators=[is_guc_mail])
