import pytest
import random
from rest_framework.test import APIClient
from model_bakery import baker
from django.urls import reverse

from students.models import Student, Course


def random_quantity():
    return random.randint(0,9)

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student():
    return Student.objects.create(name='Student Test')

@pytest.fixture
def cours_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_one(client, student, cours_factory):
    """ Проверка получения 1го курса """

    # Arrange
    course = cours_factory(_quantity=10)
    # Act
    id = course[random_quantity()].id
    response = client.get(
        reverse(viewname="courses-detail", args=[id])
    )
    # Assert
    data = response.json()
    assert data['id'] == id
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_list(client, student, cours_factory):
    """ Проверка получения списка курсов """

    # Arrange
    course = cours_factory(_quantity=10)
    # Act
    response = client.get(reverse(viewname="courses-list"))
    # Assert
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_filter_id(client, student, cours_factory):
    """ Проверка фильтрации списка курсов по id """

    # Arrange
    course = cours_factory(_quantity=10)
    # Act
    id = course[random_quantity()].id
    response = client.get(
        reverse(viewname="courses-list"),
        {'id':f'{id}'}
    )
    # Assert
    data = response.json()
    assert data[0]['id'] == id
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_filter_name(client, student, cours_factory):
    """ Проверка фильтрации списка курсов по name """

    # Arrange
    course = cours_factory(_quantity=10)
    # Act
    name = course[random_quantity()].name
    response = client.get(
        reverse(viewname="courses-list"),
        {'name':f'{name}'}
    )
    # Assert
    data = response.json()
    assert data[0]['name'] == name
    assert response.status_code == 200


@pytest.mark.parametrize(
    ["datacreate", "statuscode"],
    (
        ("FirstCourse", 201),
        ("SecondCourse", 201),
    )
)
@pytest.mark.django_db
def test_create(client, datacreate, statuscode):
    """ Проверка успешного создания курса """

    count = Course.objects.count()
    response = client.post(
        reverse(viewname="courses-list"),
        data = {
            "name":datacreate, 
            "students":[]
        }
    )
    assert response.status_code == statuscode
    assert Course.objects.count() == count + 1


@pytest.mark.parametrize(
    ["datacreate", "statuscode"],
    (
        ("NonFirstCourse", 200),
        ("NonSecondCourse", 200),
    )
)
@pytest.mark.django_db
def test_update(client, datacreate, statuscode, cours_factory):
    """ Проверка успешного обновления курса """
    
    course = cours_factory(_quantity=10)

    id = course[random_quantity()].id
    response = client.patch(
        reverse(viewname="courses-detail", args=[id]),
        data = {
            "name":datacreate, 
        }
    )
    print(response.json())
    assert response.status_code == statuscode


@pytest.mark.django_db
def test_delete(client, cours_factory):
    """ Проверка успешного удаления курса """

    count = Course.objects.count()
    course = cours_factory(_quantity=10)

    id = course[random_quantity()].id
    response = client.delete(
        reverse(viewname="courses-detail", args=[id])
    )
    assert response.status_code == 204