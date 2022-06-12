from django.shortcuts import render,redirect

from django.views import View
from .models import Plan

from .forms import PlanForm,PlanEditStaffForm,PlanEditManagerForm,PlanEditDirectorForm,PlanEditCompanyForm

class IndexView(View):

    def get(self, request, *args, **kwargs):

        plans   = Plan.objects.all()
        context = { "plans":plans }

        return render(request,"planning/index.html",context)

    def post(self, request, *args, **kwargs):

        form    = PlanForm(request.POST)

        if form.is_valid():
            print("保存")
            form.save()


        return redirect("planning:index")

index   = IndexView.as_view()



#TODO:ここでログインを済ませたユーザーのみ編集を受け入れる。

class EditView(View):

    def post(self, request, pk, *args, **kwargs):


        plan    = Plan.objects.filter(id=pk).first()

        form    = PlanEditStaffForm(request.POST,instance=plan)
        if form.is_valid():
            form.save()

        form    = PlanEditManagerForm(request.POST,instance=plan)
        if form.is_valid():
            form.save()
            
        form    = PlanEditDirectorForm(request.POST,instance=plan)
        if form.is_valid():
            form.save()

        form    = PlanEditCompanyForm(request.POST,instance=plan)
        if form.is_valid():
            form.save()


        return redirect("planning:index")

edit    = EditView.as_view()
