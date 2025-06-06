from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = [
        {
            'S_no' : '1',
            'Name' : 'Prathmesh Bhoir',
            'Course' : 'Python',
            'Age' : '20',
            'Nationality' : 'Indian'
        },
        {
            'S_no' : '2',
            'Name' : 'Abhishek Barote',
            'Course' : 'Web Application',
            'Age' : '20',
            'Nationality' : 'Indian'
        },
        {
            'S_no' : '3',
            'Name' : 'Vivek Bargude',
            'Course' : 'Flutter',
            'Age' : '21',
            'Nationality' : 'Indian'
        }
    ]
    
    context = {
        'data': data
    }
    
    return render(request, 'index.html', context)


def counter(request):
    words = request.POST['text']
    amount_of_words = len(words.split())
    return render(request, 'counter.html', {'amount':amount_of_words})

def largest(request):
    if 'number1' in request.GET and 'number2' in request.GET and 'number3' in request.GET:
        num1 = int(request.GET['number1'])
        num2 = int(request.GET['number2'])
        num3 = int(request.GET['number3'])
        largest_num = max(num1, num2, num3)
        return render(request, 'largest.html', {'largest_num': largest_num})
    else:
        return HttpResponse("Please provide all three numbers.")




