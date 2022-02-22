
file = open("meteorite-landings.csv", "r", encoding="utf-8")
contents = file.read()
file.close()

lines = contents.splitlines()



converters = str, int, str, str, float, str, str, float, float
meteorite_data = []

for j in range(len(lines)-1):
    line = lines[j+1]
    if ",," in line or line.count(",") > 10:
        continue
    meteorite = []
    for i in range(len(converters)):
        data = line.split(",")
        datum = data[i]
        converter_function = converters[i]

        x = converter_function(datum)
        meteorite.append(x)
    meteorite_data.append(meteorite)



def apply(fns):
    function, data = fns
    return function(data)

def error_check(data):
    return not (",," in data or data.count(",") > 10)

def convert(data):
    data = data.split(",")
    zipped = zip(converters, data)
    mapped = list(map(apply, zipped))
    return mapped

x = list(map(convert, filter(error_check, lines[1:])))
print(x)