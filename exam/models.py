from django.db import models
import datetime

year_choices = [(r,r) for r in range(2016, datetime.date.today().year+1)]

sem_choice = (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'))
exam_type_choice = (('End Sem','End Sem'),('Mid Sem','Mid Sem'),('Remid','Remid'),('Backlog','Backlog'))

# Create your models here.
class Paper(models.Model):
    id = models.AutoField
    Field = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choices, default='2023')
    exam_type = models.CharField(max_length=20, choices=exam_type_choice, default='End Sem')
    semester = models.CharField(max_length=2, choices=sem_choice, default='1')
    subject = models.CharField(max_length=20)
    question_num = models.IntegerField()
    question_subnum = models.IntegerField()
    question_subnum_or_only = models.BooleanField(default=False)
    question = models.TextField()
    question_ans = models.TextField(blank=True)
    question_ans_img = models.ImageField(upload_to ='./static/image/paperimage/', blank=True, null=True)
    question_ans_img_only = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.branch} - {str(self.year)} - {self.exam_type} - {str(self.semester)} - {self.subject} - {str(self.question_num)}({str(self.question_subnum)})"
    
    def save(self, *args, **kwargs):
        # Convert the input value to uppercase
        self.Field = self.Field.upper()
        self.branch = self.branch.upper()
        self.subject = self.subject.upper()
        super().save(*args, **kwargs)