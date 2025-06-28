from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Manager, Intern

class StaffRoleView(APIView):
    def get(self, request):
        managers = Manager.objects.all()
        interns = Intern.objects.all()

        roles = []

        for m in managers:
            roles.append({'name': m.full_name, 'role': m.get_role()})

        for i in interns:
            roles.append({'name': i.full_name, 'role': i.get_role()})

        return Response(roles)

