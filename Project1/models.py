from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField() 
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # Relacionamento com usuário
    data_publicacao = models.DateTimeField(auto_now_add=True)  # Data automática ao criar

    def __str__(self):
        return self.titulo  
