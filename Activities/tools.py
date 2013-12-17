from django.core.mail import send_mail

def send_email_to_who_commented(activity, new_comment_owner, old_comments):
    emails = list()
    for old_comment in old_comments:
        if not old_comment.owner.email in emails:
            emails.append(old_comment.owner.email)

    send_mail("[TogetherNetwork] New activity comment: %s" % activity.title,"""
Hi,
%s just left a comment on the activity you commented. 
Click on the link below to read all the comments:

http://www.togethernetwork.org%s

Thx
koala""" % (new_comment_owner.first_name, activity.get_absolute_url() ) ,
            'no-reply@togethernetwork.org', emails)
