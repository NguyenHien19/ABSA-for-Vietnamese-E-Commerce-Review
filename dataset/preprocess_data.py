import json
from typing import DefaultDict

with open("../dataset/UIT-ViSFD/train.json", 'r', encoding = 'utf-8') as f:
    all_data = []
    data = json.load(f)
    for d in data:
        #print(d)
        head = list(d['head']) 
        max=len(head)
        #print(max)
        tmp = [[0]*max for _ in range(max)]  
        for i in range(max): 
            j=head[i]
            if j==0:
                continue
            tmp[i][j-1]=1
            tmp[j-1][i]=1
        
        tmp_dict = DefaultDict(list)
        
        
        for i in range(max):
            for j in range(max):
                if tmp[i][j] == 1:
                    tmp_dict[i].append(j)  
        #print(tmp_dict)
        #print(len(tmp_dict))
        leverl_degree = [[5]*max for _ in range(max)]

        for i in range(max):
            node_set = set()
            leverl_degree[i][i]=0
            node_set.add(i)
            for j in tmp_dict[i]:
                if j not in node_set:
                    leverl_degree[i][j]=1
                    #print(word_leverl_degree)
                    node_set.add(j)
                for k in tmp_dict[j]:
                    #print(tmp_dict[j])
                    if k not in node_set:
                        leverl_degree[i][k] = 2
                        #print(word_leverl_degree)
                        node_set.add(k)
                        for g in tmp_dict[k]:
                            if g not in node_set:
                                leverl_degree[i][g] = 3
                                #print(word_leverl_degree)
                                node_set.add(g) 
                                for q in tmp_dict[g]:
                                    if q not in node_set:
                                       leverl_degree[i][q] = 4
                                       #print(word_leverl_degree)
                                       node_set.add(q) 
        
        d['short'] = leverl_degree
        #print(d['short'])
        #print(len(d['short']))

    wf = open('../dataset/UIT-ViSFD/train_write.json', 'w', encoding = 'utf-8')
    wf.write(json.dumps(data, indent=4, ensure_ascii=False))
    wf.close()

with open("../dataset/UIT-ViSFD/test.json", 'r', encoding = 'utf-8') as f:
    all_data = []
    data = json.load(f)
    for d in data:
        head = list(d['head']) 
        max=len(head)
        tmp = [[0]*max for _ in range(max)]  
        for i in range(max): 
            j=head[i]
            if j==0:
                continue
            tmp[i][j-1]=1
            tmp[j-1][i]=1
        
        tmp_dict = DefaultDict(list)
        
        for i in range(max):
            for j in range(max):
                if tmp[i][j] == 1:
                    tmp_dict[i].append(j)  

        leverl_degree = [[5]*max for _ in range(max)]

        for i in range(max):
            node_set = set()
            leverl_degree[i][i]=0
            node_set.add(i)
            for j in tmp_dict[i]:
                if j not in node_set:
                    leverl_degree[i][j]=1
                    #print(word_leverl_degree)
                    node_set.add(j)
                for k in tmp_dict[j]:
                    #print(tmp_dict[j])
                    if k not in node_set:
                        leverl_degree[i][k] = 2
                        #print(word_leverl_degree)
                        node_set.add(k)
                        for g in tmp_dict[k]:
                            if g not in node_set:
                                leverl_degree[i][g] = 3
                                #print(word_leverl_degree)
                                node_set.add(g) 
                                for q in tmp_dict[g]:
                                    if q not in node_set:
                                       leverl_degree[i][q] = 4
                                       #print(word_leverl_degree)
                                       node_set.add(q) 
        d['short'] = leverl_degree


    wf = open('../dataset/UIT-ViSFD/test_write.json', 'w', encoding = 'utf-8')
    wf.write(json.dumps(data, indent=4, ensure_ascii=False))
    wf.close()

####################################

with open("../dataset/UIT-ViSD4SA/train.json", 'r', encoding = 'utf-8') as f:
    all_data = []
    data = json.load(f)
    for d in data:
        #print(d)
        head = list(d['head']) 
        max=len(head)
        #print(max)
        tmp = [[0]*max for _ in range(max)]  
        for i in range(max): 
            j=head[i]
            if j==0:
                continue
            tmp[i][j-1]=1
            tmp[j-1][i]=1
        
        tmp_dict = DefaultDict(list)
        
        
        for i in range(max):
            for j in range(max):
                if tmp[i][j] == 1:
                    tmp_dict[i].append(j)  
        #print(tmp_dict)
        #print(len(tmp_dict))
        leverl_degree = [[5]*max for _ in range(max)]

        for i in range(max):
            node_set = set()
            leverl_degree[i][i]=0
            node_set.add(i)
            for j in tmp_dict[i]:
                if j not in node_set:
                    leverl_degree[i][j]=1
                    #print(word_leverl_degree)
                    node_set.add(j)
                for k in tmp_dict[j]:
                    #print(tmp_dict[j])
                    if k not in node_set:
                        leverl_degree[i][k] = 2
                        #print(word_leverl_degree)
                        node_set.add(k)
                        for g in tmp_dict[k]:
                            if g not in node_set:
                                leverl_degree[i][g] = 3
                                #print(word_leverl_degree)
                                node_set.add(g) 
                                for q in tmp_dict[g]:
                                    if q not in node_set:
                                       leverl_degree[i][q] = 4
                                       #print(word_leverl_degree)
                                       node_set.add(q) 
        
        d['short'] = leverl_degree
        #print(d['short'])
        #print(len(d['short']))

    wf = open('../dataset/UIT-ViSD4SA/train_write.json', 'w', encoding = 'utf-8')
    wf.write(json.dumps(data, indent=4, ensure_ascii=False))
    wf.close()

with open("../dataset/UIT-ViSD4SA/test.json", 'r', encoding = 'utf-8') as f:
    all_data = []
    data = json.load(f)
    for d in data:
        head = list(d['head']) 
        max=len(head)
        tmp = [[0]*max for _ in range(max)]  
        for i in range(max): 
            j=head[i]
            if j==0:
                continue
            tmp[i][j-1]=1
            tmp[j-1][i]=1
        
        tmp_dict = DefaultDict(list)
        
        for i in range(max):
            for j in range(max):
                if tmp[i][j] == 1:
                    tmp_dict[i].append(j)  

        leverl_degree = [[5]*max for _ in range(max)]

        for i in range(max):
            node_set = set()
            leverl_degree[i][i]=0
            node_set.add(i)
            for j in tmp_dict[i]:
                if j not in node_set:
                    leverl_degree[i][j]=1
                    #print(word_leverl_degree)
                    node_set.add(j)
                for k in tmp_dict[j]:
                    #print(tmp_dict[j])
                    if k not in node_set:
                        leverl_degree[i][k] = 2
                        #print(word_leverl_degree)
                        node_set.add(k)
                        for g in tmp_dict[k]:
                            if g not in node_set:
                                leverl_degree[i][g] = 3
                                #print(word_leverl_degree)
                                node_set.add(g) 
                                for q in tmp_dict[g]:
                                    if q not in node_set:
                                       leverl_degree[i][q] = 4
                                       #print(word_leverl_degree)
                                       node_set.add(q) 
        d['short'] = leverl_degree


    wf = open('../dataset/UIT-ViSD4SA/test_write.json', 'w', encoding = 'utf-8')
    wf.write(json.dumps(data, indent=4, ensure_ascii=False))
    wf.close()
