from django.db import models
from django.db.models.deletion import PROTECT
from django.utils import timezone
from django_crypto_fields.fields import IdentityField
from edc_base.model_mixins import BaseUuidModel
from edc_base.utils import get_utcnow


class Appointment(BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)

    appt_datetime = models.DateTimeField(default=get_utcnow)

    visit_code = models.CharField(max_length=25)

    visit_instance = models.CharField(max_length=25)


class CaregiverConsent(BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)

    screening_identifier = models.CharField(max_length=50)

    consent_datetime = models.DateTimeField()

    dob = models.DateField()

    version = models.CharField(
        max_length=10,
        editable=False)

    child_dob = models.DateField(blank=True, null=True)


class SubjectConsent(BaseUuidModel):
    subject_identifier = models.CharField(max_length=25)

    screening_identifier = models.CharField(max_length=50)

    gender = models.CharField(max_length=25)

    is_literate = models.CharField(max_length=25,
                                   blank=True,
                                   null=True)

    witness_name = models.CharField(max_length=25,
                                    blank=True,
                                    null=True)

    dob = models.DateField()

    consent_datetime = models.DateTimeField()

    version = models.CharField(
        max_length=10,
        editable=False)


class CaregiverChildConsent(BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)

    screening_identifier = models.CharField(max_length=50)

    consent_datetime = models.DateTimeField()

    child_dob = models.DateField()

    gender = models.CharField(max_length=10)

    identity = IdentityField(
        verbose_name='Identity number',
        null=True, blank=True)

    identity_type = models.CharField(
        verbose_name='What type of identity number is this?',
        max_length=25,
        null=True,
        blank=True)

    confirm_identity = IdentityField(
        help_text='Retype the identity number',
        null=True,
        blank=True)

    version = models.CharField(
        max_length=10,
        editable=False)


class ChildAssent(BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)

    screening_identifier = models.CharField(max_length=50)

    consent_datetime = models.DateTimeField()

    dob = models.DateField()

    identity = IdentityField(
        verbose_name='Identity number',
        null=True, blank=True)

    version = models.CharField(
        max_length=10,
        editable=False)


class ChildDataset(BaseUuidModel):

    study_child_identifier = models.CharField(max_length=36)

    infant_sex = models.CharField(max_length=7)


class ChildVisit(BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)

    appointment = models.OneToOneField(Appointment, on_delete=PROTECT)

    report_datetime = models.DateTimeField(default=get_utcnow)

    schedule_name = models.CharField(max_length=25)

    visit_code = models.CharField(
        max_length=25,
        null=True,
        blank=True)


class RegisteredSubject(BaseUuidModel):

    subject_identifier = models.CharField(
        max_length=50,
        unique=True)

    relative_identifier = models.CharField(
        max_length=36,
        null=True,
        blank=True)


class ScreeningPriorBhpParticipants(BaseUuidModel):

    screening_identifier = models.CharField(max_length=50)

    report_datetime = models.DateTimeField()

    study_child_identifier = models.CharField(max_length=50)


class FlourishConsentVersion(BaseUuidModel):

    screening_identifier = models.CharField(
        max_length=50,)

    version = models.CharField(
        max_length=3)

    report_datetime = models.DateTimeField(
        default=timezone.now,)
