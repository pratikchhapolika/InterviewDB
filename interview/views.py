from django.shortcuts import render
from models import Interview
from django.db.models import Q
from .forms import contactForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.

def home(request):
	if request.method=='POST':
		query = request.POST['search']
		results = Interview.objects.filter(Q(question_company__icontains = query)).order_by('-timestamp')
		if len(results)!=0:
			context = { 'results': results, 'query':query}
			template = 'home.html'
			return redirect('company/'+query)
		else:
			context={}
			template = 'nothing_returned.html'
			return render(request, template, context)

	everything = Interview.objects.all()
	context = {'everything': everything}
	template = 'home.html'
	return render(request, template, context)

def company(request, username):
	results = Interview.objects.filter(Q(question_company__icontains = username)).order_by('-timestamp')
	if len(results)!=0:
		context = {'results':results, 'query':username, 'total_company_questions': len(results)}
		template = 'company.html'
		return render(request, template, context)
	else:
		context={}
		template = 'nothing_returned.html'
		return render(request, template, context)


def questions(request, slug, username=None):
	quest = Interview.objects.get(url = slug)
	context = {'quest': quest}
	template = 'question.html'
	return render(request, template, context)

def contact(request):
	title='Contribute your Question'
	form=contactForm(request.POST or None) #contactForm is the name of the class
	confirm_message=None

	if form.is_valid():
		title=form.cleaned_data['question_title']
		description = form.cleaned_data['description_of_the_Question']
		name=form.cleaned_data['name']
		emailFrom=form.cleaned_data['email']
		company = form.cleaned_data['question_asked_in_company']
		input_question = form.cleaned_data['input']
		output_question = form.cleaned_data['output']

		emailTo=[settings.EMAIL_HOST_USER]
		message='%s \nFrom:- %s' %( 'Question title: ' + title + "\n" + 
									'Question description: ' + description + '\n' + 
									'Company: ' + company + '\n' + 
									'Input: ' + input_question + '\n' + 
									'Output: ' + output_question, emailFrom)
		subject='Message from '+name
		send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
		title=""
		confirm_message="Thanks for the message!"
		form=None

	context={ 'title':title, 'form':form, 'confirm_message':confirm_message }
	template='contact.html'
	return render(request, template, context)
