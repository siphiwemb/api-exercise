from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .forms import TitanicForm
from .models import Titanic
from django.db.models import F


class TitanicView(APIView):
    keys = [
        "uuid",
        "survived",
        "passengerClass",
        "name",
        "sex",
        "age",
        "siblingsOrSpousesAboard",
        "parentsOrChildrenAboard",
        "fare"
    ]

    def get(self, request, uuid=''):
        if uuid is not None and uuid != '':
            return Response(self.get_specified_person(uuid))
        else:
            return Response(self.get_all_people(), status=200)

    def get_renamed_columns(self, qs):
        return qs.annotate(passengerClass=F('passenger_class'), siblingsOrSpousesAboard=F('siblings_spousesaboard'), parentsOrChildrenAboard=F('parents_childrenaboard')).values(*self.keys)


    def get_all_people(self):
        titanic_qs = Titanic.objects.all()
        return self.get_renamed_columns(titanic_qs)
    

    def get_specified_person(self, uuid):
        titanic_qs = Titanic.objects.filter(uuid=uuid)
        if titanic_qs.exists():
            return self.get_renamed_columns(titanic_qs).first()
        else:
            return "Person Not Found"


    def post(self, request):
        data = request.data
        return Response(self.create_new_person(data))

    
    def create_new_person(self, data):
        data['uuid'] = ""
        form = TitanicForm(data)

        if form.is_valid():
            form_instance = form.save(commit=True)
            titanic_qs = Titanic.objects.filter(uuid=form_instance.uuid)
            return self.get_renamed_columns(titanic_qs).first()
        else:
            return form.errors


    def put(self, request, uuid):
        data = request.data
        return Response(self.update_person(data, uuid))


    def update_person(self, data, uuid):
        if uuid is not None and uuid != '':
            titanic_qs = Titanic.objects.get(uuid=uuid)
            data['uuid'] = uuid
            form = TitanicForm(data, instance=titanic_qs)

            if form.is_valid():
                form_instance = form.save(commit=True)
                titanic_qs = Titanic.objects.filter(uuid=form_instance.uuid)
                return self.get_renamed_columns(titanic_qs).first()
            else:
                return form.errors
        else:
            return "Provide uuid for the person to be updated."


    def delete(self, request, uuid=''):
        return Response(self.delete_person(uuid))
    

    def delete_person(self, uuid):
        if uuid is not None and uuid != '':
            Titanic.objects.filter(uuid=uuid).delete()
            return "Person deleted"
        else:
            return "Provide uuid for the person to be deleted."
