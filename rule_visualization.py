from graphviz import Digraph

t3=0.07
ig=3
fo=2
som=3.5
somw=0.15
somc=400
exception1=0.07/2.5
exception2=70
maxds=80
wth=0.05
t3=t3
ignore_threshold=ig
far_overlap_threshold=fo
som_threshold=som
som_weight_threshold=somw
som_cov_threshold=somc
far_overlap_exception1=exception1
far_overlap_exception2=exception2
maxd_threshold=maxds
weight_threshold=wth

n_components=3
n_heavy=3
n_light=2
n_bands=n_heavy+n_light
g = Digraph('HandCraftedRuleVisualization')
for i in range(n_bands):#第几个条带，一共5条
    for j in range(3):#weight，mean，var依次
        for l in range(n_components):#第几个component，共3个
            g.node(name=str(i)+"_"+str(j)+"_"+str(l),shape="box")

for i in range(n_bands):
    g.node(name="max_d"+"_"+str(i),shape="box")
for i in range(1+n_heavy*n_light+n_bands):
    g.node(name="ans"+"_"+str(i),shape="box")
for i in range(n_bands):
    for j in range(n_components):
        g.node(name="pre"+"_"+str(i)+"_"+str(j),shape="box")
        g.node(name="newweights"+"_"+str(i)+"_"+str(j),shape="box")

for i in range(n_bands):
    if i>0:
        continue
    ###preprocessing the data to avoid peak overlapping(far overlap and near overlap) influence: identify far/near overlap cases and suppress far overlap peaks, amplify near overlap peaks
    ###如果很理想的情况应该能把两个far overlap的peak合并成一个在中间mean的，但是现在可以先直接把两个抑制掉，毕竟就不太可能是单克隆峰了。far overlap也就是两个峰实际上在图里面是同一个，BGM将其拆分从而更好的拟合高斯模型，我们这里将其抑制因为能够拆分为两个峰的基本上cov都比较大，不尖。
    for j in range(n_components):
        for l in range(n_components):
            if l>1:
                continue
            if j<l:
                g.node(name="w"+str(i)+str(j)+str(l)+"ignore",label="weight"+str(i)+str(j)+"/"+"weight"+str(i)+str(l)+">or<reciprocal"+str(ignore_threshold))
                g.edge(str(i)+"_"+str(0)+"_"+str(j),"w"+str(i)+str(j)+str(l)+"ignore")
                g.edge(str(i)+"_"+str(0)+"_"+str(l),"w"+str(i)+str(j)+str(l)+"ignore")
                g.node(name="nearoverlap"+str(i)+str(j)+str(l),label="var"+str(i)+str(j)+"/"+"var"+str(i)+str(l)+"*w"+str(i)+str(j)+"/"+"w"+str(i)+str(l)+"/"+"|means"+str(i)+str(j)+"-means"+str(i)+str(l)+"|"+"*mean of 2 std"+str(i)+str(j)+str(l)+">or<reciprocal"+str(far_overlap_threshold))
                g.edge("w"+str(i)+str(j)+str(l)+"ignore","nearoverlap"+str(i)+str(j)+str(l),label="no:next step")
                g.edge(str(i)+"_"+str(0)+"_"+str(j),"nearoverlap"+str(i)+str(j)+str(l))
                g.edge(str(i)+"_"+str(0)+"_"+str(l),"nearoverlap"+str(i)+str(j)+str(l))
                g.edge(str(i)+"_"+str(1)+"_"+str(j),"nearoverlap"+str(i)+str(j)+str(l))
                g.edge(str(i)+"_"+str(1)+"_"+str(l),"nearoverlap"+str(i)+str(j)+str(l))
                g.edge("nearoverlap"+str(i)+str(j)+str(l),"newweights"+"_"+str(i)+"_"+str(j),label="yes:do near overlap")
                g.edge("nearoverlap"+str(i)+str(j)+str(l),"newweights"+"_"+str(i)+"_"+str(l),label="yes:do near overlap on weights")
                g.node(name="far1"+str(i)+str(j)+str(l),label="var"+str(i)+str(j)+"/"+"w"+str(i)+str(j)+"<or the other one"+str(far_overlap_exception1))
                g.edge(str(i)+"_"+str(0)+"_"+str(j),"far1"+str(i)+str(j)+str(l))
                g.edge(str(i)+"_"+str(0)+"_"+str(l),"far1"+str(i)+str(j)+str(l))
                g.edge(str(i)+"_"+str(2)+"_"+str(j),"far1"+str(i)+str(j)+str(l))
                g.edge(str(i)+"_"+str(2)+"_"+str(l),"far1"+str(i)+str(j)+str(l))
                g.node(name="far2"+str(i)+str(j)+str(l),label="var"+str(i)+str(j)+"<or the other one"+str(far_overlap_exception2))
                g.edge(str(i)+"_"+str(2)+"_"+str(j),"far2"+str(i)+str(j)+str(l))
                g.edge(str(i)+"_"+str(2)+"_"+str(l),"far2"+str(i)+str(j)+str(l))
                g.edge("far1"+str(i)+str(j)+str(l),"far2"+str(i)+str(j)+str(l),label="no:nextstep")
                g.node(name="far3"+str(i)+str(j)+str(l),label="|means"+str(i)+str(j)+"-means"+str(i)+str(l)+"|"+"<"+str(som_threshold)+"*the larger std")
                g.edge(str(i)+"_"+str(1)+"_"+str(j),"far3"+str(i)+str(j)+str(l))
                g.edge(str(i)+"_"+str(1)+"_"+str(l),"far3"+str(i)+str(j)+str(l))
                g.edge(str(i)+"_"+str(2)+"_"+str(j),"far3"+str(i)+str(j)+str(l))
                g.edge(str(i)+"_"+str(2)+"_"+str(l),"far3"+str(i)+str(j)+str(l))
                g.edge("far2"+str(i)+str(j)+str(l),"far3"+str(i)+str(j)+str(l),label="no:nextstep")
                g.edge("far3"+str(i)+str(j)+str(l),"pre"+"_"+str(i)+"_"+str(j),label="=1")
                g.edge("far3"+str(i)+str(j)+str(l),"pre"+"_"+str(i)+"_"+str(l),label="=1")
for i in range(n_bands):
    for j in range(n_components):
        if i>0 or j>0:
            continue
        g.edge("pre"+"_"+str(i)+"_"+str(j),"ans"+"_"+str(7+i),label="any pre=1, ans=0")
        g.edge(str(i)+"_"+str(0)+"_"+str(j),"ans"+"_"+str(7+i),label="check if all is too small")
        g.edge(str(i)+"_"+str(0)+"_"+str(j),"ans"+"_"+str(7+i),label="check if all is too small")
        g.node(name="if sharp"+str(i)+str(j),label="var"+str(i)+str(j)+"/"+"weight"+str(i)+str(j)+">"+str(t3))
        g.edge("if sharp"+str(i)+str(j),"ans"+"_"+str(7+i),label="no:ans=1")

g.view()
print()