from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "8b06f1f841msha5e26733df0cf3fp1d389bjsn92d58b56673d",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()



#views
def first(request):
	list = []
	last = int(response['results'])

	for x in range(0,last):
		list.append(response['response'][x]['country'])


	if request.method == 'POST':
		clicked = request.POST['clicked']
		
		
		for x in range(0,last):
			if clicked == response['response'][x]['country']:
				new = response['response'][x]['cases']['new']
				active = response['response'][x]['cases']['active']
				critical = response['response'][x]['cases']['critical']
				recovered = response['response'][x]['cases']['recovered']
				total = response['response'][x]['cases']['total']
				deaths = int(total) - int(active)-int(recovered)

		context = {'clicked': clicked,'list':list,'new': new, 'active': active, 'critical':critical,
								'recovered': recovered,'deaths': deaths,
								'total': total}
		return render(request, 'first.html', context)
	
	
	context = {'list': list}
	return render(request, 'first.html', context)
