from jovian.pythondsa import evaluate_test_case, evaluate_test_cases
def locate(cards,query):
    position=0
    while position<len(cards):
        print("hello")
        if cards[position]==query:
            return position
        position+=1
        if position==len(cards):
            return -1
    return -1
test1={"input":{'cards':[10,11,23,52,74,1],'query':1},'output':5}
test2={"input":{'cards':[10,11,23,52,12,12,12],'query':12},'output':4}
test3={"input":{'cards':[10,10,10,10,11,23,52,74,1],'query':11},'output':4}
test4={"input":{'cards':[],'query':1},'output':-1}
test4={"input":{'cards':[10,10,10,10,11,23,52,74,1],'query':None},'output':-1}
tests=[]
tests.append(test1)
tests.append(test2)
tests.append(test3) 
tests.append(test4)
print(evaluate_test_case(locate,test2,display=False))
