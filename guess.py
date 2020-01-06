class Guess:

    def __init__(self,word):
        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0 #틀린 횟수
        self.currentStatus = "_" * len(word)

    def display(self):
        print("Current :", self.currentStatus) #현재 상태
        print("Tries : ", self.numTries)

    def guess(self,character) :
        # character 사용자가 입력한 단어

        #주어진 글자를 사용한 글자의 집합에 원소로 추가
        self.guessedChars.append(character)

        #비밀 단어에 주어진 글자가 없으면 실패한 회수가 증가
        if character not in self.secretWord:
            self.numTries +=1

        #지금까지 알아낸 글자와 그 위치를 나타내는 데이터를 갱신
        for i in range(len(self.secretWord)):
            if self.secretWord[i] == character:
                self.currentStatus = self.currentStatus[0:i] + self.secretWord[i] + self.currentStatus[i+1:]

        #위에서 갱신한 데이터가 모든 위치의 글자를 알아낸 경우에 해당하면 True를, 그렇지 않으면 False 를 리턴
        return '_' not in self.currentStatus
