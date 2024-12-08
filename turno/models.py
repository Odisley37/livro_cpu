from django.db import models

class Turno(models.Model):
    turn = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['turn']
        
    def __str__(self):
        return self.turn
    
