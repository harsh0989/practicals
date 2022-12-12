import random

def genetic(p):
    x=[]
    fx=[]
    for i in range(4):
        s= p[i]
        count= s.count("1")
        x.append(count)
        val= count/10.0
        fx.append(val)
    total= sum(fx)
    avg= total/4.0
    real=[]
    exp=[]
    actual_count=[]
    for i in range(4):
        r= fx[i]/total
        e= fx[i]/avg
        real.append(r)
        exp.append(e)
        ac= round(e)
        actual_count.append(ac)
    print("\nInitial Pop\t x\t f(x)\t f(x)/sum\t f(x)/avg\t Actual Count")
    for i in range(4):
        print(p[i]," "+str(x[i])," "+str(fx[i]),"\t%.3f" %real[i],"\t%.3f\t"%exp[i],actual_count[i], sep=" ")
    min_count= min(exp)
    min_index= exp.index(min_count)
    print("String {} with count {} is rejected\n".format(p[min_index],actual_count[min_index]))
    max_count= max(exp)
    max_index= exp.index(max_count)
    p[min_index]=p[max_index]
    x[min_index]=x[max_index]
    fx[min_index]=fx[max_index]
    real[min_index]=real[max_index]
    exp[min_index]=exp[max_index]
    actual_count[min_index]=exp[max_index]
    return mate(p)
 
def mate(p):
    selection= [0,1,2,3]
    selected= [0,0,0,0]
    mates={}
    first= random.randint(1, 3)
    mates[0]= first
    selected[0]=first
    selected[first]=0
    del selection[0]
    del selection[first-1]
    mates[selection[0]]=selection[1]
    selected[selection[0]]= selection[1]
    selected[selection[1]]= selection[0]
    return crossover(p,mates,selected)
 
def crossover(p,mates,selected):
    new_pop=p.copy()
    for k in mates.keys():
        first= p[k]
        s1_p1= first[0:5]
        s1_p2= first[5:10]
        second= p[mates[k]]
        s2_p1= second[0:5]
        s2_p2= second[5:10]
        str1= s1_p1+s2_p2
        str2= s2_p1+s1_p2
        new_pop[k]=str1
        new_pop[mates[k]]=str2
    print("\n.....Performing Crossover. ... ")
    print("\nPopulation Mate \tCrossover Site \tNew Pop x f(x)")
    for i in range(4):
        print(p[i],selected[i],5," "+new_pop[i],new_pop[i].count("1"),new_pop[i].count("1")/10.0,sep=" ")
    print()
    return mutation(new_pop)
 
def mutation(p):
    before= p.copy()
    loc= random.randint(0,3)
    initial= p[loc]
    mutation= initial.replace("0","1",1)
    p[loc]=mutation
    print("\n.....Performing Mutation .... \n")
    print("\nDue to mutation String {} in New Pop becomes {}\n".format(initial,mutation))
    print("\nBefore mutation x1 \tf(x1)\tAfter mutation \tx2 \tf(x2)")
    k=0.0
    for i in range(4):
        print(before[i]," "+str(before[i].count("1")),before[i].count("1")/10.0,p[i]," "+str(p[i].count("1")),p[i].count("1")/10.0,sep=' ')
        k=k+p[i].count("1")/10.0
    print("Fitness: ",k)
    return p
 
p1= ["0000011100","1000011111","0110101011","1111111011"]
print("------------------First Generation -------------------")
p2= genetic(p1)
print("\n------------------Second Generation -------------------")
p3= genetic(p2)