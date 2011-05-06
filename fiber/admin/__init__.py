from django.contrib import admin
from fiber.admin.contentitemadmin import ContentItemAdmin
from fiber.admin.pageadmin import PageAdmin
from fiber.models import Page, ContentItem, Image, File

# Regular admin site
admin.site.register(Page, PageAdmin)
admin.site.register(ContentItem, ContentItemAdmin)
admin.site.register(Image)
admin.site.register(File)
