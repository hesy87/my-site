from xml.etree.ElementTree import Comment
from django import forms
from blog.models import commnet
from captcha.fields import CaptchaField


class commentform (forms.ModelForm):
    #captcha = CaptchaField()
    class Meta:
        model = commnet
        fields = ['post','name','subject','message','email']