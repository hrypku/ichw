from urllib.request import urlopen
import sys
import collections

def retrieve_page(url):
    """ Retrieve the contents(bytes) of a web page.
        The contents is decoded to a string before returning it.
    """
    my_socket = urlopen(url)
    dta = my_socket.read().decode()
    my_socket.close()
    return dta

def  split_text(text):
    '''Return a list that contains only words.'''
    alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    al= set()
    for i in text:
        if i in alphabet:
            pass
        else:
            al.add(i)

    for i in list(al) :
        text=text.replace(i,' ')
    return text.split()

def wcount(lines, topn=10):
    '''Turn all the words into lower-case letters.
        Return the result of the same width.
    '''
    counts={}
    results = []
    for Word in lines:
        word = Word.lower()
        counts[word]=counts.get(word,0)+1
    lst=collections.Counter(counts).most_common(topn)
    for (a,b) in lst:
        result=a+' '*(12-len(a))+str(b)+'\n'
        results.append(result)
    return ''.join(results)

if __name__ == '__main__':
    #not input url or topn
    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    #input url but not input topn
    elif len(sys.argv) == 2:
        url = sys.argv[1]
        text = retrieve_page(url)
        lines = split_text(text)
        print(wcount(lines))
    #input url and correct topn
    elif len(sys.argv) == 3:
        number = sys.argv[2]
        if number.isdigit():
            url = sys.argv[1]
            text = retrieve_page(url)
            lines = split_text(text)
            print(wcount(lines, int(number)))
        else:
            print('Please input correct number.')
    #wrong input format
    else:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)