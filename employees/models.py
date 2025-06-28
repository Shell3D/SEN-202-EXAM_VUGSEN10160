from django.db import models

from django.db import models

# Abstract base class
class StaffBase(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True

    def get_role(self):
        return "Generic Staff"

# Manager model
class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)

    def get_role(self):
        return "Manager"

# Intern model
class Intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, related_name='mentees')
    internship_end = models.DateField()

    def get_role(self):
        return "Intern"

