import time
print('<< Made by Jamie Grey for Gold CREST Award >>\n\n')
time.sleep(2)
def menu():
  try:
    m = int(input("""Welcome to Intelligent T C:
  1) Review your terms and conditions (experimental)
  2) Review google's T C (Jan 5, 2022) or gov.uk's T C
  3) Advice on terms and conditions
   """))
  except ValueError:
    print('Try again: Enter a number\n')
    menu()
  
  if m == 1:
    main(True)
  elif m == 2:
    main(False)
  elif m == 3:
    advice()
  else:
    print('Numbers 1 to 3 only\n')
    menu()

def openfile(filename):
  with open(filename, 'r') as f:
    text = f.read()
    word = []
    l_wordlist = []
    for letter in text:
      if letter != ' ':
        if letter.isalnum() or letter == '.' or letter == '\'':
          word.append(letter)
      else:
        l_wordlist.append(word)
        word = []
    
    wordlist=[]
    for word in l_wordlist:
      x=''
      for letter in word:
        x = x +letter
      wordlist.append(x)

  #  print(wordlist)
    f.close()
  return wordlist


def check(clauses,wordlist):

  for i in clauses:
   for j in range(len(wordlist)):
     if i == wordlist[j].lower():
       try:
          loop = True
          k = j
          m=j
          while loop:
            k = k-1
            for letter in wordlist[k]:
              if letter == '.' :
                loop == False
            if (j-k) > 15:
              loop = False

          loop = True
          while loop:
            m = m+1
            for letter in wordlist[m]:
              if letter == '.' or m-j > 15:
                loop = False
          
          imp = False
          for n in range(k+1,m+1):
            # if wordlist[n]=='':
            #   print('\n')
            
            # for letter in wordlist[n]:
            #   if letter.isupper():
            #     for letter in wordlist[n]:
            #       if letter.isupper():
            #         print('\n')
            #         continue
            #       print(letter,end='')
            
            if i == wordlist[n]:
              print(f"\033[1;32m{i}" + ' ', end='')
              imp = True
            else:
              if imp == True:
                print(wordlist[n] + ' ', end='')
                imp = False
              else:
                print(f"\033[0m{wordlist[n]}" + ' ', end='')
          
          print('\n\n>> ',end='')
       except IndexError:
          print('\n'*3)
          break



def main(choice):
  if choice == False:
    o = int(input("""Would you like to review Google's...:
    1) Terms of service
    2) Privacy policy
    or 
    3) Gov.uk terms and conditions
    """))
    if o == 1:
      wordlist = openfile('terms.txt')
    elif o == 2:
      wordlist = openfile('privacy.txt')
    elif o == 3:
      wordlist = openfile('gov.txt')
    else:
      print('Enter a valid number: \n')
      main(choice)

  else:
    print("""
    (Hit Enter, type '>', and hit Enter again once you've pasted.)
    (This will let the program know you're done with pasting)

    (Use right click to paste, not ctrl-v since this wont work on repl)
    Copy and paste the t's and c's here: 
    
    >>> """)
    i=0
    text = ''
    while i < 9999:
      line = input()
      if line == '>':
        i = 10011
      else:
        text = text + line
      i+=1
      print('\nLine number: ',i," (hit Enter, type '>' then hit Enter again when finished)")

  

    word = []
    l_wordlist = []
    for letter in text:
      if letter != ' ':
        if letter.isalnum() or letter == '.' or letter == '\'':
          word.append(letter)
      else:
        l_wordlist.append(word)
        word = []

    wordlist=[]
    for word in l_wordlist:
      x=''
      for letter in word:
        x = x +letter
      wordlist.append(x)
  
  print('\n')
  clause = input("""Here are the most important clauses in t's and c's:
  1) Payment details
  2) Location information
  3) Activity
  4) Malware and viruses 
  5) Disclaimers
  6) Personal data usage
  7) Artificial intelligence (AI)
  8) Harassment, bullying, stalking
  9) Deleting or removing your data
  0) < < Check all clauses > >
  
  Enter 0 if nothing is appearing
  Enter the number(s) you want to check (e.g '2358' or just '7'):
  """)
  print('\n'*3)
  for num in clause:
    try:
      clauses = int(num)
    except:
      print('Try Again and enter numbers only: \n')
      menu()
    if clauses == 1:
      check(['payment', 'pay', 'money'],wordlist)
    if clauses == 2:
      check(['location', 'gps', 'map', 'tracking'],wordlist)
    if clauses == 3:
      check(['activity', 'time', 'app'],wordlist)
    if clauses == 4:
      check(['malware','virus','viruses','risky','download','downloads'],wordlist)
    if clauses == 5:
      check(['disclaimer','disclaimers'],wordlist)
    if clauses == 6:
      check(['cookies','personal','sensitive'],wordlist)
    if clauses == 7:
      check(['ai', 'artificial', 'automation'],wordlist)
    if clauses == 8:
      check(['bullying', 'harassment', 'hate', 'stalking', 'abuse'],wordlist)
    if clauses == 9:
      check(['delete', 'remove', 'clear', 'wipe'],wordlist)
    if clauses == 0:
      check(['payment', 'pay','location', 'gps', 'map', 'tracking','activity', 'time', 'app','malware','virus','viruses','risky','download','downloads','disclaimer','disclaimers','cookies','personal','sensitive','ai', 'artificial', 'automation','bullying', 'harassment', 'hate', 'stalking', 'abuse','delete', 'remove', 'clear', 'wipe'],wordlist)


  print('>>> Complete \n\n')
  menu()



def advice():

  print('>> Advice: \nOpen link in web browser (use right-click to copy)\n\nhttps://InfoSlides.jimmyjamjar84.repl.co')
  time.sleep(5)
  print('\n'*3)
  menu()




menu()
