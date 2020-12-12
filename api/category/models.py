from django.db import models
from django.utils.safestring import mark_safe
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='categoryImages/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def image_tag(self):
        return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))

    image_tag.short_description = 'Images'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name

    # def get_image_url(self):
    #     return "%s,%s" % (settings.MEDIA_URL, self.image)
