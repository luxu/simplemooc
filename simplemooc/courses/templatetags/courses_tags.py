from django.template import Library

register = Library()

from simplemooc.courses.models import Enrollment


def my_courses(user):
	enrollments = Enrollment.objects.filter(user=user)


