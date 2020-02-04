import os
for p in os.listdir('./src/'):
    filedir = p.replace('.txt', '')
    #os.mkdir(filedir)
    f = open('./src/' + p, 'r')
    idx = 0
    for url in f:
        os.system('you-get -s 127.0.0.1:1080 --itag=137 -o ' + filedir + ' ' + url)
    print(p + ':done')
