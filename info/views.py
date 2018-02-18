from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from info.models import *


class InfoListView(TemplateView):
	template_name = "info/info_list.html"

	def get(self, request, *args, **kwargs):
		context = super(InfoListView, self).get_context_data(**kwargs)

		info_list = Info.objects.all().order_by("released").reverse()  # データベースからオブジェクトを取得して
		context['info_list'] = info_list  # 入れ物に入れる

		return render(self.request, self.template_name, context)