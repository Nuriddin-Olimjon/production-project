from datetime import date


def filter_by_date_range(queryset, params):
    time_start = params.get('time_start')
    time_end = params.get('time_end')

    if time_start is not None or time_end is not None:
        if time_end is None:
            time_end = date.today()
        if time_start is None:
            time_start = "0001-01-01"
        queryset = queryset.filter(
            time_created__date__range=(time_start, time_end)
        )
    return queryset
