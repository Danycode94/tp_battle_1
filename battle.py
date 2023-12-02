import re

chenn = "badio ap challenge 02 0  dec 2023"

n = re.findall("\d+", chenn)

print(n)