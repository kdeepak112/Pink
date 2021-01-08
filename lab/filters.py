import django_filters
from django_filters import CharFilter , DateFilter
from patient.models import labBook

class orderFilter(django_filters.FilterSet):
    Start_Date = DateFilter(field_name='test_date',lookup_expr = 'gte')
    End_Date = DateFilter(field_name='test_date',lookup_expr = 'lte')
    test_name = CharFilter(field_name='test_name',lookup_expr = 'icontains')
    test_time = CharFilter(field_name='test_time',lookup_expr = 'icontains')
    class Meta:
        model = labBook
        fields = '__all__'
        exclude=['report','pid','pname','pgender','page','pemail','lab_id','lab_suburb','lab_name','bookingStatus','testStatus','pcontact','lab_city','fasting','postprandal',]