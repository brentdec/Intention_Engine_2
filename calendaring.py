from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone

cal = Calendar()
cal.add('prodid', '-//Brents Practice ICS File//')
cal.add('version', '2.0')

event = Event()
event.add('summary', 'Python meeting about calendaring')
event.add('dtstart', datetime(2018,6,19,14,48,0,tzinfo='US/Pacific'))
event.add('dtend', datetime(2018,6,19,22,0,0,tzinfo=UTC))
event.add('dtstamp', datetime(2018,6,19,14,48,0,tzinfo=UTC))
event['uid'] = 'brent.decracker@icloud.com'
event.add('priority', 5)

cal.add_component(event)

f = open('example.ics', 'wb')
f.write(cal.to_ical())
f.close()