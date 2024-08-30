from datetime import timedelta
from datetime import datetime
from home.models import TableBooking, ReservationTables


def get_interval_for_time(date_time):
    minute = date_time.minute
    if minute < 30:
        interval_start = date_time.replace(minute=0, second=0, microsecond=0)
    else:
        interval_start = date_time.replace(minute=30, second=0, microsecond=0)

    interval_end = interval_start + timedelta(minutes=30)
    return interval_start, interval_end

def get_available_tables(selected_date, selected_time):
    date_string = selected_date + " " + selected_time
    format_string = "%Y-%m-%d %I:%M %p"
    date_time_obj = datetime.strptime(date_string, format_string)
    interval_start, interval_end = get_interval_for_time(date_time_obj)

    booked_tables_subquery = TableBooking.objects.filter(
        booking_date__gte=interval_start,
        booking_date__lt=interval_end
    )
    tables = []
    for table in ReservationTables.objects.all():
        tables.append({
            'table_id': table.table_id,
            'is_available': not booked_tables_subquery.filter(reservation_table=table).exists()
        })

    return tables
