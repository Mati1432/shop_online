import json

from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.template.loader import render_to_string

from core.models import SettingsMail, Mail
import requests
from mailerlite import MailerLiteApi

from project import settings


def create_and_send_newsletter(mail):  # noqa D103
    mail_settings = SettingsMail.objects.get()

    api_key = mail_settings.api_key

    api = MailerLiteApi(api_key)

    headers = {
        'content-type': 'application/json',
        'x-mailerlite-apikey': f'{mail_settings.api_key}',
    }

    value_list = []
    values = {
        'email': str(mail),
    }

    api.subscribers.create(values)
    group = api.groups.create(mail_settings.name_group)
    value_list.append(values)
    url = f'https://api.mailerlite.com/api/v2/groups/{group.id}/subscribers'

    for data in value_list:
        payload = json.dumps(data)
        requests.request('POST', url, data=payload, headers=headers)

    cam = {'subject': mail_settings.title,
           'name': mail_settings.name_campaign,
           'groups': [group.id],
           'type': 'regular'}

    campaign = api.campaigns.create(cam)
    context = {
        'content': mail_settings.content,
        'title': mail_settings.title,
        'unsubscribe': '\"{$unsubscribe}\"',
    }

    required_footer = render_to_string('mailerlite_template.html', context)

    html = required_footer

    plain = 'Your email client does not support HTML emails. '
    plain += 'Open newsletter here: {$url}. If you do not want'
    plain += ' to receive emails from us, click here: {$unsubscribe}'

    api.campaigns.update(campaign[1]['id'], html=html, plain=plain)

    url = f"https://api.mailerlite.com/api/v2/campaigns/{campaign[1]['id']}/actions/send"
    if not Mail.objects.filter(email=mail).exists():
        return requests.request('POST', url, headers=headers)
    else:
        send_mail_password(mail)
        raise ValidationError(message='you are currently in our newsletter.')


def send_mail_password(email):  # noqa D103
    send_mail(
        'Newsleter',
        'You are currently subscribed to our newsletter',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
