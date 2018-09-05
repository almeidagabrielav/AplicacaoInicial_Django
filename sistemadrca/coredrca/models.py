from django.db import models

class Credito(models.Model):
    #num de creditos da disciplina
    d_credito = models.IntegerField()
    #pre requisito da disciplina
    d_credito_p = models.IntegerField()
    #num de creditos obrigatorios do aluno
    a_credito_o = models.IntegerField()
    #num de creditos não obrigatorios do aluno
    a_credito_l = models.IntegerField()
    def __str__(self):
        return str(self.d_credito)


class Departamento(models.Model):
    nome = models.CharField(max_length = 30)

    def __str__(self):
        return str(self.nome)


class Professor(models.Model):
    nome = models.CharField(max_length = 30)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return str(self.nome)


class Secretaria(models.Model):
    nome = models.CharField(max_length = 30)
    tipo = models.IntegerField()
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return str(self.nome)


class Curso(models.Model):
    nome = models.CharField(max_length = 30)
    secretaria = models.ForeignKey(Secretaria, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return str(self.nome)


class Disciplina(models.Model):
    nome = models.CharField(max_length = 30)
    codigo = models.CharField(max_length = 30)
    #disciplina obrigatoria ou eletiva
    obr_let = models.CharField(max_length = 30) 
    status = models.CharField(max_length = 30) 
    credito = models.ForeignKey(Credito, on_delete=models.PROTECT)
    d_requisito = models.ManyToManyField('Disciplina', blank = True)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.nome)


class Aluno(models.Model):
    nome = models.CharField(max_length = 30)
    matricula = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, null = True)
    credito = models.ForeignKey(Credito, on_delete=models.PROTECT)
    disciplinas = models.ManyToManyField(Disciplina, blank=True)

    def __str__(self):
        return str(self.nome)
