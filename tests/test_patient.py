"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name


def test_create_doctor():
    from inflammation.models import Doctor

    name = 'Chris'
    d = Doctor(name=name)

    assert d.name == name
    patient = 'Alice'
    d.add_patient(patient)

    assert d.patients[0].name == patient
