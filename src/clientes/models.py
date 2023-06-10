from django.db import models

class Cliente(models.Model):

    ESTADOS = [
        ("SP", "Sao Paulo"),
        ("MG", "Minas Gerais"),
        ("GO", "Gioas")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    cidade = models.CharField(max_length=70, null=False, blank=False)
    estado = models.CharField(choices=ESTADOS, max_length=2, null=False, blank=False)
    endereço = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome
