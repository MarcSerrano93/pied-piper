def no_more_items(list, status, printl = False):
    res = False
    if (printl):
        print("LIST ITEMS")
    for l in list:
        if (printl):
            print(f"Film: {l.title} - {l.status}")
    for l in list:
        if l.status.value <= status.value:
            res = True
            break
    return res