from django import forms
from .models import Category, Event, Participant

# Mixing to apply style to form field,
class StyledFormMixin:
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)  # MRO: Method Resolution Order, here, calls init of forms.ModelForm
        self.apply_styled_widgets()

    default_classes = "border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-cyan-500 mb-1"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    #'class': 'block w-full border border-gray-300 rounded-md px-3 py-2 focus:outline-none focus:ring focus:ring-indigo-200 focus:border-indigo-300 mb-1',
                    'placeholder': f"Enter {field.label.lower()}"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': self.default_classes, 
                    'rows': 3,
                    'placeholder':  f"Enter {field.label.lower()}",
                })
            elif isinstance(field.widget, forms.SelectDateWidget):                
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'type': 'datetime-local',  # HTML5 datetime input
                    'placeholder': 'YYYY-MM-DDTHH:MM'
                })
            elif isinstance(field.widget, forms.DateInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'type': 'date',  # HTML5 date input
                    'placeholder': 'YYYY-MM-DD'
                })
            elif isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'type': 'time',  # HTML5 time input
                    'placeholder': 'HH:MM'
                })    
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):                
                field.widget.attrs.update({
                    'class': "space-y-2"
                })
            else:              
                field.widget.attrs.update({
                    'class': self.default_classes
                })

class CategoryForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-cyan-500 mb-1'}),			 
            'description': forms.Textarea(attrs={
                'class': 'border-2 border-gray-300 w-full p-3 rounded-lg shadow-sm focus:outline-none focus:border-cyan-500 mb-1',
                'rows': 3,  # Adjust the number of visible rows as needed
            }),
		}

class EventForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category']  # no image
        widgets = {
            # name, description as default
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }



class ParticipantForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'events']
        widgets = { 
            # 'events': forms.SelectMultiple(attrs={'class': 'border rounded px-2 py-1 w-full'})
            'events': forms.CheckboxSelectMultiple(attrs={'class': 'border rounded px-2 py-1 w-full'})
        }