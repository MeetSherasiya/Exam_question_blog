from django import forms
from exam.models import Paper

class QuestionAdd(forms.ModelForm):

    class Meta:
        model = Paper
        fields = '__all__'
        labels = {
            'Field': 'Field',
            'branch': 'Branch',
            'year': 'Year',
            'exam_type': 'Exam Type',
            'semester': 'Semester',
            'subject': 'Subjet',
            'question_num': 'Question No.',
            'question_subnum': 'Sub Question No.',
            'question_subnum_or_only' : 'Or Question',
            'question': 'Question',
            'question_ans': 'Answer',
            'question_ans_img': 'Image of Answer',
            'question_ans_img_only': 'Only Image Show in Answer',
        }
        widgets = {
            'question': forms.Textarea(attrs={'rows': 5, 'cols': 30}),
            'question_ans': forms.Textarea(attrs={'rows': 5, 'cols': 30}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'