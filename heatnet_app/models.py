from django.core.exceptions import ValidationError
from django.db import models
import math


class Project(models.Model):
    # TYPES = (
    #     ('Креслення', 'Креслення'),
    #     ('Розрахунок', 'Розрахунок'),
    #     ('Граф', 'Граф'),
    # )
    # type = models.CharField(max_length=20, choices=TYPES)
    name = models.CharField(max_length=100)


class Node(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='nodes')
    number = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    TYPES = (
        ('Теплова камера', 'Теплова камера'),
        ('Споживач', 'Споживач'),
    )
    type = models.CharField(max_length=100, choices=TYPES, blank=True, null=True)

    def __str__(self):
        if self.type == 'Теплова камера':
            return f"ТК-{self.number}"
        if self.type == 'Споживач':
            return f"{self.address}({self.number})"
        else:
            return "---"


class Link(models.Model):
    node1 = models.ForeignKey(Node, related_name='links_to', on_delete=models.CASCADE)
    node2 = models.ForeignKey(Node, related_name='links_from', on_delete=models.CASCADE)
    length = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Дожина ділянки (м)")
    flow_rate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Витрата (т/год)")
    speed = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Швидкість(м/с)")
    diameter = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def clean(self):
        super().clean()
        if self.speed is None:
            raise ValidationError("Швидкість має бути в межах 1.5 - 2 м/с")
        if self.speed < 1.5:
            raise ValidationError("Швидкість має бути не менше 1.5 м/с")
        if self.speed > 2:
            raise ValidationError("Швидкість має бути не більше 2 м/с")

    def given_length(self):
        gl = self.length * 1.3
        return gl

    def calculate_diameter(self):
        flow_rate = float(self.flow_rate)  # перетворюємо Decimal у float
        speed = float(self.speed)  # перетворюємо Decimal у float
        return math.sqrt((4 * flow_rate) / (math.pi * speed))

    def save(self, *args, **kwargs):
        if not self.diameter:
            self.diameter = self.calculate_diameter()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ділянка {self.node1} ===> {self.node2}"
