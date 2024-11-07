from django import forms
from .models import TaskCreate,TaskList


class ListForm(forms.ModelForm):
    class Meta:
        model=TaskList
        fields=['name'] #リストの名前を入力　

        #見た目
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'タスクのタイトルを入力'}),
        }

class ListSelectForm(forms.Form):
    lists=forms.ModelMultipleChoiceField(  # ModelChoiceFieldではなくModelMultipleChoiceFieldを使用
        label='リスト選択',
        required=False,
        queryset=TaskList.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class':'checkbox'}),
    )

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskCreate   # TaskCreateモデルとフォームを紐づける
        fields = ['title', 'description', 'due_date',] #'priority', #'list'  # フォームに表示したいフィールドを指定
        
        # 各フィールドに対してラベルやウィジェット（入力フォームの見た目）をカスタマイズできます。
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'タスクのタイトルを入力'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'タスクの説明を入力', 'rows': 3}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'list':forms.Select(attrs={'class':'from-control'}),
        }
        
        labels = {
            'title': 'タスクタイトル',
            'description': 'タスク説明',
            'due_date': '期日',
            'priority': '優先度',
            'list':'リスト選択',
        }