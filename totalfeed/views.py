from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from accounts.models import UserProfile
import json

# Create your views here.
class MainView( TemplateView ):
	template_name = "totalfeed/mainview.html"
	
	@method_decorator( login_required )
	def dispatch( self , *args , **kwargs ):
		return super( MainView , self ).dispatch( *args , **kwargs )
	
	def get( self , req , *args , **kwargs ):
		kwargs.setdefault( "curruser" , """ user object """ )
		return super( MainView , self ).get( req , *args , **kwargs )

class SiteView(View):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SiteView, self).dispatch(*args, **kwargs)
	
	def get_context_data(self, **kwargs):
		context = super(SiteView, self).get_context_data(**kwargs)
		context['curruser'] = UserProfile.objects.get(user=self.request.user)
		return context