from django.forms import ModelForm, FileField
from .models import Comment, Ad
from .humanize import naturalsize
from django.core.files.uploadedfile import InMemoryUploadedFile

class CommentForm(ModelForm):
    class Meta():
        model = Comment
        fields = ['text',]
        labels = {'text':'comment'}

class PictureForm(ModelForm):
    max_upload_limit = 2*1024*1024
    max_upload_limit_text = naturalsize(max_upload_limit)
    picture = FileField(required=False, label='Upload Ad picture'+max_upload_limit_text)
    upload_field_name = 'picture'
    
    class Meta:
        model = Ad
        fields = ['title', 'price', 'text', 'picture']
    
    def clean(self):
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')
        if pic is None:
            return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', 'picture must be <'+self.max_upload_limit_text+'bytes')
    
    def save(self, commit=True):
        instance = super(PictureForm, self).save(commit=False)
        pic = instance.picture
        if isinstance(pic, InMemoryUploadedFile):
            bytearr = pic.read()
            instance.content_type = pic.content_type
            instance.picture = bytearr
        if commit:
            instance.save()
        return instance