from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

# Register your models here.
from .models import Interview

class interviewAdmin(MarkdownModelAdmin):
	prepopulated_fields={"url":("question_title",)}
	class Meta:
		model=Interview

admin.site.register(Interview,interviewAdmin)