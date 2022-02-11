from django.db import models

class Topic(models.Model):

    #models.Modelを継承した時点でここに主キーである、idフィールドが作られている。だからあえてidフィールドを書く必要はない。

    #文字列型で、2000文字まで許容し、入力必須(Null禁止、空文字列禁止)
    comment     = models.CharField(verbose_name="コメント",max_length=2000)

    def __str__(self):
        return self.comment