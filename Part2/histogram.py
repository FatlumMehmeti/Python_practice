from os import strerror

try:
    s=open("Part2\\txt_files\\text.txt",'rt',)
    con=s.read().lower()
    dc={}
    for ch in con:
        if ch in dc:
            dc[ch]+=1
        else:
            dc[ch]=1
    s.close()         
    for k in dc:
        print(k,' -> ',dc[k])   
    sorrt_dc = sorted(dc.items(), key=lambda item: (-item[1], item[0]))
    print(sorrt_dc)

    output_filename = "Part2\\txt_files\\text.txt.hist"
    with open(output_filename, 'wt', encoding='utf-8') as out:
        for k, v in sorrt_dc:
           string =str(k)+" ->"+ str(v)+"\n"
           out.write(string)
           print(string, end='')  

    print("\nHistogram saved to:", output_filename)    
except IOError as e:
    print("I/O error occurred: ",strerror(e.errno))        

    