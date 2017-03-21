from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self): #supaya di tabel munculnya bukan question object semua. str utk python 3, unicode utk python 2
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #on delete : kalau class question di delete, ini juga ikut ke delete
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True) #null & blank mengindikasikan kalau dia optional, kalau kosong jg gpp

    def __str__(self):
        return self.choice_text
