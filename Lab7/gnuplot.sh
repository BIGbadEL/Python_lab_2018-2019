set term png
    set out "wykres.png"
    plot "nowy.out" w err, 'plik4.in', 'plik2.in', 'plik0.in', 'plik5.in', 'plik1.in', 'plik3.in' 