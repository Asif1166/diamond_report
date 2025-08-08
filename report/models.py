from django.db import models




class DiamondReport(models.Model):
    report_number = models.CharField(max_length=100, unique=True)
    product = models.CharField(max_length=200, blank=True, null=True)
    g_weight = models.CharField(max_length=100, blank=True, null=True)
    dia_weight = models.CharField(max_length=100, blank=True, null=True)
    colour = models.CharField(max_length=100, blank=True, null=True)
    clarity = models.CharField(max_length=100, blank=True, null=True)
    finish = models.CharField(max_length=100, blank=True, null=True)
    cut = models.CharField(max_length=100, blank=True, null=True)
    metal = models.CharField(max_length=100, blank=True, null=True)
    diamond_image = models.ImageField(upload_to='diamonds/', blank=True, null=True)

    def __str__(self):
        return self.report_number
    


class HomeBanner(models.Model):
    background_image = models.ImageField(upload_to='banners/', blank=True, null=True)
    small_title = models.CharField(max_length=255, blank=True, null=True)  # h3
    big_title = models.CharField(max_length=255, blank=True, null=True)    # h1
    description = models.TextField(blank=True, null=True)
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return self.big_title or "Home Banner"
    


class AboutSection(models.Model):
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    title_part1 = models.CharField(max_length=100, blank=True, null=True)  # e.g., "Welcome"
    title_part2 = models.CharField(max_length=100, blank=True, null=True)  # e.g., "To Hand Made"
    paragraph_1 = models.TextField(blank=True, null=True)
    paragraph_2 = models.TextField(blank=True, null=True)
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.title_part1} {self.title_part2}"
    

# For contact info display
class ContactInfo(models.Model):
    email_1 = models.EmailField(blank=True, null=True)
    email_2 = models.EmailField(blank=True, null=True)
    phone_1 = models.CharField(max_length=20, blank=True, null=True)
    phone_2 = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    map_embed_code = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Contact Info"

# For storing contact form submissions
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name or 'Anonymous'}"
