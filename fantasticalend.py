#modules import here

import random
import time


#character stats are defined here
#homeless guy
homelessHealth = 8
#homelessAC = 12


#PTSD teen
ptsdHealth = 12
#ptsdAC = 14
ptsdAttack = random.randrange(2, 4, 1)

#DID Office
didHealth = 10
#didAC = 16
didAttack = random.randrange(1, 5, 1)

#Monster stat blocks!!

#Voice
voiceHealth = 5
#voiceAC = 8


#Unreality
unrealityHealth = 8
unrealityAttack = random.randrange(2, 4, 1)

#Depression
depressionHealth = 10
depressionAttack = random.randrange(2, 4, 1)

#Aggression
aggressionHealth = 12
aggressionAttack = random.randrange(2, 5, 1)

#Paranoia
paranoiaHealth = 10
paranoiaAttack = random.randrange(3, 5, 1)

#Guilt
guiltHealth = 6
guiltAttack = random.randrange(2, 4, 1)

#Hallucination
hallucinationHealth = 7
hallucinationAttack = random.randrange(1, 4, 1)

#Flashback
flashbackHealth = 8
flashbackAttack = random.randrange(1, 4, 1)

#Loneliness
lonelinessHealth = 5
lonelinessAttack = random.randrange(1, 3, 1)

#Anxiety
anxietyHealth = 6
anxietyAttack = random.randrange(2, 4, 1)

#Mood Swing
moodSwingHealth = 9
moodSwingAttack = random.randrange(0, 5, 1)


#Time Loss
depressionHealth = 8
depressionAttack = random.randrange(1, 5, 1)

#title thing
print("""

,--.         .           .             .   ,--.       .
|            |           |   o         |   |          |
|-   ,-: ;-. |-  ,-: ,-. |-  . ,-. ,-: |   |-   ;-. ,-|
|    | | | | |   | | `-. |   | |   | | |   |    | | | |
'    `-` ' ' `-' `-` `-' `-' ' `-' `-` '   `--' ' ' `-'

""")




startGame = 1



