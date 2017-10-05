from django import forms
from .models import Timepost
from .daysOfWeek import DAYS_OF_WEEK
class TimepostForm(forms.ModelForm):
    class Meta:
        model = Timepost
        fields = ['days',
                  'start_time',
                  'end_time',]
        # TODO: Hope these in html ui to be date/time picker (maybe using angular.js/JQuery)
        widgets = {
            'start_time': forms.TextInput(attrs={'class': 'timepicker text-center',
                                                     'time-string': 'model.timeString',
                                                     'default-time': 'model.options.defaultTime',
                                                     'time-format': 'model.options.timeFormat',
                                                     'start-time': 'model.options.startTime',
                                                     'min-time': 'model.options.minTime',
                                                     'max-time': 'model.options.maxTime',
                                                     'interval': 'model.options.interval',
                                                     'dynamic': 'model.options.dynamic',
                                                     'scrollbar': 'model.options.scrollbar',
                                                     'dropdown': 'model.options.dropdown',
                                                     'placeholder': 'start time'
                                                     }),
            'end_time': forms.TextInput(attrs={'class': 'timepicker text-center',
                                                     'time-string': 'model.timeString',
                                                     'default-time': 'model.options.defaultTime',
                                                     'time-format': 'model.options.timeFormat',
                                                     'start-time': 'model.options.startTime',
                                                     'min-time': 'model.options.minTime',
                                                     'max-time': 'model.options.maxTime',
                                                     'interval': 'model.options.interval',
                                                     'dynamic': 'model.options.dynamic',
                                                     'scrollbar': 'model.options.scrollbar',
                                                     'dropdown': 'model.options.dropdown',
                                                     'placeholder': 'end time'
                                                     }),
        }

