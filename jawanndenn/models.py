# Copyright (C) 2019 Sebastian Pipping <sebastian@pipping.org>
# Licensed under GNU Affero GPL v3 or later

import hashlib
import os

from django.db import models
from django.urls import reverse
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
from annoying.fields import AutoOneToOneField


def _get_random_sha256():
    return hashlib.sha256(os.urandom(256 // 8)).hexdigest()


class Poll(TimeStampedModel):
    slug = models.CharField(max_length=64, default=_get_random_sha256, unique=True)
    title = models.CharField(max_length=255)
    equal_width = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("poll-detail", args=[self.slug])


class PollOption(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="options")
    position = models.PositiveSmallIntegerField()  # starting at 0
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ("poll", "position")


class Profile(models.Model):
    user = AutoOneToOneField(User, primary_key=True, on_delete=models.CASCADE)


class Ballot(TimeStampedModel):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name="ballots")
    voter_name = models.CharField(max_length=255)
    voter_user = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="ballots"
    )


class Vote(models.Model):
    ballot = models.ForeignKey(Ballot, related_name="votes", on_delete=models.CASCADE)
    option = models.ForeignKey(PollOption, on_delete=models.CASCADE)

    apruebo, nulo, rechazo = "A", "N", "R"
    ALTERNATIVAS = [(apruebo, "Apruebo"), (nulo, "Nulo"), (rechazo, "Rechazo")]
    choice = models.CharField(max_length=2, choices=ALTERNATIVAS, default=nulo)

    class Meta:
        unique_together = ("ballot", "option")

"""
class Consejo(models.Model):
    nombre = models.CharField(max_length=50)
    miembros = models.ManyToManyField(Profile, related_name="consejos")
    futuros_miembros = models.TextField()

    def agregar_miembros(self):
        por_procesar = self.futuros_miembros.strip().split(",")
        usuarios = User.objects.all()
        emails = [usuario.email for usuario in usuarios]
        for miembro in por_procesar:
            if miembro in emails:
                a_agregar = Profile.get(user__email=miembro)
                print("Agregando a", miembro, "a", self.nombre)
                a_agregar.consejos.add(self)
 """