while startGame == 1:
	#paths
	pathChoice = ""
	pathChoice = input("Choose 1, 2, or 3			")
	#1 is homeless, 2 is teen, 3 is DID Office
	if pathChoice == "1":
		startGame = 2
		print("""\n\nIt’s the crack of dawn, you are beside the river bank idly picking at the bugs on your skin.
Meanwhile, you are staring meaninglessly at the scrap of blankets and trash you call a home.
Suddenly, you hear a familiar voice, it’s the voice of one of your old high school teachers.
He is yelling at you to jump in the river, to help get the bugs off your skin.
He murmurs under his breath for you to stay in the river.\n\n""")
#choice1ForHomelessspaaaaal
		playerChoice = input("Refuse to listen (1) or do as he says (2).			")
		if playerChoice == "1":
			print("""

          ((((c,               ,7))))
        (((((((              ))))))))
         (((((((            ))))))))
          ((((((@@@@@@@@@@@))))))))
           @@@@@@@@@@@@@@@@)))))))
        @@@@@@@@@@@@@@@@@@))))))@@@@
       @@/,:::,\/,:::,\@@@@@@@@@@@@@@
       @@|:::::||:::::|@@@@@@@@@@@@@@@
       @@\\':::'/\\':::'/@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@
          @@@@@@@@@@@@@@@@@@@@@@
             /    \        (   \\
             (    )        \   \\              \


""")
			print("Your Health:"+" █"*int(homelessHealth))
			print("""
Monster Health:"""+" █"*int(voiceHealth))

			while (voiceHealth > 0) and (homelessHealth > 0):

				time.sleep(2)
				voiceAttack = random.randrange(0, 2, 1)
				print("\nThe monster attacks for", voiceAttack, "damage!")
				homelessHealth=homelessHealth-voiceAttack
				print("\nYour Health:"+" █"*int(homelessHealth))
				if homelessHealth < 1:
					break
				time.sleep(2)
				homelessAttack = random.randrange(2, 4, 1)
				print("\nYou attack the monster for",homelessAttack,"damage!")
				voiceHealth=voiceHealth-homelessAttack
				print("\nMonster Health:"+" █"*int(voiceHealth))
			if homelessHealth < 1:
				time.sleep(1)
				print("\nYou have lost the fight.")
				break
			elif voiceHealth < 1:
				print("\nYou have defeated the voice!")
				time.sleep(1)

		elif playerChoice == "2":
			deathSave = random.randrange(1,21,1)
			if deathSave < 11:
				#you jumped in the water and died
				print("""


				_____  _____
                                <     `/     |
                                 >          (
                                |   _     _  |
                                |  |_) | |_) |
                                |  | \ | |   |
                                |            |
                 ______.______%_|            |__________  _____
               _/                                       \|     |
              |                                                <
              |_____.-._________              ____/|___________|
                                |            |
                                |            |
                                |            |
                                |            |
                                |   _        <
                                |__/         |
                                 / `--.      |
                               %|            |%
                           |/.%%|          -< @%%%
                           `\%`@|     v      |@@%@%%
                         .%%%@@@|%    |    % @@@%%@%%%%
                    _.%%%%%%@@@@@@%%_/%\_%@@%%@@@@@@@%%%%%%

				""")
				break



			elif deathSave > 10:
				#you jumped in the water and survived
				#break
				print("\nYou dragged yourself out of the river.")
				time.sleep(2)


		print("\nThe line between reality and imagination has become a blur. You don’t know where you are. Are those even your hands? Maybe not. \n \n ")
		time.sleep(6)
		print("""
	                                                     __,
	                                        __...---`````_,
	            .-``-.     .-``-......__.-``   _.--``````  ___,
	           ^      :   :               -`````---````````_,
	           ^_      :  :....._                    _.-```
	            |`|-.   `.    o  ``-.__.-`````...````
	                 `.   `...__. ,'.___.-```;:'
	                   `._     ; ;        .:'___,
	                      ````` ;        _...--`
	                   __..--```       -```-.
	          .|,|_.-``___....---```````--.._\
	          `-,,--```     ..---```````--.
	                         `-.          ;).
	                            ;        ;'..)
	  __.-`|`-./                ;       ;).        \.-`/8e.__
	 __.   |   .                '      ;'..)       .  (88 8.__
	 __:  /|\  :_           __ ;      ;_          _: 8  )88:__
	    `/_|_\'/ '-._      / /;      ;) \     _.-' \`._/8*'
	           '.    ``-._/  |;     ;/   \_.-``   ,'
	             `-.          \;    ;\         ,-'
	                `-._     /  ;   ; \     ,-'
	                    `.__/    ;  ;  \__,'
	                              ; ;)`.
	                               ;;'..)
	                                ;

	""")
		print("\nYour Health:"+" █"*int(homelessHealth))
		print("""
Monster Health:"""+" █"*int(unrealityHealth))

		while (unrealityHealth>0) and (homelessHealth>0):

			time.sleep(2)
			unrealityAttack = random.randrange(0, 2, 1)
			print("\nThe monster attacks for", unrealityAttack, "damage!")
			homelessHealth=homelessHealth-unrealityAttack
			print("\nYour Health:"+" █"*int(homelessHealth))
			if homelessHealth < 1:
				break
			time.sleep(2)
			homelessAttack = random.randrange(2, 4, 1)
			print("\nYou attack the monster for",homelessAttack,"damage!")
			unrealityHealth=unrealityHealth-homelessAttack
			print("\nMonster Health:"+" █"*int(unrealityHealth))

		if homelessHealth < 1:
			time.sleep(1)
			print("\nYou have lost the fight.")
			break
		elif unrealityHealth < 1:
			print("\nYou have defeated the unreality!")
			time.sleep(1)

		homelessChoice = input("""
You feel a touch on your shoulder.

Quickly lash out against whatever is behind you (1) or try to calmly turn around and look (2).			""")

		if homelessChoice == "1":
			print("""            *                       *
	        *                 *
	       )       (\___/)     (
	    * /(       \ (. .)     )\ *
	      # )      c\   >'    ( #
	       '         )-_/      '
	     \\|,    ____| |__    ,|//
	       \ )  (  `  ~   )  ( /
	        #\ / /| . ' .) \ /#
	        | \ / )   , / \ / |
	         \,/ ;;,,;,;   \,/
	          _,#;,;;,;,
	         /,i;;;,,;#,;
	        //  %;;,;,;;,;
	       ((    ;#;,;%;;,,
	      _//     ;,;; ,#;,
	     /_)      #,;    ))
	             //      \|_
	             \|_      |#\
	               -"

		""")
			print("\nYour Health:"+" █"*int(homelessHealth))
			print("""
Monster Health:"""+" █"*int(aggressionHealth))

			while (aggressionHealth>0) and (homelessHealth>0):

				time.sleep(2)
				aggressionAttack = random.randrange(0, 2, 1)
				print("\nThe monster attacks for", aggressionAttack, "damage!")
				homelessHealth=homelessHealth-aggressionAttack
				print("\nYour Health:"+" █"*int(homelessHealth))
				if homelessHealth < 1:
					break
				time.sleep(2)
				homelessAttack = random.randrange(2, 4, 1)
				print("\nYou attack the monster for",homelessAttack,"damage!")
				aggressionHealth=aggressionHealth-homelessAttack
				print("\nMonster Health:"+" █"*int(aggressionHealth))
			if homelessHealth < 1:
				time.sleep(1)
				print("\nYou have lost the fight.")
				break
			elif aggressionHealth < 1:
				print("\nYou have defeated the aggression!")
				time.sleep(1)
			#fight aggression



		elif homelessChoice == "2":
			print("""




	                                                    `-.
	                                                      .`
	                                                   _.`.`
	                                               _.-` .`
	                                       ___.---` _.-`
	                               __..---`___..---`
	                      _...--.-`   _.--`
	                  _.-`.-`.-`  _.-`
	               .-` .`  .`   .`
	    .         /   /   /    /                    .
	    \`-.._    |  |    \    `.              _..-`/
	   .'-.._ ``--.._\     `. -- `.      _..-``  _..-`.
	   `_    _       `-. .`        `. .-`      _    _`
	     `.``           .            \          ``.`
	      `-.-'    _   .              :   _   `-.-`
	        `..-..'    ;       .` `.  '    `..-..`
	            /      .      : .-. : :        \

	               `-._.'`.    .`-'.' `._.-'
	                       `-....-`


		""")
			print("\nYour Health:"+" █"*int(homelessHealth))
			print("""
Monster Health:"""+" █"*int(paranoiaHealth))

			while (paranoiaHealth>0) and (homelessHealth>0):

				time.sleep(2)
				paranoiaAttack = random.randrange(0, 2, 1)
				print("\nThe monster attacks for", paranoiaAttack, "damage!")
				homelessHealth=homelessHealth-paranoiaAttack
				print("\nYour Health:"+" █"*int(homelessHealth))
				if homelessHealth < 1:
					break
				time.sleep(2)
				homelessAttack = random.randrange(2, 4, 1)
				print("\nYou attack the monster for",homelessAttack,"damage!")
				paranoiaHealth=paranoiaHealth-homelessAttack
				print("\nMonster Health:"+" █"*int(paranoiaHealth))
			#fight paranoia
			if homelessHealth < 1:
				time.sleep(1)
				print("\nYou have lost the fight.")
				break
			elif paranoiaHealth < 1:
				print("\nYou have defeated the paranoia!")
				time.sleep(1)

		print("\nThe touch on your shoulder turns out to be a social worker. You leave with them, and they take you to a shelter where you are able to get help.")
		time.sleep(6)
		print("""




						.---.
					       |---|
					       |---|
					       |---|
					   .---^ - ^---.
					   :_______:
					       |  |//|
					       |  |//|
					       |  |//|
					       |  |//|
					       |  |//|
					       |  |//|
					       |  |.-|
					       |.-'**|
					        \***/
					         \*/
					          V


	""")
		print("\nYour Health:"+" █"*int(homelessHealth))
		print("""
Monster Health:"""+" █"*int(guiltHealth))

		while (guiltHealth>0) and (homelessHealth>0):

			time.sleep(2)
			guiltAttack = random.randrange(0, 2, 1)
			print("\nThe monster attacks for", guiltAttack, "damage!")
			homelessHealth=homelessHealth-guiltAttack
			print("\nYour Health:"+" █"*int(homelessHealth))
			if homelessHealth < 1:
				break
			time.sleep(2)
			homelessAttack = random.randrange(2, 4, 1)
			print("\nYou attack the monster for",homelessAttack,"damage!")
			guiltHealth=guiltHealth-homelessAttack
			print("\nMonster Health:"+" █"*int(guiltHealth))
			#guilt fight
		if homelessHealth < 1:
			time.sleep(1)
			print("\nYou don’t deserve the help you're getting. You decide to leave the shelter as soon as you can.")
			time.sleep(2)
			break
		elif guiltHealth < 1:
			print("\nYou have defeated the guilt!")
			time.sleep(1)
			print("\nYou stay at the shelter as the months go by you get real help and are slowly able to get back on your feet.")
			time.sleep(2)
			break












