from django.db import models
import uuid
from django.utils import timezone




class TimestampedModel(models.Model):
    """Abstract model that provides created_at and updated_at timestamps."""


    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True




class UUIDModel(models.Model):
    """Abstract model that uses a UUID primary key."""


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


    class Meta:
        abstract = True




class BaseModel(UUIDModel, TimestampedModel):
    """Common base model for most domain models in the project."""


    class Meta:
        abstract = True