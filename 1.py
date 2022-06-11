import random as rd

WordList = ["ankara","makina","araba","koltuk","top","tren","bilgisayar","telefon","yemek","balina","bardak","istatistik"]

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word = "";
SecretWord = [];
UsedWords = [];
MissingLetters = 0;
Lives = 6;

print(logo);
word = rd.choice(WordList);

for i in word:
    SecretWord+="_";
    MissingLetters +=1;

print(stages[Lives]);
print(SecretWord);

while MissingLetters >0:
    letter = input("Guess a letter: ").lower()
    i=0;
    x = MissingLetters;
    for let in word:
        if(let == letter and SecretWord[i] != letter):
            SecretWord[i] = letter;
            MissingLetters-=1;

        i+=1;
    if(MissingLetters == x):
        Lives -=1;
        if(Lives <= 0):
            print (stages [Lives])
            print("You Lose,The Word Was {}".format(word))
            break;

    print("\n\n\n\n",stages[Lives])
    print(SecretWord);
if(Lives > 0):
    print("You Did it");










