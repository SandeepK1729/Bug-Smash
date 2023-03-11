from django.contrib import admin

from .models import Question, User, Test, TestResult, Answer

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Test)
admin.site.register(TestResult)
admin.site.register(Answer)


