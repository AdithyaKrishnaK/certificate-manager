from django.contrib import admin
from .models import Certificate
# Register your models here.
class CertificateModelAdmin(admin.ModelAdmin):
    list_display = ('domain_name', 'owner', 'expiry_date')
    search_fields = ('domain_name', 'owner')
    list_filter = ('owner',)

admin.site.register(Certificate, CertificateModelAdmin)