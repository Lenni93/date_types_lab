import math

centuries = int(input())

years = centuries * 100
days = math.floor(36524.22 * centuries)
hours = days * 24
minutes = hours * 60
print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')
