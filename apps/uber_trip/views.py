from django.shortcuts import render, redirect
from django.db.models import Sum, Avg
from .models import UberTrip

# Create your views here.
def index(request):
    uber_trips = UberTrip.objects.all().order_by('created_at')
    print uber_trips
    trip_count = UberTrip.objects.all().count()
    print "Trip Count: {}".format(trip_count)
    fare_sum = UberTrip.objects.aggregate(Sum('fare'))
    print "Fare Sum: {}".format(fare_sum)
    miles_sum = UberTrip.objects.aggregate(Sum('miles_driven'))
    print "Miles Sum: {}".format(miles_sum)
    miles_tax_refund_percentage = .535
    args = {
        'fare_sum': fare_sum,
        'uber_trips': uber_trips,
        'miles_sum': miles_sum,
        'trip_count': trip_count,
    }
    return render(request, 'uber_trip/index.html', args)

def enter_trip(request):
    uber_trips = UberTrip.objects.all()
    last_trip = UberTrip.objects.all().last()
    fare_sum = UberTrip.objects.aggregate(Sum('fare'))
    miles_sum = UberTrip.objects.aggregate(Sum('miles_driven'))
    args = {
        'uber_trips': uber_trips,
        'fare_sum': fare_sum,
        'miles_sum': miles_sum,
        'last_trip': last_trip
    }
    return render(request, 'uber_trip/enter_trip.html', args)

def add_trip(request):
    if request.method == 'POST':
        print request.POST
        new_trip = UberTrip.objects.validate_trip(request.POST)
        uber_trips = UberTrip.objects.all()
        fare_sum = UberTrip.objects.aggregate(Sum('fare'))
        miles_sum = UberTrip.objects.aggregate(Sum('miles_driven'))
        print new_trip
        args ={
            'new_trip': new_trip,
            'uber_trips': uber_trips,
            'fare_sum': fare_sum,
            'miles_sum': miles_sum,
        }
        # return redirect('/', args)
        return render(request, 'uber_trip/index.html', args)
    else:
        return redirect('/enter_trip')

def view_trip(request, id):
    trip = UberTrip.objects.all().filter(id=id)
    uber_trips = UberTrip.objects.all()
    fare_sum = UberTrip.objects.aggregate(Sum('fare'))
    miles_sum = UberTrip.objects.aggregate(Sum('miles_driven'))
    args={
        'trip': trip,
        'uber_trips': uber_trips,
        'fare_sum': fare_sum,
        'miles_sum': miles_sum,
    }
    return render(request, 'uber_trip/view_trip.html', args)