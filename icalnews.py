#!/usr/bin/env python

from datetime import date, timedelta
from icalevents import icalparser
from icalevents.icalevents import events
from os import path

def format_date(start: date, end: date, all_day: bool) -> str:
    if all_day:
        if start.year == end.year \
                and start.month == end.month \
                and start.day == end.day:
            # All day, single day
            # Weekday Month DD, YYYY
            return start.strftime('%A %B %e, %Y')
        else:
            # All day, multiple days
            # Weekday Month DD, YYYY to Weekday, Month DD, YYYY
            return start.strftime('%A %B %e, %Y') + ' to ' + end.strftime('%A %B %e, %Y')
    else:
        if start.year == end.year \
                and start.month == end.month \
                and start.day == end.day:
            # Specific time, single day
            # Weekday Month DD, YYYY, HH:MM to HH:MM
            return start.strftime('%A %B %e, %Y, %l:%M') + ' to ' + end.strftime('%l:%M')
        else:
            # Specific times, multiple days
            # Weekday Month DD, YYYY, HH:MM to Weekday Month DD, YYYY, HH:MM
            return start.strftime('%A %B %e, %Y, %l:%M') + ' to ' + end.strftime('%A %B %e, %Y, %l:%M')
    raise RuntimeError('Impossible position reached')

def main(url: str, days: int, template, output):
    start = icalparser.now()
    end = start + timedelta(days=days)

    es = events(url=url, start=start, end=end)

    for ev in es:
        entry = template
        ev = vars(ev)
        ev['timespan'] = format_date(ev['start'], ev['end'], ev['all_day'])

        for key in ev.keys():
            if ev[key]:
                value = str(ev[key])
            else:
                value = '<i style="opacity:70%;">none</i>'
            entry = entry.replace(f'%{key}%', value)
        output.write(entry)

    output.close()

if __name__ == '__main__':
    ical_url = input('iCal URL: ')
    days = int(input('Print events in the next __ days: '))

    template = open(path.join(path.dirname(__file__), 'template.html'), 'r').read()
    with open('output.html', 'w') as output:
        main(ical_url, days, template, output)
