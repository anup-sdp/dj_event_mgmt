# users, signals.py:
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import pre_save, post_delete
from cloudinary.uploader import destroy

User = get_user_model()

@receiver(post_save, sender=User)
def send_activation_email(sender, instance, created, **kwargs):
    if created:
        token = default_token_generator.make_token(instance)
        activation_url = f"{settings.FRONTEND_URL}/users/activate/{instance.id}/{token}/"
        subject = 'Activate Your Account'
        message = (
            f'Hi {instance.username},\n\n'
            f'Activate your account by clicking the link below:\n'
            f'{activation_url}\n\nThank You!'
        )
        recipient_list = [instance.email]
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)                      
        except Exception as e:
            print(f"Failed to send email to {instance.email}: {str(e)}")
            

@receiver(post_save, sender=User)
def assign_role(sender, instance, created, **kwargs):
    if created:
        user_group, created = Group.objects.get_or_create(name='Participant')  # returns tuple
        instance.groups.add(user_group)
        #instance.save()  # no need to call, here—the m2m add() is enough
        # Avoid calling save() inside a post_save
        


@receiver(post_delete, sender=User)
def delete_profile_image_on_user_delete(sender, instance, **kwargs):    
    img = getattr(instance, 'profile_image', None)
    public_id = getattr(img, 'public_id', None)
    if public_id:
        destroy(public_id)

        
@receiver(pre_save, sender=User)  # learn pre_save vs post_save in details -----
def delete_old_profile_image_on_change(sender, instance, **kwargs):    
    if not instance.pk:
        return  # New user    
    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return  # user doesn't exist yet
    
    old_img = getattr(old_instance, 'profile_image', None)
    old_id = getattr(old_img, 'public_id', None)
    
    new_img = getattr(instance, 'profile_image', None)
    new_id = getattr(new_img, 'public_id', None)    
    
    if old_id and old_id != new_id:
        destroy(old_id)

       
