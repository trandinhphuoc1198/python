class Question:
    def __init__(self,cau_hoi,answer):
        self.cau_hoi = cau_hoi
        self.answer = answer
cauhoi1 = [
    "trai tao co mau gi \n a/mau do\nb/mau xanh\n",
    "trai nho co mau gi\na/mau do\nb/mau tim\n",
]
cauhoine = [
    Question(cauhoi1[0],"a"),
    Question(cauhoi1[1],"b")
]
def run(cauhoine):
    score=0
    for ques in cauhoine:
        if str.lower(input((ques.cau_hoi)))==ques.answer:
            score+=1
    print("so diem ban dat la: "+ str(score)+"/" +str(len(cauhoine)))
run(cauhoine)