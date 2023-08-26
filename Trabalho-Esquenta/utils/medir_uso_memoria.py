import psutil

def medirUsoMemoria():
    return psutil.Process().memory_info().rss

