from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome.upper()


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "acessório"


class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "cores"


class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="modelos"
    )
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="modelos")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Modelos"


class Veiculo(models.Model):
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")
    descricao = models.CharField(max_length=100, default="")
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True
    )
    ano = models.IntegerField(null=True, blank=True)
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    modelo = models.ForeignKey(
        Modelo,
        on_delete=models.PROTECT,
        related_name="veiculos",
        default=2,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.modelo} {self.descricao}"

    class Meta:
        verbose_name = "Veículo"
