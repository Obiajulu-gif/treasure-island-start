print('''


               ,,ggddY"""Ybbgg,,
          ,agd888b,_ "Y8, ___`""Ybga,
       ,gdP""88888888baa,.""8b    "888g,
     ,dP"     ]888888888P'  "Y     `888Yb,
   ,dP"      ,88888888P"  db,       "8P""Yb,
  ,8"       ,888888888b, d8888a           "8,
 ,8'        d88888888888,88P"' a,          `8,
,8'         88888888888888PP"  ""           `8,
d'          I88888888888P"                   `b
8           `8"88P""Y8P'                      8
8            Y 8[  _ "                        8
8              "Y8d8b  "Y a                   8
8                 `""8d,   __                 8
Y,                    `"8bd888b,             ,P
`8,                     ,d8888888baaa       ,8'
 `8,                    888888888888'      ,8'
  `8a                   "8888888888I      a8'
   `Yba                  `Y8888888P'    adP'
     "Yba                 `888888P'   adY"
       `"Yba,             d8888P" ,adP"'          -------
          `"Y8baa,      ,d888P,ad8P"'
               ``""YYba8888P""''

#######                                                                       
   #       #####     ######      ##       ####     #    #    #####     ###### 
   #       #    #    #          #  #     #         #    #    #    #    #      
   #       #    #    #####     #    #     ####     #    #    #    #    #####  
   #       #####     #         ######         #    #    #    #####     #      
   #       #   #     #         #    #    #    #    #    #    #   #     #      
   #       #    #    ######    #    #     ####      ####     #    #    ###### 
                                                                              
 #####        #       #     #    ####### 
#     #      # #      ##   ##    #       
#           #   #     # # # #    #       
#  ####    #     #    #  #  #    #####   
#     #    #######    #     #    #       
#     #    #     #    #     #    #       
 #####     #     #    #     #    #######
 
                                         
''')
#welcome statement to the users
print("Welcome To the Treaure island \n")
print("Your Mission is to find the Missing Treasure\n")
print('''
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|M)(MMMMoMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
88 vanishing point 888888888888888888888888888888888888888888888 fL 888
 

''')
#asking for the user direction
direction = input(
    "There is a Crooky Road in Front of You, Do You wish to Go Right or Left?\n"
)

#converting it to a Lowercase
directionLowercase = direction.lower()

if directionLowercase == "right":
    print("✖✖✖SORRY YOU FELL INTO A HOLE.✖✖✖\ ")
    print("✖✖✖GAME OVER✖✖✖")

elif directionLowercase == "left":
    print("⭐⭐KEEP IT UP⭐⭐\n")
    #asking if to swim or to wait
    swim_and_wait = input("Do you wish to Swim or Wait?\n")

    #converting it to a Lowercase
    swim_and_waitLowercase = swim_and_wait.lower()

    #condition for the Water Part
    if swim_and_waitLowercase == "swim":
        print('''
                 ,
             .';
         .-'` .'
       ,`.-'-.`\
      ; /     '-'
      | \       ,-,
      \  '-.__   )_`'._
       '.     ```      ``'--._
      .-' ,                   `'-.
       '-'`-._           ((   o   )
        >>>   `'--....(`- ,__..--'
                       '-'`    
                ''')
        print("✖✖✖ ATTACKED BY A TROUT✖✖✖")
        print("✖✖✖GAMEOVER✖✖✖")

    elif swim_and_waitLowercase == "wait":
        print("IT SEEM YOU MADE THE RIGHT CHOICE\n")
        print("⭐⭐KEEP IT UP DEAR⭐⭐\n")

        # asking for which door to choose
        print('''
 ______________
|\ ___________ /|
| |  _ _ _ _  | |
| | | | | | | | |
| | |-+-+-+-| | |
| | |-+-+-+-| | |
| | |_|_|_|_| | |
| |     ___   | |
| |    /__/   | |
| |   [%==] ()| |
| |         ||| |
| |         ()| |
| |           | |
| |           | |
| |           | |
|_|___________|_| 
        
        ''')
        door = input(
            "Which Colour of the Door do you wish to pass through?\n RED, BLUE OR YELLOW\n"
        )
        doorLowercase = door.lower()

        #condition for the Door Entrance
        if doorLowercase == "yellow":
            print('''

dP    dP     .88888.     dP     dP                   dP   dP   dP     .88888.     888888ba  
Y8.  .8P    d8'   `8b    88     88                   88   88   88    d8'   `8b    88    `8b 
 Y8aa8P     88     88    88     88                   88  .8P  .8P    88     88    88     88 
   88       88     88    88     88                   88  d8'  d8'    88     88    88     88 
   88       Y8.   .8P    Y8.   .8P                   88.d8P8.d8P     Y8.   .8P    88     88 
   dP        `8888P'     `Y88888P'                   8888' Y88'       `8888P'     dP     dP 
                                      
            ''')
        elif doorLowercase == "red":
            print('''
         _____
     .o8PP"""PYbo_
   o8P'    )    `Yb.
 .8P    ) ))(    _ooL
.8P    ( )) ) ),dP'`8L
dP    )) (  ,o8P'   Y8.
8b   ) ) ,o8P' ((   )8[
Y8  ( ,o8P'( )) )   d8
 8b_o8P'--`-'--'   ,8'
  `P`   Flames    o8'
   `Yb._      _.o8P
     `"PYbooo8PP'  

            ''')
            print("Oh No, it Seem You Got burn by a Fiercing Fire\n")
            print("✖✖✖GAMEOVER✖✖✖")
        elif doorLowercase == "blue":
            print('''
                                __,,,,_
          _ __..-;''`--/'/ /.',-`-.
      (`/' ` |  \ \ \\ / / / / .-'/`,_
     /'`\ \   |  \ | \| // // / -.,/_,'-,
    /<7' ;  \ \  | ; ||/ /| | \/    |`-/,/-.,_,/')
   /  _.-, `,-\,__|  _-| / \ \/|_/  |    '-/.;.\'
   `-`  f/ ;      / __/ \__ `/ |__/ |
        `-'      |  -| =|\_  \  |-' |
              __/   /_..-' `  ),'  //
          fL ((__.-'((___..-'' \__.'
            
            ''')
            print("Oh No, You Got Eaten by beast\n")
            print("✖✖✖GAMEOVER✖✖✖")
        else:
            print("⚡⚡YOU INPUT THE WRONG CHARACTER⚡⚡ \n")
            print("⚡⚡⚡⚡ TRY AGAIN ⚡⚡⚡⚡")

    else:
        print("⚡⚡YOU INPUT THE WRONG CHARACTER⚡⚡ \n")
        print("⚡⚡⚡⚡ TRY AGAIN ⚡⚡⚡⚡")

else:
    print("⚡⚡YOU INPUT THE WRONG CHARACTER⚡⚡ \n")
    print("⚡⚡⚡⚡ TRY AGAIN ⚡⚡⚡⚡")
