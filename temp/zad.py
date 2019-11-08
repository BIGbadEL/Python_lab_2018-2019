import glob


############# 1

def first_n(seq, n):
    wycinek = seq[:n]
    print(wycinek)


def last_n(seq, n):
    wycinek = seq[-n:]
    print(wycinek)


def co_nty_wiersz(seq, n):
    wycinek = seq[::n]
    print(wycinek)


def nty_slowo(seq, n):
    print(list(el.split(" ")[n - 1] for el in seq))


def nty_znak(seq, n):
    print(list(el[n] for el in seq))


with open("plik0.in", "r") as file:
    data = file.readlines()
    first_n(data, 10)
    last_n(data, 10)
    co_nty_wiersz(data, 10)
    nty_slowo(data, 2)
    nty_znak(data, 2)


############# 2

# def print_line_with(str, seq, rep):
#     toPrint = []
#     num = 0
#     for el in seq:
#         if el.startswith(str):
#             toPrint.append(el.replace(str, rep))
#             num = num + 1
#     print(toPrint)
#     print(num)
#
#
# with open("plik0.in", "r") as file:
#     data = file.readlines()
#     print_line_with("27", data, "haha")

############# 3

file_in = glob.glob("*.in")
print(file_in)

files = [open(name, "r") for name in file_in]

with open("nowy.out", "w") as file:
    for el in files[0]:
        line = [el.split()]
        for f in files[1:]:
            line.append(f.readline().split())
        y = [float(number[1]) for number in line]
        file.writelines(line[0][0] + " " + str(sum(y) / len(y)) + " " + str(max(y) - min(y)) + "\n")

for f in files:
    f.close()

############# 4

with open("gnuplot.sh", "w") as file:
    file.write(f"""set term png
    set out "wykres.png"
    plot "nowy.out" w err, {str(file_in).replace("[", "").replace("]", "")} """)

############# 5

all_files = glob.glob("*.py")
print(all_files)
all_words = []
data = []
for f in all_files:
    with open(f, 'r') as pfile:
        data.append(pfile.read())


for word in data[0].split():
    for other in data[1:]:
        if other.find(word) != -1:
            break
    else:
        all_words.append(word)
        for i, other in enumerate(data):
            data[i] = other.replace(word, "")

print(all_words)
############# 6
