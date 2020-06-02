from termcolor import cprint
import time
from os import system, name
from pygame import mixer

mixer.init()
mixer.music.load('bday.mp3')
mixer.music.play()

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


happy = '''
 HHHHHHH   HHHHHHH       AAAAA       PPPPPPPPPPPPPP   PPPPPPPPPPPPPP   YYYYY       YYYYY
  HHHHH     HHHHH       AA   AA      PPPP        PPPP PPPP        PPPP  YYYYY     YYYYY 
  HHHHH     HHHHH      AAA   AAA     PPPPP      PPPPP PPPPP      PPPPP   YYYYY  YYYYY
  HHHHHHHHHHHHHHH     AAAAAAAAAAA    PPPPPPPPPPPPPP   PPPPPPPPPPPPPP       YYYYYYY
  HHHHH     HHHHH    AAAA     AAAA   PPPPP            PPPPP                 YYYYY
  HHHHH     HHHHH   AAAAA     AAAAA  PPPPP            PPPPP                 YYYYY
 HHHHHHH   HHHHHHH AAAAA       AAAAA PPPPPPP          PPPPPPP              YYYYYYY
'''
birthday = '''                      
 BBBBBBBBBBBBBB    IIIIIIIIIIIIIIIII RRRRRRRRRRRRRR   TTTTTTTTTTTTTTTTT HHHHHHH   HHHHHHH DDDDDDDDDDDDD           AAAAA     YYYYY       YYYYY
 BBBBB     BBBBBB    IIIIIIIIIIIII   RRRR        RRRR   TTTTTTTTTTTTT    HHHHH     HHHHH  DDDDD     DDDDD        AA   AA     YYYYY     YYYYY  
 BBBBB     BBBBBBB       IIIII       RRRRR      RRRRR       TTTTT        HHHHH     HHHHH  DDDDD      DDDDD      AAA   AAA      YYYYY  YYYYY
 BBBBBBBBBBBBBBB         IIIII       RRRRRRRRRRRRRR         TTTTT        HHHHHHHHHHHHHHH  DDDDD       DDDDD    AAAAAAAAAAA       YYYYYYY
 BBBBB     BBBBBBB       IIIII       RRRRR    RRRRRR        TTTTT        HHHHH     HHHHH  DDDDD      DDDDD    AAAA     AAAA       YYYYY
 BBBBB     BBBBBB    IIIIIIIIIIIII   RRRRR      RRRRR       TTTTT        HHHHH     HHHHH  DDDDD     DDDDD    AAAAA     AAAAA      YYYYY
 BBBBBBBBBBBBBB    IIIIIIIIIIIIIIIII RRRRR      RRRRR       TTTTT       HHHHHHH   HHHHHHH DDDDDDDDDDDDD     AAAAA       AAAAA    YYYYYYY
'''
harini = '''
HHHHHHH   HHHHHHH       AAAAA       RRRRRRRRRRRRRR   IIIIIIIIIIIIIIIII  NNNNN     NNNNNNN IIIIIIIIIIIIIIIII
 HHHHH     HHHHH       AA   AA      RRRR        RRRR   IIIIIIIIIIIII    NNNNNN     NNNNN    IIIIIIIIIIIII  
 HHHHH     HHHHH      AAA   AAA     RRRR        RRRR       IIIII        NNNN NNN   NNNNN        IIIII      
 HHHHHHHHHHHHHHH     AAAAAAAAAAA    RRRRRRRRRRRRRR         IIIII        NNNNN NNN  NNNNN        IIIII      
 HHHHH     HHHHH    AAAA     AAAA   RRRRR    RRRRRR        IIIII        NNNNN  NNN NNNNN        IIIII      
 HHHHH     HHHHH   AAAAA     AAAAA  RRRRR      RRRRR   IIIIIIIIIIIII    NNNNN    NNNNNNN    IIIIIIIIIIIII  
HHHHHHH   HHHHHHH AAAAA       AAAAA RRRRR      RRRRR IIIIIIIIIIIIIIIII NNNNNNN     NNNNN  IIIIIIIIIIIIIIIII

'''
clear()
time.sleep(5)
cprint(happy, "cyan", attrs=['blink'])
time.sleep(5)
clear()
cprint(birthday, 'yellow', attrs=['blink'])
time.sleep(5)
clear()
cprint(harini, 'green', attrs=['blink'])
time.sleep(5)
clear()
time.sleep(5)
cprint(happy, "yellow", attrs=['blink'])
cprint(birthday, 'cyan', attrs=['blink'])
cprint(harini, 'green', attrs=['blink'])
time.sleep(5)
cake1 = r'''
          *                         *                                                  
    ~              *         ~              ~        ~
*         ~             *             *
  ~        )                   )   (        ~
          (_)    (        )   (_) (_)    *
    *     .#`` `(_) `( ` (_) ` # ` #_           *     *
       ,`  #     #  (_)   #    #   # \  ~ 
~     :    #     #   #    #    #   #  :      *     ~
      :.         #   #    #    #     .: 
   *  | `.____       #         ____"" |         ~    *
~     |       ````" "  " "```         |   * 
      |        HAPPY BIRTHDAY         |       *    ~  
 *    |                               |
    - |           HARINI              |-   *      ~
   /   \                             /   \     *
~  `.     ''''' "  "  " "  " " '''' '   .'            *
     \                                 /       ~
        "   "  "   "  " "   "   "   "     
          

'''
cake2 = r'''
          ~                         ~                                                  
    ~              ~         *              ~        *
~         *             *             *
  *        (                   (   )        *
          (_)    )        (   (_) (_)    ~
    ~     .#`` `(_) `) ` (_) ` # ` #_           ~     ~
       ,`  #     #  (_)   #    #   # \  ~ 
*     :    #     #   #    #    #   #  :      ~     *
      :.         #   #    #    #     .:                 ~
   ~  | `.____       #         ____"" |         *      
*     |       ````" "  " "```         |   ~
      |        HAPPY BIRTHDAY         |       ~       *  
 ~    |                               |
    - |           HARINI              |-   *      *
   /   \                             /   \     ~
*  `.     ''''' "  "  " "  " " '''' '   .'            ~
     \                                 /       *
        "   "  "   "  " "   "   "   "     
          

'''
for i in range(0,270):
    cprint(cake1,'white',attrs=['bold'])
    time.sleep(0.1)
    clear()
    cprint(cake2,'white',attrs=['bold'])
    time.sleep(0.1)
    clear()
mixer.music.stop()