#path2
	elif pathChoice == "2":
		startGame = 2
		print("""\n\nYou’re walking through the halls of your high school, crowded by your classmates.
Your classmates are chitchatting within their group of friends.
You see a group of girls in your peripheral vision and when you turn to look
directly at them they are gone, along with the rest of your classmates, Leaving you completely and utterly alone.\n\n""")

		playerChoice = input("Run out of the school as quickly as you can (1), or scream at the top of your lungs (2).			")
		if playerChoice == "1":
			print("\nYou bolt away from the empty building, heart racing.")
			time.sleep(2)

		elif playerChoice == "2":
			print("\nYou scream curses at the empty halls, voice straining.")
			time.sleep(2)



		print("""



             ,,,,,,,,
           ,|||````||||
     ,,,,|||||       ||,
  ,||||```````       `||
,|||`                 |||,
||`     ....,          `|||
||     ::::::::          |||,
||     :::::::'     ||    ``|||,
||,     :::::'               `|||
`||,                           |||
 `|||,       ||          ||    ,||
   `||                        |||`
    ||                   ,,,||||
    ||              ,||||||```
   ,||         ,,|||||`
  ,||`   ||   |||`
 |||`         ||
,||           ||
||`           ||
|||,         |||
 `|||,,    ,|||
   ``||||||||`
	""")
		print("\nYour Health:"+" █"*int(ptsdHealth))
		print("""
Monster Health:"""+" █"*int(hallucinationHealth))

		while (hallucinationHealth>0) and (ptsdHealth>0):

			time.sleep(2)
			hallucinationAttack = random.randrange(1, 3, 1)
			print("\nThe monster attacks for", hallucinationAttack, "damage!")
			ptsdHealth=ptsdHealth-hallucinationAttack
			print("\nYour Health:"+" █"*int(ptsdHealth))
			if ptsdHealth < 1:
				break
			time.sleep(2)
			ptsdAttack = random.randrange(2, 4, 1)
			print("\nYou attack the monster for",ptsdAttack,"damage!")
			hallucinationHealth=hallucinationHealth-ptsdAttack
			print("\nMonster Health:"+" █"*int(hallucinationHealth))
		#fight hallucination
		if ptsdHealth < 1:
			time.sleep(1)
			print("\nYou have lost the fight.")
			break
		elif hallucinationHealth < 1:
			print("\nYou have defeated the hallucination!")
			time.sleep(1)

		print("\nEverything outside of the school is barren, dead grass only broken up by a single road in front of the school.\nYou see a figure sitting on the curb, staring into the pale sky.")
		figureChoice = input("\nApproach the figure(1), or ignore it.(2)			")

		if figureChoice == "1":
			print("\nIt's you! They turn to face you, looking up with a gaunt face and distant eyes.\nThey seem to look through you, lost in their own thoughts.")
			figure2Choice = input("\nAttempt to comfort the figure,(1) or flee in terror from them (2).			")
			if figure2Choice == "1":
				print("\nYou feel an overwhleming sense of abandonment wash over you.")
				time.sleep(2)

				print("""



                     .          ..
                      . .       .. .
                      . ..     ... .
                       . ..    .. .
                       .  ......  .
                        . ...... .
                         ........
                         ........
                         .... 0..
                        .........
                       ........ .
       .              @...)  ....
       ..                    ....
       ...                .......
        ........................
         .......................
         .......................
        ........................
       ........      .....  .....
      .......      .....    .....
     ...  ...     ....       ....
    ...    ...   ...           ...
   ...       ......             ...
   ...        .:..                ...
   ...        ...:..                ...
    ...      ...   ..                 ..
      ..    ..



			""")
				print("\nYour Health:"+" █"*int(ptsdHealth))
				print("""
Monster Health:"""+" █"*int(lonelinessHealth))

				while (lonelinessHealth>0) and (ptsdHealth>0):

					time.sleep(2)
					lonelinessAttack = random.randrange(1, 3, 1)
					print("\nThe monster attacks for", lonelinessAttack, "damage!")
					ptsdHealth=ptsdHealth-lonelinessAttack
					print("\nYour Health:"+" █"*int(ptsdHealth))
					if ptsdHealth < 1:
						break
					time.sleep(2)
					ptsdAttack = random.randrange(2, 4, 1)
					print("\nYou attack the monster for",ptsdAttack,"damage!")
					lonelinessHealth=lonelinessHealth-ptsdAttack
					print("\nMonster Health:"+" █"*int(lonelinessHealth))
				#fight loneliness
				if ptsdHealth < 1:
					time.sleep(1)
					print("\nYou have lost the fight.")
					break
				elif lonelinessHealth < 1:
					print("\nYou have defeated the loneliness!")
					time.sleep(1)


		if figureChoice or figure2Choice == "2":
			print("\n\nYou're in your bedroom closet, but are trapped. The small space contains a handful of old toys you know your mother had thrown away when you were small.\nThe voice of your mother comes from down the hall, spitting curses at whatever has upset her now.")

			time.sleep(2)

			print("""


         .__---~~~(~~-_.
     _-'  ) -~~- ) _-" )_
    (  ( `-,_..`.,_--_ '_,)_
   (  -_)  ( -_-~  -_ `,    )
   (_ -_ _-~-__-~`, ,' )__-'))--___--~~~--__--~~--___--__..
   _ ~`_-'( (____;--==,,_))))--___--~~~--__--~~--__----~~~'`=__-~+_-_.
  (@) (@) `````      `-_(())_-~  mn



		""")
			print("\nYour Health:"+" █"*int(ptsdHealth))
			print("""
Monster Health:"""+" █"*int(flashbackHealth))

			while (flashbackHealth>0) and (ptsdHealth>0):

				time.sleep(2)
				flashbackAttack = random.randrange(1, 3, 1)
				print("\nThe monster attacks for", flashbackAttack, "damage!")
				ptsdHealth=ptsdHealth-flashbackAttack
				print("\nYour Health:"+" █"*int(ptsdHealth))
				if ptsdHealth < 1:
					break
				time.sleep(2)
				ptsdAttack = random.randrange(2, 4, 1)
				print("\nYou attack the monster for",ptsdAttack,"damage!")
				flashbackHealth=flashbackHealth-ptsdAttack
				print("\nMonster Health:"+" █"*int(flashbackHealth))
			#fight flashback
			if ptsdHealth < 1:
				time.sleep(1)
				print("\nYou have lost the fight.")
				break
			elif flashbackHealth < 1:
				print("\nYou have defeated the flashback!")
				time.sleep(1)

			print("\n\nYou wake up with a tight pain in your chest in your actual bedroom, glancing around. It was all a dream, right?")
			time.sleep(6)


			print("""


            (         .-,
            / )      .' (       ___
           //(.-""''-/ /\ )   .-"   "-.
           |.'     _`.\// .-'         `..--.
       ..--/-.   .'_` `'-'      ___    ( C  )\

     /    \_/|   \__/   |    (
    |     _\-' _   __  /      `.
    \ ,--7  `.(_)_.| .'         `.
     | C._)   `.___/' .---._      \           __
     \    |       `. /      `-.    \        ,'  `.
      `--'          Y          \    |       )     `-._.--.__
                    |     \         |    _.'  .--.___.-'`--.\

               _    \      |       /  `v    |
          .'`-' `--._)     /::___.'     \   /
         /    .---.       /   `-.        \ |
      _.' _.-' `._ `-.   /       `.       /
     /.--'        `-. `. \         `-.__.'
                     `.'_/



		""")
			print("\nYour Health:"+" █"*int(ptsdHealth))
			print("""Monster Health:"""+" █"*int(anxietyHealth))

			while (anxietyHealth>0) and (ptsdHealth>0):

				time.sleep(2)
				anxietyAttack = random.randrange(1, 3, 1)
				print("\nThe monster attacks for", anxietyAttack, "damage!")
				ptsdHealth=ptsdHealth-anxietyAttack
				print("\nYour Health:"+" █"*int(ptsdHealth))
				if ptsdHealth < 1:
					break
				time.sleep(2)
				ptsdAttack = random.randrange(2, 4, 1)
				print("\nYou attack the monster for",ptsdAttack,"damage!")
				anxietyHealth=anxietyHealth-ptsdAttack
				print("\nMonster Health:"+" █"*int(anxietyHealth))
			#fight anxiety
			if ptsdHealth < 1:
				time.sleep(1)
				print("\nYou have lost the fight.")
				break
			elif anxietyHealth < 1:
				print("\nYou have defeated the anxiety! After a few restless hours, you manage to fall back asleep.")
				time.sleep(1)





