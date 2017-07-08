from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse, reverse_lazy
from . models import DailyDietTotals


class IndexView(generic.ListView):
    template_name = 'nutrition/index.html'
    context_object_name = 'all_daily_diet_totals'

    def get_queryset(self):
        return DailyDietTotals.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['daily_diet_totals'] = [0,1,2,3]
        return context

    def organize_data(self):
        array_of_averages_per_date = []
        newVariable = 4
        for meal in DailyDietTotals:
            array_of_averages_per_date.append(newVariable)
        return newVariable


class DetailView(generic.DetailView):
    model = DailyDietTotals
    template_name = 'nutrition/detail.html'


class DailyDietTotalsCreate(CreateView):
    model = DailyDietTotals
    fields = ['date', 'total_KCALS', 'total_protein', 'total_carbs', 'total_fat']


class DailyDietTotalsUpdate(UpdateView):
    model = DailyDietTotals
    fields = ['date', 'total_KCALS', 'total_protein', 'total_carbs', 'total_fat']


class DailyDietTotalsDelete(DeleteView):
    model = DailyDietTotals
    success_url = reverse_lazy('nutrition:index')
