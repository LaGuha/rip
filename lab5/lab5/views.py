from django.shortcuts import render
content=[
		{
			'id' : 1,
			'author' : "author1",
			'text' : "text1"
		},
		{
			'id' : 2,
			'author' : "author2",
			'text' : "text2"
		},
		{
			'id' : 3,
			'author' : "author3",
			'text' : "text3"
		}
	]

# Create your views here.
def lab5(request):
	return render(request, 'lab5/lab5.html',{"Text":content})

def info(request, pk):
	return render(request, 'lab5/info.html',{"Text":content[int(pk)-1]})