#path3
	elif pathChoice == "3":
		startGame = 2
		print("""\n\nIt's midday, and you try to shake the fog out of your thoughts, and concentrate on the spreadsheet that’s been open on your computer\nfor the past hour, a single change still not made.\n\n""")
		playerChoice = input("\nTry to focus on your work (1) or take a break and try again in a bit (2).			")
		if playerChoice == "1":
			print("\nYou focus in on the screen, only to see the text and images on the screen distort before your eyes.")
			time.sleep(4)
		elif playerChoice == "2":
			print("\nYou decide to take a break and try to get back to work later only to be interrupted by the room spinning.")
			time.sleep(4)
		print("""
	                                                     __,
	                                        __...---`````_,
	            .-``-.     .-``-......__.-``   _.--``````  ___,
	           ^      :   :               -`````---````````_,
	           ^_      :  :....._                    _.-```
	            |`|-.   `.    o  ``-.__.-`````...````
	                 `.   `...__. ,'.___.-```;:'
	                   `._     ; ;        .:'___,
	                      ````` ;        _...--`
	                   __..--```       -```-.
	          .|,|_.-``___....---```````--.._\
	          `-,,--```     ..---```````--.
	                         `-.          ;).
	                            ;        ;'..)
	  __.-`|`-./                ;       ;).        \.-`/8e.__
	 __.   |   .                '      ;'..)       .  (88 8.__
	 __:  /|\  :_           __ ;      ;_          _: 8  )88:__
	    `/_|_\'/ '-._      / /;      ;) \     _.-' \`._/8*'
	           '.    ``-._/  |;     ;/   \_.-``   ,'
	             `-.          \;    ;\         ,-'
	                `-._     /  ;   ; \     ,-'
	                    `.__/    ;  ;  \__,'
	                              ; ;)`.
	                               ;;'..)
	                                ;

		""")
		print("\nYour Health:"+" █"*int(didHealth))
		print("""
Monster Health:"""+" █"*int(unrealityHealth))

		while (unrealityHealth>0) and (didHealth>0):

			time.sleep(2)
			unrealityAttack = random.randrange(0, 2, 1)
			print("\nThe monster attacks for", unrealityAttack, "damage!")
			didHealth=didHealth-unrealityAttack
			print("\nYour Health:"+" █"*int(didHealth))
			if didHealth < 1:
				break
			time.sleep(2)
			didAttack = random.randrange(2, 4, 1)
			print("\nYou attack the monster for",didAttack,"damage!")
			unrealityHealth=unrealityHealth-didAttack
			print("\nMonster Health:"+" █"*int(unrealityHealth))

		if didHealth < 1:
			time.sleep(1)
			print("\nYou have lost the fight.")
			break
		elif unrealityHealth < 1:
			print("\nYou have defeated the unreality!")
			time.sleep(1)

		print("\nYour project manager comes over and asks why you've been scribbling nonsense in your notebook for the past half hour instead of working on the spreadsheet.")
		playerChoice = input("\nTell her that they're not scribbles to you (1), or ignore her questions (2).			")
		if playerChoice == "1":
			print("""
	                /   \\
	                | /| \\
	                | ||_/
	                | ||
	          /\\    | ||
	        /   |   | ||
	      /  |\\ |   | ||
	     |__/|| |   | ||
	         || |   | ||
	         || |   | ||
	        /    ~~~    \\
	       |   ^     ^   |
	       |  (o)   (o)  |
	       \      !      /
	       >\     ^     /<
	         \_________/
	           (\   /)
	           ( >o< )
	           (/   \)

			""")
			print("\nYour Health:"+" █"*int(didHealth))
			print("""
Monster Health:"""+" █"*int(moodSwingHealth))

			while (moodSwingHealth>0) and (didHealth>0):

				time.sleep(2)
				moodSwingAttack = random.randrange(0, 2, 1)
				print("\nThe monster attacks for", moodSwingAttack, "damage!")
				didHealth=didHealth-moodSwingAttack
				print("\nYour Health:"+" █"*int(didHealth))
				if didHealth < 1:
					break
				time.sleep(2)
				didAttack = random.randrange(2, 4, 1)
				print("\nYou attack the monster for",didAttack,"damage!")
				moodSwingHealth=moodSwingHealth-didAttack
				print("\nMonster Health:"+" █"*int(moodSwingHealth))

			if didHealth < 1:
				time.sleep(1)
				print("\nYou have lost the fight.")
				break
			elif moodSwingHealth < 1:
				print("\nYou have defeated the mood swing!")
				time.sleep(1)

			print("\nYou lash out and react in a rather aggressive manner till she storms off to your boss")
			time.sleep(5)
			print("""
	         .-'`'-.
	  ,-'`'.   '._     \     ______
	 /    .'  ___ `-._  |    \ .-'`
	|   .' ,-' __ `'/.`.'  ___\\
	______  \ .' \',-' 12 '-.  '.  `-._ \
	'`-. /   ` / / 11    7 1 `.  `.    '.\
	/ _.-'  | |      O      3|  |  ______
	/.'      | |9      \      '  '  '`-. /
	______ '  \ 8     \   4/  /      //___
	\ .-'`  '. `'.7  6  5.'  '      / _.-'
	___\\       `. _ `'''` _.'\\-.   /.'
	`-._ \       .//`''--''   (   )
	'.\     (   )          '-`
	      `-'
			""")
			print("\nYour Health:"+" █"*int(didHealth))
			print("""
	Monster Health:"""+" █"*int(depressionHealth))

			while (depressionHealth>0) and (didHealth>0):

				time.sleep(2)
				depressionAttack = random.randrange(1, 3, 1)
				print("\nThe monster attacks for", depressionAttack, "damage!")
				didHealth=didHealth-depressionAttack
				print("\nYour Health:"+" █"*int(didHealth))
				if didHealth < 1:
					break
				time.sleep(2)
				didAttack = random.randrange(2, 4, 1)
				print("\nYou attack the monster for",didAttack,"damage!")
				depressionHealth=depressionHealth-didAttack
				print("\nMonster Health:"+" █"*int(depressionHealth))

			if didHealth < 1:
				time.sleep(1)
				print("\nYou have lost the fight.")
				break
			elif depressionHealth < 1:
				print("\nYou have defeated the time loss!")
				time.sleep(1)

			print("You suddenly realize you’re back in your apartment. Staring at static. You don't know how long you've been there, you just know there's an empty bag of chips beside you.")

		elif playerChoice == "2":
			print("""
      ____  __.---""---.__  ____
      /####\/              \/####\

      \__OO/                \OO__/
    __/                          \__
 .-"    .                      .    "-.
 |  |   \.._                _../   |  |
  \  \    \."-.__________.-"./    /  /
    \  \    "--.________.--"    /  /
  ___\  \_                    _/  /___
./    )))))                  (((((    \.
\                                      /
 \           \_          _/           /
   \    \____/""-.____.-""\____/    /
     \    \                  /    /
      -.  .|               ./.
    ." / |  -              /  | -  ".
 ."  /   |   -           /   |   -   ".
/.-./.--.|.--.\          /.--.|.--.\.-.|
			""")
			print("\nYour Health:"+" █"*int(didHealth))
			print("""
Monster Health:"""+" █"*int(depressionHealth))

			while (depressionHealth>0) and (didHealth>0):

				time.sleep(2)
				depressionAttack = random.randrange(1, 3, 1)
				print("\nThe monster attacks for", depressionAttack, "damage!")
				didHealth=didHealth-depressionAttack
				print("\nYour Health:"+" █"*int(didHealth))
				if didHealth < 1:
					break
				time.sleep(2)
				didAttack = random.randrange(2, 4, 1)
				print("\nYou attack the monster for",didAttack,"damage!")
				depressionHealth=depressionHealth-didAttack
				print("\nMonster Health:"+" █"*int(depressionHealth))

			if didHealth < 1:
				time.sleep(1)
				print("\nYou have lost the fight.")
				break
			elif depressionHealth < 1:
				print("\nYou have defeated the time loss!")
				time.sleep(1)
			print("\nYou suddenly realize you’re back in your apartment.\nYou don't know how long you've been there, you just know there's an empty bag of chips beside you.")




#pathno
	else:
		print("Please choose a valid path; 1, 2, or 3.")
