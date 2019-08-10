from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from info.models import *


class UpdateInfoView(TemplateView):
    template_name = "info/update_info.html"

    def get(self, request, *args, **kwargs):
        context = super(UpdateInfoView, self).get_context_data(**kwargs)

        update_info = Info.objects.all().order_by("released").reverse()  # データベースからオブジェクトを取得して
        context['update_info'] = update_info  # 入れ物に入れる

        return render(self.request, self.template_name, context)