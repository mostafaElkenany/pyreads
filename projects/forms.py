from django import forms
from users.models import Project, Project_pictures, Comment
from django.utils.translation import ugettext_lazy as _


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "title",
            "details",
            "total_target",
            "start_date",
            "end_date",
            "category",
            "tags",
        )
        widgets = {
            "tags": forms.TextInput(attrs={"data-role": "tagsinput", "name": "tags"}),
            "details": forms.Textarea(attrs={"rows": 7, "style": "resize:none;"}),
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date <= start_date:
            msg = "End date should be greater than start date."
            self.add_error("end_date", msg)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Project_pictures
        fields = ("picture",)
        labels = {"picture": "Images"}
        widgets = {
            "picture": forms.ClearableFileInput(attrs={"multiple": True}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        labels = {"content": ""}
        widgets = {
            "content": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "border: none; border-radius: 0",
                    "placeholder": "New Comment....",
                }
            ),
        }
