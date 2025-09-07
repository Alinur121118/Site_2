from django.db import models

# Create your models here.
class InfoUser(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    image = models.ImageField(upload_to='infouser/', verbose_name="Фотография")
    email = models.EmailField()
    description = models.TextField(verbose_name="Описание")
    telegram = models.URLField(verbose_name="Телерам")
    github = models.URLField(verbose_name="Гитхаб")
    You = models.CharField( verbose_name="Ютуб")
    Google = models.CharField( verbose_name="Гугл")
    Experience = models.IntegerField(verbose_name="Опыт работы")
    Project = models.IntegerField(verbose_name="Завершенный проект")
    Happy_Clients= models.IntegerField(verbose_name="Довольные клиенты")



    def __str__(self):
        return f"{self.name} / {self.email} / {self.surname}"
    
    class Meta:
        verbose_name  = "Информация о пользователье"
        verbose_name_plural  = "Информация о пользователях"

class Services(models.Model):
    title = models.CharField(max_length=255,verbose_name="Названия услуги")
    description = models.TextField(verbose_name="Описания услуги")

    def __str__(self):
        return f"ID: {self.id} || Title: {self.title}"
            
    class Meta:
        verbose_name  = "Услуга"
        verbose_name_plural  = 'Услуги'

class Experience(models.Model):
    start_year = models.IntegerField(verbose_name= "Начало опыта")
    last_year = models.IntegerField(verbose_name= "Конец опыта")
    work = models.CharField(max_length=255, verbose_name= "Должность")
    lokation = models.CharField(max_length=255, verbose_name= "Локация")

    def __str__(self):
        return f"ID: {self.id} || Начало и конец опыта: {self.start_year}-{self.last_year} || Должность: {self.work}"
    
    class Meta:
        verbose_name  = "Год опыта"
        verbose_name_plural  = 'Годы опыта'

class Education(models.Model):
    start_year = models.IntegerField(verbose_name= "Начало образования")
    last_year = models.IntegerField(verbose_name= "Конец образования")
    lesson = models.CharField(max_length=255, verbose_name= "Образования")
    lokation = models.CharField(max_length=255, verbose_name= "Локация")

    def __str__(self):
        return f"ID: {self.id} || Начало и конец образования: {self.start_year}-{self.last_year} || Образования: {self.lesson}"
    
    class Meta:
        verbose_name  = "Год образования"
        verbose_name_plural  = 'Годы образования'

class Skills(models.Model):
    names = models.CharField(max_length=255, verbose_name= "Названия скила")
    image = models.ImageField(upload_to='infouser/', verbose_name="Фотография")
    skils_2 = models.IntegerField(verbose_name="Скил")




    class Meta:
        verbose_name  = "Скил"
        verbose_name_plural  = 'Скилы'
