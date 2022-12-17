from django.shortcuts import render
from datetime import datetime 

def django(request):
    data = {
        'courseName': 'Django',
        'duration': '4 Months',
        'seats': 10,
        'description': 'django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Built by experienced developers, Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It is free and open source, has a thriving and active community, great documentation, and many options for free and paid-for support. Django helps you write software that is: Complete Django follows the "Batteries included" philosophy and provides almost everything developers might want to do "out of the box". Because everything you need is part of the one "product", it all works seamlessly together, follows consistent design principles, and has extensive and',
        'user': '',
        'now': datetime.now(),
        'amount': 800.52585,
        'students': ['Anu', 'Raj', 'Sonam', 'Vikram'],
        'teachers': {
            'teacher1': {'name': 'Rakshamwar', 'subject': 'Science'},
            'teacher2': {'name': 'Wankhede', 'subject': 'Maths'},
            'teacher3': {'name': 'Bhusari', 'subject': 'Marathi'},
            'teacher4': {'name': 'Pande', 'subject': 'History'},
        }
    }
    return render(request, 'course/django.html', data)
    