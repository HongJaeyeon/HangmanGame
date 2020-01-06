import random
#단어가 있는 파일을 열고 라인으로 읽어들여서 단어로 나눔, 단어 리스트와 단어 개수를 최종적으로 받음
class Word:

    def __init__(self,filename):
        self.words = []
        f = open(filename,'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            self.words.append(line.rstrip()) #rstrip 사전에서 불러왔을 때 불필요한 것들 제거
            self.count += 1

        print('%d words in DB' %self.count)

    def test(self):
        return 'default'

    def randFromDB(self):
        r = random.randrange(self.count)
        return self.words[r]
    #self.count는 단어 개수, 그 단어 개수 범위 내에서 랜덤한 숫자 하나가 r
    #그 r을 단어들이 들어있는 리스트 self.words의 인덱스로 넣음
     
