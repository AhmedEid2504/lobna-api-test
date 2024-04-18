from djongo import models

class MyModel(models.Model):
    username = models.CharField(max_length=200)
    field2 = models.IntegerField()
    email = models.EmailField(max_length=200)
    major = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'my_collection'

    def __str__(self):
        return self.username + " - " + str(self.field2) + " - " + self.email + " - " + self.major
    