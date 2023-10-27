import subprocess
from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

# Create your models here.
class Certificate(models.Model):
    domain_name = models.CharField(max_length=255, blank=False, null=False)
    owner = models.EmailField(blank=False, null=False)
    expiry_date = models.DateTimeField(null=True, blank=True)
    private_key = models.FileField(upload_to='uploads/private_keys')
    certificate = models.FileField(upload_to='uploads/certs')

    def save(self, *args, **kwargs):
        # Call the parent class's save method to ensure normal save behavior
        super().save(*args, **kwargs)

        # Validate the certificate using the private key
        try:
            validation_output = subprocess.check_output([
                'openssl', 'x509', '-noout', '-in', self.certificate.path,
                '-pubkey', '-out', '/dev/null', '-signkey', self.private_key.path
            ])
            if validation_output:
                raise ValidationError("Certificate validation failed.")
        except subprocess.CalledProcessError:
            raise ValidationError("Certificate validation failed.")

        # Extract the certificate expiry date
        cert_info = subprocess.check_output([
            'openssl', 'x509', '-noout', '-enddate', '-in', self.certificate.path
        ]).decode('utf-8')
        # Extract and parse the expiry date
        expiry_date_str = cert_info.split('=')[1].strip()
        self.expiry_date = datetime.strptime(expiry_date_str, '%b %d %H:%M:%S %Y %Z')

        # Save the model with the updated expiry date
        super().save(*args, **kwargs)


class CertificateRenewal(models.Model):
    pass