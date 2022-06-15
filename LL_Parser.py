import string
from js import console

# sentence = input()

non_term = ['S', 'N', 'V', 'O']
term = ['cang', 'cai', 'ia', 
        'nginem', 'ngutgut', 'ningeh', 
        'lipi', 'woh', 'wit', 'be']

parse_tab = {}

parse_tab[('S', 'cang')] = ['N', 'V', 'O']
parse_tab[('S', 'cai')] = ['N', 'V', 'O']
parse_tab[('S', 'ia')] = ['N', 'V', 'O']
parse_tab[('S', 'nginem')] = ['error']
parse_tab[('S', 'ngutgut')] = ['error']
parse_tab[('S', 'ningeh')] = ['error']
parse_tab[('S', 'lipi')] = ['error']
parse_tab[('S', 'woh')] = ['error']
parse_tab[('S', 'wit')] = ['error']
parse_tab[('S', 'be')] = ['error']
parse_tab[('S', 'EOS')] = ['error']

parse_tab[('N', 'cang')] = ['cang']
parse_tab[('N', 'cai')] = ['cai']
parse_tab[('N', 'ia')] = ['ia']
parse_tab[('N', 'nginem')] = ['error']
parse_tab[('N', 'ngutgut')] = ['error']
parse_tab[('N', 'ningeh')] = ['error']
parse_tab[('N', 'lipi')] = ['error']
parse_tab[('N', 'woh')] = ['error']
parse_tab[('N', 'wit')] = ['error']
parse_tab[('N', 'be')] = ['error']
parse_tab[('N', 'EOS')] = ['error']

parse_tab[('V', 'cang')] = ['error']
parse_tab[('V', 'cai')] = ['error']
parse_tab[('V', 'ia')] = ['error']
parse_tab[('V', 'nginem')] = ['nginem']
parse_tab[('V', 'ngutgut')] = ['ngutgut']
parse_tab[('V', 'ningeh')] = ['ningeh']
parse_tab[('V', 'lipi')] = ['error']
parse_tab[('V', 'woh')] = ['error']
parse_tab[('V', 'wit')] = ['error']
parse_tab[('V', 'be')] = ['error']
parse_tab[('V', 'EOS')] = ['error']

parse_tab[('O', 'cang')] = ['error']
parse_tab[('O', 'cai')] = ['error']
parse_tab[('O', 'ia')] = ['error']
parse_tab[('O', 'nginem')] = ['error']
parse_tab[('O', 'ngutgut')] = ['error']
parse_tab[('O', 'ningeh')] = ['error']
parse_tab[('O', 'lipi')] = ['lipi']
parse_tab[('O', 'woh')] = ['woh']
parse_tab[('O', 'wit')] = ['wit']
parse_tab[('O', 'be')] = ['be']
parse_tab[('O', 'EOS')] = ['error']

def get_sentence(*args, **kwargs):
    global sentence
    console.log(f'args: {args}')
    console.log(f'kwargs: {kwargs}')
    sentence = Element('test-input').element.value
    console.log(f'sentence: {sentence}')
    Element('output').element.innerText = "termsError, kata tidak ditemukan"

def parser(*args, **kwargs):
    global trans_tab
    global sentence
    get_sentence()
    token = sentence.lower().split()
    token.append('EOS')
    stack = []
    stack.append('#')
    stack.append('S')
    hasil = ""

    i = 0
    symbol = token[i]

    while (len(stack) > 0):
        top = stack[len(stack) - 1]
        hasil+= f'top = {top}\n'
        hasil+= f'symbol = {symbol}\n'
        if top in term:
            hasil+='top stack is a terminal symbol\n'
            if top == symbol:
                stack.pop()
                i = i + 1
                symbol = token[i]
                if symbol == 'EOS':
                    hasil+=f'Stack = {stack}\n'
                    stack.pop()
            else:
                hasil+='error\n'
                break
        elif top in non_term:
            hasil+='top stack is a non terminal symbol\n'
            if parse_tab[(top, symbol)][0] != 'error':
                stack.pop()
                pushed_symbol = parse_tab[(top, symbol)]
                for j in range(len(pushed_symbol)-1,-1,-1):
                    stack.append(pushed_symbol[j])
            else:
                hasil+='error\n'
                break
        else:
            hasil+='error\n'
            break
        hasil+=f'stack elements = {stack}\n\n'

    if symbol == 'EOS' and len(stack) == 0:
        verdict =f'input string {sentence} diterima, sesuai dengan grammar\n'
        valid = True
    else:
        verdict =f'error, input string = {sentence}, tidak sesuai grammar\n'
        valid = False
    Element('output').element.innerText = verdict
    return hasil, verdict, valid