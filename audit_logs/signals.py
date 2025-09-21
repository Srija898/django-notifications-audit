from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out
from .models import AuditLog

@receiver(post_save)
def log_create_update(sender, instance, created, **kwargs):
    if sender.__name__ in ["AuditLog", "Notification"]:
        return
    action = "CREATE" if created else "UPDATE"
    AuditLog.objects.create(
        user=getattr(instance, "user", None),
        action=action,
        model_name=sender.__name__,
        object_id=str(instance.pk),
        description=f"{sender.__name__} {action.lower()}d",
    )

@receiver(post_delete)
def log_delete(sender, instance, **kwargs):
    if sender.__name__ in ["AuditLog", "Notification"]:
        return
    AuditLog.objects.create(
        user=getattr(instance, "user", None),
        action="DELETE",
        model_name=sender.__name__,
        object_id=str(instance.pk),
        description=f"{sender.__name__} deleted",
    )

@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    AuditLog.objects.create(user=user, action="LOGIN", description="User logged in")

@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    AuditLog.objects.create(user=user, action="LOGOUT", description="User logged out")
