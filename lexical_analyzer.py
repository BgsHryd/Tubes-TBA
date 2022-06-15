import string
from js import console

alphabet = string.ascii_lowercase + " "
states_list = ["start", "q1", "q2", "q3", "q4", "q5",
                "r0", "r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "r10",
                "r11", "r12", "r13", "s1", "s2", "s3", "s4", "s5", "s6", "s7", "accept"]

'''
S → N V O 
N → cang | cai | ia
V → nginem | ngutgut | ningeh
O → lipi | woh | wit | be
'''

trans_tab = {}
for state in states_list:
    for char in alphabet:
        trans_tab[(state, char)] = "error" 
    trans_tab[(state, "#")] = "error"
    trans_tab[(state, " ")] = "error"

trans_tab[("start", " ")] = "start"

# cai
trans_tab[("start", "c")] = "q1"
trans_tab[("r0", "c")] = "q1"
trans_tab[("q1", "a")] = "q2"
trans_tab[("q2", "i")] = "q5"

# cang
trans_tab[("start", "c")] = "q1"
trans_tab[("r0", "c")] = "q1"
trans_tab[("q1", "a")] = "q2"
trans_tab[("q2", "n")] = "q3"
trans_tab[("q3", "g")] = "q5"

# ia
trans_tab[("start", "i")] = "q4"
trans_tab[("r0", "i")] = "q4"
trans_tab[("q4", "a")] = "q5"

# nginem
trans_tab[("start", "n")] = "r1"
trans_tab[("r0", "n")] = "r1"
trans_tab[("r1", "g")] = "r2"
trans_tab[("r2", "i")] = "r3"
trans_tab[("r3", "n")] = "r4"
trans_tab[("r4", "e")] = "r5"
trans_tab[("r5", "m")] = "q5"

# ngutgut
trans_tab[("start", "n")] = "r1"
trans_tab[("r0", "n")] = "r1"
trans_tab[("r1", "g")] = "r2"
trans_tab[("r2", "u")] = "r6"
trans_tab[("r6", "t")] = "r7"
trans_tab[("r7", "g")] = "r8"
trans_tab[("r8", "u")] = "r9"
trans_tab[("r9", "t")] = "q5"

#ningeh
trans_tab[("start", "n")] = "r1"
trans_tab[("r0", "n")] = "r1"
trans_tab[("r1", "i")] = "r10"
trans_tab[("r10", "n")] = "r11"
trans_tab[("r11", "g")] = "r12"
trans_tab[("r12", "e")] = "r13"
trans_tab[("r13", "h")] = "q5"

# lipi
trans_tab[("start", "l")] = "s1"
trans_tab[("r0", "l")] = "s1"
trans_tab[("s1", "i")] = "s2"
trans_tab[("s2", "p")] = "s3"
trans_tab[("s3", "i")] = "q5"

# woh
trans_tab[("start", "w")] = "s4"
trans_tab[("r0", "w")] = "s4"
trans_tab[("s4", "o")] = "s5"
trans_tab[("s5", "h")] = "q5"

# wit
trans_tab[("start", "w")] = "s4"
trans_tab[("r0", "w")] = "s4"
trans_tab[("s4", "i")] = "s6"
trans_tab[("s6", "t")] = "q5"

# be
trans_tab[("start", "b")] = "s7"
trans_tab[("r0", "b")] = "s7"
trans_tab[("s7", "e")] = "q5"

# transition to EOS (#)
trans_tab["q5", " "] = "r0"
trans_tab["q5", "#"] = "accept"
trans_tab["r0", " "] = "r0"
trans_tab["r0", "#"] = "accept"

def lexical_analyzer(*args):
    global trans_tab
    global sentence
    get_sentence()
    input_sentence = sentence + "#"
    index_ch = 0
    state = 'start'
    current_token = ''
    hasil = ""

    while state != 'accept':
      current_char = input_sentence[index_ch]
      current_token += current_char
      
      state = trans_tab[(state, current_char)]
      if state == 'q5' or state == 'r0' and current_char != ' ':
          hasil+=f'token: {current_token} valid\n'
          current_token = ''
      elif state == 'error':
          hasil+=f'token: {current_token} tidak valid\n'
          break
      index_ch += 1

    if state == 'accept':
      verdict =f'semua token di kalimat: "{sentence}" valid\n'
      valid = True
    else:
      verdict =f'input kalimat: "{sentence}" tidak valid\n'
      valid = False
    # Element('output').element.innerText = hasil + verdict
    return hasil, verdict, valid

def get_sentence(*args, **kwargs):
    global sentence
    console.log(f'args: {args}')
    console.log(f'kwargs: {kwargs}')
    sentence = Element('test-input').element.value
    console.log(f'sentence: {sentence}')
    Element('output').element.innerText = sentence