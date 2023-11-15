from django.db import models
from django.core.exceptions import ValidationError

class Node(models.Model):
    name = models.CharField(max_length=100)
    is_master = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField()
    last_check_in = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.is_master:
            # Ensure there's only one master node
            if Node.objects.filter(is_master=True).exclude(pk=self.pk).exists():
                raise ValidationError("There can only be one master node.")
        super(Node, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({'Master' if self.is_master else 'Slave'})"
