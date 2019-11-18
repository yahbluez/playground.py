def shrink_list(list_in):
    list_res = []
    i = 0
    while i < len(list_in):
        if i % 2 == 0:
            list_res.append(list_in[i])
        i += 1

    if(len(list_in) % 2):
        list_res.insert(0,list_res.pop())

    if(len(list_res) > 1):
        return(shrink_list(list_res))
    else:
        return(list_res)


print(shrink_list([x for x in range(1600)]))

