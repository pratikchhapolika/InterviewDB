from django.db import models
from django_markdown.models import MarkdownField

# Create your models here.
COMPANY_LEVELS=(
		('Google','Google'),
		('Facebook','Facebook'),
		('Microsoft', 'Microsoft'),
		('Amazon', 'Amazon'),
		('Quora', 'Quora'),
		('Salesforce', 'Salesforce'),
		('Uber', 'Uber')
		)

class Interview(models.Model):
	question_title = models.CharField(max_length = 500)
	question_description = MarkdownField(default = 'Default question')
	question_company = models.CharField(max_length = 200)
	# question_type = models.CharField(max_length = 500)
	url = models.SlugField(max_length = 500)
	question_input = models.TextField(max_length = 250, default = 'Input of the question')
	question_output = models.TextField(max_length = 500, default = 'Output of the question')	
	timestamp = models.DateTimeField(auto_now_add=True, null=True)
	explanation = models.TextField(max_length=500, default='Explanation')

	def __unicode__(self):
		return self.question_title