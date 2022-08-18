import glob
import os
import re
def extractMostCommonWords():
    print("Extracting the most common words from the text files in this folder")
    wordCount = {}
    for filename in glob.glob('*.txt'):
        with open(os.path.join(os.getcwd(), filename), 'r', encoding='UTF-8') as f: 
            for word in f.read().lower().split():
                word = word.replace(".","")
                word = word.replace(",","")
                word = word.replace(":","")
                word = word.replace("\"","")
                word = word.replace("!","")
                word = word.replace("â€œ","")
                word = word.replace("â€˜","")
                word = word.replace("*","")
                word = word.replace("\xa2", "")
                word = re.sub(r'\[\d+\]', '', word) #Delete timestamps from twitch chat using regular expressions ie: [21345]
                if(word not in wordCount):
                    wordCount[word] = 1
                else: wordCount[word] +=1
                        
    # print(dict(sorted(wordCount.items(), key=lambda item: -item[1])), sep="\n")
    wordAnalizer9000 = dict(sorted(wordCount.items(), key=lambda item: -item[1]))
    #print(wordAnalizer9000)
    with open('Count.txt', 'w+', encoding="utf-8") as f:
        print(('{}\n'*len(sorted(wordCount.items(), key=lambda item: -item[1]))).format(*sorted(wordCount.items(), key=lambda item: -item[1])), file=f,sep="\n")#Rewriting the file each time the script is used.
    print(('{}\n'*len(sorted(wordCount.items(), key=lambda item: -item[1]))).format(*sorted(wordCount.items(), key=lambda item: -item[1])))#Print the words in order, new line for each word into the console


if __name__=="__main__":
    extractMostCommonWords()
