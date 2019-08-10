from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

class PortalView(TemplateView):
    template_name = "portal/index.html"

    def get(self, request, *args, **kwargs):

        return render(self.request, self.template_name)
        
class PortalAboutView(TemplateView):
    template_name = "portal/about.html"

    def get(self, request, *args, **kwargs):

        return render(self.request, self.template_name)