import django.utils.timezone
from django.db import models
from faker import Faker


class Students(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    birthday = models.DateField(
        default=django.utils.timezone.now(),
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'{self.name} {self.surname}'

    @classmethod
    def create_fake_student(cls, qnt):
        f = Faker()
        for i in range(qnt):
            name = f.first_name()
            surname = f.last_name()
            email = f'{str(name).lower()}.{str(surname).lower()}@gmail.com'
            st = Students(name=name, surname=surname, email=email)
            print(st)
            try:
                st.save()
                print('Saved')
            except:
                pass

    class Meta:
        db_table = 'students'
