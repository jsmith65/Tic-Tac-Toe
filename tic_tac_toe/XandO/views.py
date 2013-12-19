from django.shortcuts import render

def playGame(request):
	context = {}
	return render(request, 'playGame.html', context)