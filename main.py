###############          ##########        #######   #######        #########      #######       #
#              #        #          #             #         #       #         #           #
#               #       #          #            #         #        #         #          #        #
#              #        #          #           #         #         #         #         #         #
###############         ############          #         #          ###########        #          #
#              #        #          #         #         #           #         #       #           #
#               #       #          #        #         #            #         #      #            #
#              #        #          #       #         #             #         #     #             #
###############         #          #      #######    #######       #         #    #######        #

# Developer: Mohammad Ali Bazzazi (me)

########################### START ###########################
import pyttsx3

def speech(word):
    engine = pyttsx3.init()
    engine.setProperty('rate' , 120)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(word)
    engine.runAndWait()

word = input('Enter a Phrase: ')
speech(word)

########################### END ###########################
