from . import models

def get_logo(request):
	logo=models.AppSetting.objects.first()
	data={
		'logo':logo
	}
	return data 