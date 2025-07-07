# core, signals.py:
from django.db.models.signals import m2m_changed, pre_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Event
from django.contrib.auth import get_user_model
from cloudinary.uploader import destroy


@receiver(m2m_changed, sender=Event.participants.through)
def send_participant_notification(sender, instance, action, pk_set, **kwargs):    
    # Send email notifications when participants are added or removed from events    
    if action in ['post_add', 'post_remove']:        
        User = get_user_model()
        users = User.objects.filter(pk__in=pk_set)
        
        for user in users:
            if user.email:  # Only send if user has an email
                if action == 'post_add':
                    # Send addition email
                    subject = f'You have been added to event: {instance.name}'
                    message = f'''Hello {user.first_name or user.username},
You have been added as a participant to the following event:

Event: {instance.name}
Description: {instance.description}
Date: {instance.date.strftime("%B %d, %Y")}
Time: {instance.time.strftime("%I:%M %p")}
Location: {instance.location}
Category: {instance.category.name}

Best regards,
Event Management Team'''
                    
                    try:
                        send_mail(
                            subject=subject,
                            message=message,
                            from_email=settings.DEFAULT_FROM_EMAIL,
                            recipient_list=[user.email],
                            fail_silently=False,
                        )
                        print(f"Addition email sent to {user.email} for event {instance.name}")
                    except Exception as e:
                        print(f"Failed to send addition email to {user.email}: {str(e)}")
                
                elif action == 'post_remove':
                    # Send removal email
                    subject = f'You have been removed from event: {instance.name}'
                    message = f'''Hello {user.first_name or user.username},
You have been removed from the following event:
Event: {instance.name}
Description: {instance.description}
Date: {instance.date.strftime("%B %d, %Y")}
Time: {instance.time.strftime("%I:%M %p")}
Location: {instance.location}
Category: {instance.category.name}
If you believe this was done in error, please contact the event organizer.
Best regards,
Event Management Team'''
                    
                    try:
                        send_mail(
                            subject=subject,
                            message=message,
                            from_email=settings.DEFAULT_FROM_EMAIL,
                            recipient_list=[user.email],
                            fail_silently=False,
                        )
                        print(f"Removal email sent to {user.email} for event {instance.name}")
                    except Exception as e:
                        print(f"Failed to send removal email to {user.email}: {str(e)}")
                        


# delete event image if event is deleted or image updated.
@receiver(post_delete, sender=Event)
def delete_event_image(sender, instance, **kwargs):
    if instance.asset:
        
        destroy(instance.asset.public_id)
        
@receiver(post_delete, sender=Event)
def delete_event_image(sender, instance, **kwargs):
    if instance.asset:
        public_id = instance.asset.public_id
        if public_id != "events_asset/default_img":
            destroy(public_id)  # Deletes from Cloudinary using the public ID
            

@receiver(pre_save, sender=Event)
def delete_old_event_image(sender, instance, **kwargs):
    if not instance.pk:
        return  # skip if new instance (no replacement happening)

    try:
        old_instance = Event.objects.get(pk=instance.pk)
    except Event.DoesNotExist:
        return

    if old_instance.asset and old_instance.asset != instance.asset:
        public_id = old_instance.asset.public_id
        if public_id != "events_asset/default_img":
            destroy(public_id)