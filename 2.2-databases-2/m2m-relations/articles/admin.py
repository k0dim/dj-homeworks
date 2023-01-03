from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from articles.models import Article, Tag, Scope

class ScopeInLineFormset(BaseInlineFormSet):
    def clean(self):
        list_form = [form.cleaned_data.get('is_main') for form in self.forms]
        list_bool = []
        for bools in list_form:
            if bools is True:
                list_bool.append(bools)
        if len(list_bool) > 1 or len(list_bool) == 0:
            raise ValidationError('Ошибка')
        return super().clean()

class ScopeInLine(admin.TabularInline):
    model =  Scope
    formset = ScopeInLineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInLine]
    extra = 1

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass