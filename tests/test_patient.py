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

def test_add_observation():
    from inflammation.models import Patient

    patient = 'Alice'
    p = Patient(name=patient)
    obs = p.add_observation(3)

    assert p.observations[0].day == 0
    assert p.observations[0].value == 3
