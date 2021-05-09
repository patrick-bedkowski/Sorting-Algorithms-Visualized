from quick_sort import quick_sort
from file_management import read_txt_file

data1000 = read_txt_file('files/pan-tadeusz.txt', 1000)
data2000 = read_txt_file('files/pan-tadeusz.txt', 2000)
data3000 = read_txt_file('files/pan-tadeusz.txt', 3000)
data4000 = read_txt_file('files/pan-tadeusz.txt', 4000)
data5000 = read_txt_file('files/pan-tadeusz.txt', 5000)
data6000 = read_txt_file('files/pan-tadeusz.txt', 6000)
data7000 = read_txt_file('files/pan-tadeusz.txt', 7000)
data8000 = read_txt_file('files/pan-tadeusz.txt', 8000)
data9000 = read_txt_file('files/pan-tadeusz.txt', 9000)
data10000 = read_txt_file('files/pan-tadeusz.txt', 10000)


def test_quick_tadeusz_1000(benchmark):
    result = benchmark(quick_sort, data1000)
    assert result == sorted(data1000)


def test_quick_tadeusz_2000(benchmark):
    result = benchmark(quick_sort, data2000)
    assert result == sorted(data2000)


def test_quick_tadeusz_3000(benchmark):
    result = benchmark(quick_sort, data3000)
    assert result == sorted(data3000)


def test_quick_tadeusz_4000(benchmark):
    result = benchmark(quick_sort, data4000)
    assert result == sorted(data4000)


def test_quick_tadeusz_5000(benchmark):
    result = benchmark(quick_sort, data5000)
    assert result == sorted(data5000)


def test_quick_tadeusz_6000(benchmark):
    result = benchmark(quick_sort, data6000)
    assert result == sorted(data6000)


def test_quick_tadeusz_7000(benchmark):
    result = benchmark(quick_sort, data7000)
    assert result == sorted(data7000)


def test_quick_tadeusz_8000(benchmark):
    result = benchmark(quick_sort, data8000)
    assert result == sorted(data8000)


def test_quick_tadeusz_9000(benchmark):
    result = benchmark(quick_sort, data9000)
    assert result == sorted(data9000)


def test_quick_tadeusz_10000(benchmark):
    result = benchmark(quick_sort, data10000)
    assert result == sorted(data10000)
