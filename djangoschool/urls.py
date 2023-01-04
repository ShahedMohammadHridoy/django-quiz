from django.urls import path, include
from school.views import classroom, students, teachers

urlpatterns = [
    path('', include('school.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view() , name='signup'),
    # path('accounts/signup/student/', classroom.),
    # path('accounts/signup/teacher/', classroom.),
]
