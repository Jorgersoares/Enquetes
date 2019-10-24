from django.db import models


# Create your models here.


class Poll(models.Model):
    nome = models.CharField(max_length=200)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    encerrada = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Votação"
        verbose_name_plural = "Votações"

    def __str__(self):
        return self.nome

    def get_vencedor(self):
        questions = Poll_questions.objects.filter(poll=self.id)
        lista = list()
        vencedor_empate = []
        for i in questions:
            lista.append(questions.votos)
        result_set = list(set(lista))



class Poll_questions(models.Model):
    nome = models.CharField(max_length=100)
    poll = models.ForeignKey(
        Poll,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        related_name='poll_fk',
    )
    votos = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.nome
