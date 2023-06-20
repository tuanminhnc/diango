from django.contrib import admin

# Register your models here.
from polls.models import Question, Choise

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_text', 'pub_date']

class ChoiseAdmin(admin.ModelAdmin):
    list_display = ['id', 'question',  'choise_text', 'vote']

    def question(self, obj):
        return  obj.question.question_text

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choise, ChoiseAdmin)