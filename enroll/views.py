from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student
from .forms import StudentForm
from django.views.generic.base import TemplateView , RedirectView
from django.views import View

class UserAddShowView(TemplateView):
    template_name  = 'enroll/first.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = StudentForm()
        stu = Student.objects.all()
        context={'form':form,'objects':stu}
        return context 

    def post(self , request):
        form = StudentForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        del_id = kwargs['pk']
        Student.objects.get(id = del_id).delete()
        return super().get_redirect_url(*args, **kwargs)

class UserUpdateView(View):
    def get(self , request , pk):
        stu = Student.objects.get(id=pk)
        form = StudentForm(instance = stu)
        return render(request , 'enroll/update.html' , context={'form':form})
    def post(self , request , pk):
        form = StudentForm(data = request.POST)
        if form.is_valid():
            object = Student.objects.get(id = pk)
            object.name = form.cleaned_data['name']
            object.email = form.cleaned_data['email']
            object.password = form.cleaned_data['password']
            object.save()
        return HttpResponseRedirect('/')





