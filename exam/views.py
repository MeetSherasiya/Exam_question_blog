from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    table = Paper.objects.values('Field').distinct()
    context = {'objs':table}
    return render(request, 'index.html',context)

def field(request,pk):
    table = Paper.objects.values('Field','branch').distinct()
    context = {'objs': table}
    return render(request, 'branch.html', context)

def paper(request,pk):
    table = Paper.objects.filter(id=pk).values()
    re2 = table[0]
    table1 = Paper.objects.filter(Field=re2['Field'], year= re2['year'], branch=re2['branch'], semester=re2['semester'], exam_type=re2['exam_type'] ,subject=re2['subject']).values_list().order_by('question_num','question_subnum')
    context = {'table':table,'sidebar':table1}
    return render(request, 'paper_question.html', context)

def question(request, pk, pk1, pk2, pk3, pk4, pk5):
    table = Paper.objects.filter(Field=pk, year= pk1, branch=pk2, semester=pk3, exam_type=pk4 ,subject=pk5).values().order_by('question_num','question_subnum')
    all_set = []
    all_set.append([pk,pk1,pk2,pk3,pk4,pk5])
    context = {'objs':table,'nav':all_set}
    return render(request, 'question.html', context)

def branch(request, pk, pk1):
    all_year = []
    table = Paper.objects.filter(Field=pk, branch=pk1).values()
    Field = [item['Field'] for item in table]
    Field = [*set(Field)]
    year = {item['year'] for item in table}
    branch= {item['branch'] for item in table}
    for cat1 in branch:
        cat1 = str(cat1)
    for cat in year:
        cat = str(cat)
        all_year.append([cat1,cat,Field])
    all_set = []
    all_set.append([Field,cat1])
    context = {'objs':all_year,'nav':all_set}
    return render(request, 'exam_sem.html',context)


def sem(request, pk, pk1, pk2):
    table = Paper.objects.filter(Field=pk, branch=pk1, year=pk2).values()
    Field = {'Field':item['Field'] for item in table}
    branch = {'branch':item['branch'] for item in table}
    year = {'year':item['year'] for item in table}
    sem = [item['semester'] for item in table]
    sem = [*set(sem)]
    sem.sort()
    all_value = []
    for cat in sem:
        all_value.append([Field,year,branch,cat])
    all_set = []
    all_set.append([Field,branch,year])
    context = {'objs':all_value,'nav':all_set}
    return render(request, 'semester.html', context)

def subject(request,pk,pk1,pk2, pk3,pk4):
    # table = Paper.objects.filter(branch=pk, semester=pk1).values()
    table = Paper.objects.filter(Field=pk, year=pk1, branch=pk2, semester=pk3, exam_type=pk4).values()
    Field = {'Field':item['Field'] for item in table}
    branch = {'branch':item['branch'] for item in table}
    year = {'year':item['year'] for item in table}
    sem = {'sem':item['semester'] for item in table}
    examtype = {'examtype':item['exam_type'] for item in table}
    subject = [item['subject'] for item in table]
    subject = [*set(subject)]
    subject.sort()
    all_value= []
    for cat in subject:
        all_value.append([Field,year,branch,sem,examtype,cat])
    all_set = []
    all_set.append([Field,branch,year,sem,examtype])
    context = {'objs':all_value,'nav':all_set}
    return render(request, 'subject.html', context)

def examtype(request, pk, pk1, pk2, pk3):
    table = Paper.objects.filter(Field=pk, year=pk1, branch=pk2, semester=pk3).values()
    Field = {'Field':item['Field'] for item in table}
    branch = {'branch':item['branch'] for item in table}
    year = {'year':item['year'] for item in table}
    sem = {'sem':item['semester'] for item in table}
    exam_type = [item['exam_type'] for item in table]
    exam_type = [*set(exam_type)]
    exam_type.sort()
    all_value = []
    for cat in exam_type:
        all_value.append([Field,year,branch,sem,cat])
    all_set = []
    all_set.append([Field,branch,year,sem])
    context = {'objs':all_value,'nav':all_set}
    return render(request, 'examtype.html', context)

def error_404(request, exception):
    return render(request, '404error.html')