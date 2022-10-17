from django.test import TestCase
from .models import (Titanic, )
from .views import TitanicView
import json

# Create your tests here.

class TitanicTest(TestCase):
    people = [
            {
                "survived": True,
                "name": "Mr. Juha Niskanen",
                "sex": "male",
                "age": 39,
                "fare": 7.925,
                "passengerClass": 3,
                "siblingsOrSpousesAboard": 0,
                "parentsOrChildrenAboard": 0
            },
            {
                "survived": False,
                "name": "Mr. Leonard Charles Moore",
                "sex": "male",
                "age": 19,
                "fare": 8.05,
                "passengerClass": 3,
                "siblingsOrSpousesAboard": 0,
                "parentsOrChildrenAboard": 0
            },
            {
                "survived": False,
                "name": "Mr. Owen Harris Braundy",
                "sex": "male",
                "age": 22,
                "fare": 7.25,
                "passengerClass": 3,
                "siblingsOrSpousesAboard": 7,
                "parentsOrChildrenAboard": 5
            }
        ]

    def setUp(self):
        # create a people

        for person in self.people:
            Titanic.objects.create(
                survived = person['survived'],
                passenger_class = person['passengerClass'],
                name = person['name'],
                sex = person['sex'],
                age = person['age'],
                siblings_spousesaboard = person['siblingsOrSpousesAboard'],
                parents_childrenaboard = person['parentsOrChildrenAboard'],
                fare = person['fare']
            )


    def test_titatic_view(self):
        """TitanicView methods return expected responses"""

        TV = TitanicView()        

        # 1. test TV.get_all_people()

        people = TV.get_all_people()
        
        lst1 = sorted([self.people[0]['name'], self.people[1]['name'], self.people[2]['name']])
        lst2 = sorted([people[0]['name'], people[1]['name'], people[2]['name']])

        self.assertEqual(lst1, lst2)


        # 2. test TV.get_specified_person()
        titatinc_qs = Titanic.objects.get(name=self.people[0]['name'])
        person = TV.get_specified_person(titatinc_qs.uuid)

        name1 = titatinc_qs.name
        name2 = person['name']

        self.assertEqual(name1, name2)


        # 3. test TV.create_new_person()
        new_person = TV.create_new_person(self.people[0])
        new_pers_name = new_person['name']

        self.assertEqual(new_pers_name, self.people[0]['name'])


        # 4. test TV.update_person()
        self.people[0]['survived'] = True
        new_person = TV.update_person(self.people[0], new_person['uuid'])
        new_pers_survival = new_person['survived']

        self.assertEqual(new_pers_survival, True)


        # 5. test TV.delete_person()
        new_pers_deleted = TV.delete_person(new_person['uuid'])
        self.assertEqual(new_pers_deleted, "Person deleted")