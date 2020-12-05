from django import forms
from .models import newsSection, Article

class newsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(newsForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta:
        model = newsSection
        fields = ('choices', )

    NEWS_CHOICES =(
        ("Science", "Science"),
        ("Tech", "Tech"),
        ("World Politics", "World Politics"),
        ("Uk", "Uk"),
    )
    choices = forms.MultipleChoiceField(choices = NEWS_CHOICES, widget=forms.CheckboxSelectMultiple, label="Favorite News Section")

class ArticleTitlesForm(forms.ModelForm):
    def __init__(ArticleTitlesForm, *args, **kwargs):
        super(newsForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta:
        model = Article
        fields = ("title", "section", )
