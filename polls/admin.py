from django.contrib import admin

from .models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    """
    Inline fields to add the choice in question model
    """
    model = Choice
    extras = 3
    readonly_fields = ('votes',)

class QuestionAdmin(admin.ModelAdmin):
    """
    Question admin class to add question on the admin panel
    """
    inlines = [ChoiceInline]
    list_display = ['question_text', 'date', 'created_by']
    exclude = ('created_by', 'voted')

    def save_model(self, request, obj, form, change):
        """
        Add request user to the question model created_by attribute"""
        obj.created_by = request.user
        return super().save_model(request, obj, form, change)


# Registering the models and changing some more config
admin.site.register(Question, QuestionAdmin)
admin.site.site_title = "DjangoPolls"
admin.site.site_header = "DjangoPolls"
admin.site.site_url = '/polls'