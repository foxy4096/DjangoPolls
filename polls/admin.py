from django.contrib import admin

from .models import Question, Choice
# Register your models here.

class ChoiceInlineAdmin(admin.TabularInline):
    model = Choice
    extras = 3
    readonly_fields = ('votes',)

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInlineAdmin]
    list_display = ['question_text', 'date', 'created_by']
    exclude = ('created_by', 'voted')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        return super().save_model(request, obj, form, change)



admin.site.register(Question, QuestionAdmin)
admin.site.site_title = "DjangoPolls"
admin.site.site_header = "DjangoPolls"
admin.site.site_url = '/polls'