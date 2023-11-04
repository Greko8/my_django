import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory

@pytest.mark.django_db
def test_get_course(client, course_factory):
    courses = course_factory(_quantity=20)

    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()

    assert data[0]['id'] == courses[0].id
    assert len(data) == len(courses)

@pytest.mark.django_db
def test_get_course_id(client, course_factory):
    courses = course_factory(_quantity=20)

    response = client.get(f'/api/v1/courses/?id={courses[2].id}')
    assert response.status_code == 200
    data = response.json()

    assert data[0]['id'] == courses[2].id

@pytest.mark.django_db
def test_get_course_name(client, course_factory):
    courses = course_factory(_quantity=20)

    response = client.get(f'/api/v1/courses/?name={courses[2].name}')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[2].name

@pytest.mark.django_db
def test_create_course(client):
    response = client.post('/api/v1/courses/', data={'name': 'Курс 1'})

    assert response.status_code == 201

@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses = course_factory(_quantity=20)

    response = client.patch(f'/api/v1/courses/{courses[2].id}/', data={'name': 'другой курс'})

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'другой курс'

@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=20)

    response = client.delete(f'/api/v1/courses/{courses[2].id}/')

    assert response.status_code == 204