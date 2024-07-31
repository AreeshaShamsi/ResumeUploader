from django.shortcuts import render
from .forms import Resumeform
from .models import resume
from django.views import View
from django.shortcuts import render, get_object_or_404

class HomeView(View):
 def get(self, request):
  form =Resumeform()
  candidates = resume.objects.all()
 
  return render(request, 'home.html', {'candidates':candidates,'form':form})
 

 def post(self, request):
  form = Resumeform(request.POST, request.FILES)
  if form.is_valid():
   form.save()
   return render(request, 'home.html', {'form':form}) 

class CandidateView(View):
 def get(self, request, pk):
  candidate = resume.objects.get(pk=pk)
  return render(request, 'candidate.html', {'candidate':candidate})