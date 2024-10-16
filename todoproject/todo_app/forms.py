from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task  # Taskモデルとフォームを紐づける
        fields = ['title', 'description', 'due_date', 'priority']  # フォームに表示したいフィールドを指定
        
        # 各フィールドに対してラベルやウィジェット（入力フォームの見た目）をカスタマイズできます。
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'タスクのタイトルを入力'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'タスクの説明を入力', 'rows': 3}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }
        
        labels = {
            'title': 'タスクタイトル',
            'description': 'タスク説明',
            'due_date': '期日',
            'priority': '優先度',
        }
