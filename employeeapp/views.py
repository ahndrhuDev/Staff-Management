from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView
from .models import Employee
from .forms import EmployeeForm

class EmployeeListViewSet(View):
    def get(self, request):
        employee = Employee.objects.all()
        return render(request, 'index.html', {'employee':employee})
    
class CreateView(FormView):
    template_name = 'index.html'
    form_class = EmployeeForm
    success_url = '/employee'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)