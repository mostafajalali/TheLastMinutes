from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class obj(models.Model):
    CATEGORY_CHOICES = (
        ('🏠 منزل', '🏠 منزل'),
        ('💼 محل کار', '💼 محل کار'),
        ('🧑‍🎓 محل تحصیل', '🧑‍🎓 محل تحصیل'),
        ('🚗 خودرو', '🚗 خودرو'),
        ('🏷️ سایر', '🏷️ سایر'),
    )
    name=models.CharField(max_length=20, verbose_name='نام وسیله')
    date_s=models.DateField(null= True,blank= True,verbose_name='تاریخ شروع')
    date_e=models.DateField(null=True, blank=True,verbose_name='تاریخ پایان')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_notifed = models.BooleanField(default=False)
    is_finished=models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='سایر' ,verbose_name='دسته بندی')
    slug = models.SlugField(max_length=250)
    


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    def has_alarm(self):
        if self.date_e is not None:
            return True
    def end_alarm(self):
        if self.has_alarm()  >= self.date_s:
            return True   
            
    def status(self):
        if self.is_finished:
            return 'انجام شده!'
        elif self.end_alarm:
            return '.....'
        else:
            return 'تمام شده!'
