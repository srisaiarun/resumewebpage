from django.shortcuts import render

def resume_view(request):
    # Sample data to be rendered in the template
    context = {
        'name': 'Sri Sai Arun',
        'father_name': 'Srinivas',
        'mother_name': 'Padmaja',
        'contact_info': {
            'email': 'janagamssarun22@gmail.com',
            'phone': '9502473298',
            'address': 'Ramanthapur, Hyderabad, Telangana, India'
        },
        'education': [ 
            {'level': 'High School', 'school': 'Cardinal Gracious High School', 'year': '2021'},
            {'level': 'Intermediary', 'school': 'Narayana Junior College', 'year': '2023'},
            {'level': 'Graduation', 'school': 'KL University', 'year': '2027'},
        ],
        'hobbies': [
            'Dancing',
            'Gaming',
            'Singing',
            'Photography'
        ],
        'achievements': [
        ],
        'github_link': 'https://github.com/srisaiarun',  # Add your GitHub link here
    }
    return render(request, 'resume.html', context)
