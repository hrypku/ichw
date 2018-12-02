from urllib.request import urlopen


# Part A: Breaking Up Strings
def before_space(s):
    """return substring of s, but not including the first space"""

    return s.split(' ', 1)[0]


def after_space(s):
    """return substring of s after the first space"""

    return s.split(' ', 1)[1]


# Part B: Processing a JSON String
def first_inside_quotes(s):
    """return the first substring of s between two (double) quote characters"""

    first_quote = s.find('"')
    second_quote = s.find('"', (first_quote + 1))
    return s[first_quote + 1:second_quote]


def get_from(json):
    """return the FROM value in the response to a currency query"""

    index_of_from = json.find('from')
    return first_inside_quotes(json[index_of_from + 5:])


def get_to(json):
    """return the TO value in the response to a currency query"""

    index_of_to = json.find('to')
    return first_inside_quotes(json[index_of_to + 3:])


def has_error(json):
    """return True if the query has an error; False otherwise"""

    return True if get_from(json) == "" else False


# Part C: Currency Query
def currency_response(currency_from, currency_to, amount_from):
    """return a JSON string that is a response to a currency query"""

    url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' \
          + currency_from + '&to=' + currency_to + '&amt=' + str(amount_from)
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    return docstr.decode('ascii')


# Part D: Currency Exchange
def iscurrency(currency):
    """return True if currency is a valid (3 letter code for a) currency.
    It returns False otherwise."""
    
    json = currency_response('USD', currency, 1)
    return False if has_error(json) else True


def exchange(currency_from, currency_to, amount_from):
    """return amount of currency received in the given exchange"""

    if iscurrency(currency_from) and iscurrency(currency_to):
        try:
            float(amount_from)
        except ValueError:
            print('Input is not a number')
        #test the legitimacy of the user's input
        json = currency_response(currency_from, currency_to, amount_from)
        return float(before_space(get_to(json)))
    else:
        'This is not currency!'

# TEST Part A
def test_before_space():
    """test function before_space"""
    #Case 1
    str1 = '2.5 United States Dollars'
    str1_before = '2.5'
    assert str1_before == before_space(str1)
    
    #Case2
    str2 = 'United States'
    str2_before = 'United'
    assert str2_before == before_space(str2)


def test_after_space():
    """test function after_space"""
    #Case 1
    str1 = '2.5 United States Dollars'
    str1_after = 'United States Dollars'
    assert str1_after == after_space(str1)

    #Case2
    str2 = 'United States'
    str2_after = 'States'
    assert str2_after == after_space(str2)


def test_A():
    """test module A"""
    test_after_space()
    test_before_space()


#TEST Part B
def test_first_inside_quotes():
    '''test function first_inside_quotes'''
    #Case 1
    str1='A "B C" D'
    str1_first='B C'
    assert str1_first==first_inside_quotes(str1)

    #Case2
    str2='A "B C" D "E F" G'
    str2_first='B C'
    assert str2_first==first_inside_quotes(str2)

def test_B():
    """test module B"""
    test_first_inside_quotes()

#TEST Part C
def test_currency_response():
    '''test function currency_response'''
    #Case 1
    str1='{ "from" : "1 United States Dollar", "to" : "6.8521 Chinese Yuan", "success" : true, "error" : "" }'
    assert str1==currency_response('USD','CNY',1)

    #Case 2
    str2='{ "from" : "1 New Zealand Dollar", "to" : "0.65521138757392 Panamanian Balboas", "success" : true, "error" : "" }'
    assert str2==currency_response('NZD','PAB',1)

def test_C():
    """test module C"""
    test_currency_response()

#TEST Part D
def test_iscurrency():
    '''test function iscurrency'''
    #Case 1
    assert True==iscurrency('PAB')

    #Case 2
    assert False==iscurrency('US')
    
def test_exchange():
    '''test function exchange'''
    #Case 1
    assert exchange('USD','CNY',1)==6.8521

    #Case 2
    assert exchange('NZD','PAB',1)==0.65521138757392

def test_D():
    """test module D"""
    test_iscurrency()
    test_exchange()

#TEST ALL
def testAll():
    """test all cases"""

    test_A()
    test_B()
    test_C()
    test_D()
    print("All tests passed")

#User input
def main():
    testAll()
    currency_from=input('Please input currency from:')
    currency_to=input('Please input currency to:')
    amount_from=input('Please input amount from:')
    print (exchange(currency_from, currency_to, amount_from))

main()

