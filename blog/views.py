from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
	return render(request, 'blog/index.html')

def topics(request):

	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'blog/topics.html', context)

def topic(request, tid):
	topic = Topic.objects.get(id=tid)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'blog/topic.html', context)