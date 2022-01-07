import itertools

import jdatetime


def jalali_convertor(model):
    # Gregorian To Jalali date
    year = '%Y'
    month = '%m'
    day = '%d'
    year = int(model.date.strftime(year))
    month = int(model.date.strftime(month))
    day = int(model.date.strftime(day))
    jalali = jdatetime.GregorianToJalali(year, month, day)
    months = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند', ]
    jalali = {'year': jalali.jyear, 'month': months[jalali.jmonth - 1], 'day': jalali.jday}

    return jalali


def grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e] for t in itertools.zip_longest(*args))
