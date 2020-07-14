import datetime
import properties

creation_date = datetime.datetime.strptime(properties.ZONES['RED'][properties.initial_date],
                                           properties.DATE_FORMAT)

end_date = datetime.datetime.strptime(properties.ZONES['RED'][properties.end_date],
                                      properties.DATE_FORMAT)

print(creation_date)
print(end_date)

range = end_date - creation_date
range /= 60

print(range.total_seconds())

print(range)

creation_date += range

print(creation_date)
