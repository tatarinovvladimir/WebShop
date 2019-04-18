from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=50, error_messages={'invalid':'Некорректное имя!'})
    surname = forms.CharField(max_length=50,  error_messages={'invalid':'Некорректная фамилия!'})
    patronymic = forms.CharField(max_length=50,  error_messages={'invalid':'Некорректное отчество!'})
    email = forms.EmailField(max_length=100)
    city = forms.CharField(max_length=50,  error_messages={'invalid':'Некорректное название города!'})
    post_adress = forms.IntegerField(error_messages={'invalid':'Некорректный номер отделения!'})
    phone = forms.CharField(max_length=13,  error_messages={'invalid':'Некорректный номер телефона!'})

    def clean_name(self):
        data = self.cleaned_data['name']
        if data.isalpha():
            return data
        else:
            raise forms.ValidationError(self.fields['name'].error_messages['invalid'])

    def clean_surname(self):
        data = self.cleaned_data['surname']
        if data.isalpha():
            return data
        else:
            raise forms.ValidationError(self.fields['surname'].error_messages['invalid'])

    def clean_patronymic(self):
        data = self.cleaned_data['patronymic']
        if data.isalpha():
            return data
        else:
            raise forms.ValidationError(self.fields['patronymic'].error_messages['invalid'])

    def clean_email(self):
        data = self.cleaned_data['email']
        return data

    def clean_city(self):
        data = self.cleaned_data['city']
        if data.isalpha() or ' ' in data or '-' in data:
            return data
        else:
            raise forms.ValidationError(self.fields['city'].error_messages['invalid'])

    def clean_post_adress(self):
        data = self.cleaned_data['post_adress']
        if data >= 0:
            return data
        else:
            raise forms.ValidationError(self.fields['post_adress'].error_messages['invalid'])

    def clean_phone(self):
        data = self.cleaned_data['phone']
        if data.startswith('+') and data[1:len(data)].isdigit():
            return data
        else:
            raise forms.ValidationError(self.fields['phone'].error_messages['invalid'])

	