def game():
    answer = input('Press "s" to start the game: ')

    if answer.lower() == 's':
        print('The adventure begins')
        start = True

    if start:
        print('You wake up in a hospital room. There doesn\'t seem to be anyone around to tell you what\'s going on.')
        choice = input('Do you press the help button (button) by your bed or go out in the hall to look around (look): ')

        # button
        if choice.lower() == 'button': 
            print('You push the button but no one shows up.')
            choice = input('Do you go out into the hall (hall) or look around the room (room): ')

            # button-hall
            if choice.lower() == 'hall':
                print('You look into the hall. There is a lone person standing down the hall on the left aways in a hospital gown.')
                choice = input('Do you go ask the person what is happening (left) or turn right (right): ')

                # button-hall-left
                if choice.lower() == 'left':
                    print('You approach the person asking if they know what\'s going on. As you get closer, you see something isn\'t right. Once you reach the man, he turns around and you see his decomposing face. He tackles you to the ground and takes a chunk out of your shoulder.')
                    print('GAME OVER')

                # button-hall-right
                if choice.lower() == 'right':
                    print('You turn right and find the exit. Once outside it\'s clear something terrible has happened. Buildings have been looted. There\'s a horrible stench in the air. You see a police car still running nearby.')
                    choice = input('Do you get in the poice car(car) or walk down the street(walk): ')

                    # button-hall-right-car
                    if choice.lower() == 'car':
                        print('When you open the door you find another horrific site. It\'s obvious the cop was attacked by something. There are wounds on his arms and face. You notice his gun is still in his hand. You grab it and check to see there are still four rounds left.')
                        choice = input('You take the gun, given the state of things it might come in handy. As you walk down the street you hear a scream. Do you run towards the screams(help) or ignore them(continue): ')

                        # button-hall-right-car-help
                        if choice.lower() == 'help':
                            print('You run towards the screams. There is a woman being attack by another one of those things.')
                            choice = input('Do you use your gun to shoot the zombie(shoot) or save your bullets and try to use your hands(hands): ')

                            # button-hall-right-car-help-shoot
                            if choice.lower() == 'shoot':
                                print('You shoot the zombie in the head saving the woman. "Thank you", she says. "I thought I was going to die"')
                                print('The woman tells you about a group of people taking shelter at a nearby firehouse and offers you a place to stay there')
                                print('Congratulations! You have survied the into. Chapter 1 will becoming soon.')

                            # button-hall-right-car-help-hands
                            if choice.lower() == 'hands':
                                print('You grab the zombie and pull it away from the woman. It turns it\'s attention to you now, biting a chunk out of your arm.')
                                print('The woman runs away terrified. You manage to beat the zombie with a nearby rock but quickly pass out from blood loss. When you wake up your\'re consumed with the urge to eat. The rest of your days are spent wondering around mindlessly looking for flesh')
                                print('GAME OVER')

                        # button-hall-right-car-ignore
                        if choice.lower() == 'ignore':
                            print('You ignore the screams. You\'re not in any place to be offering help right now. You come across a mostly looted store but figured it can\'t hurt to look.')
                            print('As you\'re looking through the shelves a group of those monsters come in and block off your exit. You try to fight them off but theres too many of them.')
                            print('GAME OVER')

                    # button-hall-right-walk
                    if choice.lower() == 'walk':
                        choice = input('As you walk down the street you hear a scream. Do you run towards the screams(help) or ignore them(continue): ')

                        # button-hall-right-walk-help
                        if choice.lower() == 'help':
                            print('You run towards the screams. You see a woman being attacked by another one of those creatures. With no weapon in sight you grab the monster an pull it away from the woman. It turns it\'s attention to you now, biting a chunk out of your arm.')
                            print('The woman runs away terrified. You manage to beat the zombie with a nearby rock but quickly pass out from blood loss. When you wake up your\'re consumed with the urge to eat. The rest of your days are spent wondering around mindlessly looking for flesh')
                            print('GAME OVER')

                        # button-hall-right-walk-continue
                        if choice.lower() == 'continue':
                            print('You ignore the screams. You\'re not in any place to be offering help right now. You come across a mostly looted store but figured it can\'t hurt to look.')
                            print('As you\'re looking through the shelves a group of those monsters come in and block off your exit. You try to fight them off but theres too many of them.')
                            print('GAME OVER')

            # button-room
            if choice.lower() == 'room':
                print('You look around the room and notice a bedpan and a tray of needles.')
                print('A man with a decomposing face wearing a night gown walk in and tries to attack you')
                choice = input('Do you defend yourself with the needles(needle) or with the bedpan(bedpan): ')

                # button-room-needle
                if choice.lower() == 'needle':
                    print('You grab a needle and stab the man in the neck. The needle snaps and the man seems unfazed. He then takels you to the ground bitting into your neck.')
                    print('GAME OVER')

                # button-room-bedpan
                if choice.lower() == 'bedpan':
                    print('You grab the bedpan and smash the man in the head. He gets knocked back and falls to the ground. You take the opertunity to run out of the room and find the exit. ')
                    print('You think "What was that? Are zombies a real thing now?')
                    print('Once outside it\'s clear something terrible has happened. Buildings have been looted. There\'s a horrible stench in the air. You see a police car still running nearby.')
                    choice = input('Do you get in the poice car(car) or walk down the street(walk): ')

                    # button-room-bedpan-car
                    if choice.lower() == 'car':
                        print('When you open the door you find another horrific site. It\'s obvious the cop was attacked by something. There are wounds on his arms and face. You notice his gun is still in his hand. You grab it and check to see there are still four rounds left.')
                        choice = input('You take the gun, given the state of things it might come in handy. As you walk down the street you hear a scream. Do you run towards the screams(help) or ignore them(continue): ')

                        # button-room-bedpan-car-help
                        if choice.lower() == 'help':
                            print('You run towards the screams. There is a woman being attack by another one of those things.')
                            choice = input('Do you use your gun to shoot the zombie(shoot) or save your bullets and try to use your hands(hands): ')

                            # button-room-bedpan-car-help-hands
                            if choice.lower() == 'hands':
                                print('You grab the zombie and pull it away from the woman. It turns it\'s attention to you now, biting a chunk out of your arm.')
                                print('The woman runs away terrified. You manage to beat the zombie with a nearby rock but quickly pass out from blood loss. When you wake up your\'re consumed with the urge to eat. The rest of your days are spent wondering around mindlessly looking for flesh')
                                print('GAME OVER')

                            # button-room-bedpan-car-help-shoot
                            if choice.lower() == 'shoot':
                                print('You shoot the zombie in the head saving the woman. "Thank you", she says. "I thought I was going to die"')
                                print('The woman tells you about a group of people taking shelter at a nearby firehouse and offers you a place to stay there')
                                print('Congratulations! You have survied the into. Chapter 1 will becoming soon.')

                        # button-room-bedpan-car-ignore
                        if choice.lower() == 'ignore':
                            print('You ignore the screams. You\'re not in any place to be offering help right now. You come across a mostly looted store but figured it can\'t hurt to look.')
                            print('As you\'re looking through the shelves a group of those monsters come in and block off your exit. You try shooting them but theres too many.')
                            print('GAME OVER')

                    # button-room-bedpan-walk
                    if choice.lower() == 'walk':
                        choice = input('As you walk down the street you hear a scream. Do you run towards the screams(help) or ignore them(continue): ')

                        # button-room-bedpan-walk-help
                        if choice.lower() == 'help':
                            print('You run towards the screams. You see a woman being attacked by another one of those creatures. With no weapon in sight you grab the monster an pull it away from the woman. It turns it\'s attention to you now, biting a chunk out of your arm.')
                            print('The woman runs away terrified. You manage to beat the zombie with a nearby rock but quickly pass out from blood loss. When you wake up your\'re consumed with the urge to eat. The rest of your days are spent wondering around mindlessly looking for flesh')
                            print('GAME OVER')

                        # button-room-bedpan-walk-continue
                        if choice.lower() == 'continue':
                            print('You ignore the screams. You\'re not in any place to be offering help right now. You come across a mostly looted store but figured it can\'t hurt to look.')
                            print('As you\'re looking through the shelves a group of those monsters come in and block off your exit. You try to fight them off but theres too many of them.')
                            print('GAME OVER')

            # button-hall
            if choice.lower() == 'hall':
                print('You look into the hall. There is a lone person standing down the hall on the left aways in a hospital gown.')
                choice = input('Do you go ask the person what is happening (left) or turn right (right): ')
        # look
        if choice.lower() == 'look':
            print('You look into the hall. There is a lone person standing down the hall on the left aways in a hospital gown.')
            choice = input('Do you go ask the person what is happening (left) or turn right (right): ')

            # look-left
            if choice.lower() == 'left':
                print('You approach the person asking if they know what\'s going on. As you get closer, you see something isn\'t right. Once you reach the man, he turns around and you see his decomposing face. He tackles you to the ground and takes a chunk out of your shoulder.')
                print('GAME OVER')
            
            # look-right
            if choice.lower() == 'right':
                print('You turn right, avoiding the person at the end of the hall on the left. You find the exit and take a step outside. Once outside, it\'s clear something terrible has happened. Buildings have been looted. There\'s a horrible stench in the air. You see a police car still running nearby.')
                choice = input('Do you take the police car (car) or walk down the street (walk): ')

                # look-right-car
                if choice.lower() == 'car':
                        print('When you open the door you find another horrific site. It\'s obvious the cop was attacked by something. There are wounds on his arms and face. You notice his gun is still in his hand. You grab it and check to see there are still four rounds left.')
                        choice = input('You take the gun, given the state of things it might come in handy. As you walk down the street you hear a scream. Do you run towards the screams(help) or ignore them(continue): ')

                        # look-right-car-help
                        if choice.lower() == 'help':
                            print('You run towards the screams. There is a woman being attack by another one of those things.')
                            choice = input('Do you use your gun to shoot the zombie(shoot) or save your bullets and try to use your hands(hands): ')

                            # look-right-car-help-hands
                            if choice.lower() == 'hands':
                                print('You grab the zombie and pull it away from the woman. It turns it\'s attention to you now, biting a chunk out of your arm.')
                                print('The woman runs away terrified. You manage to beat the zombie with a nearby rock but quickly pass out from blood loss. When you wake up your\'re consumed with the urge to eat. The rest of your days are spent wondering around mindlessly looking for flesh')
                                print('GAME OVER')

                            # look-right-car-help-shoot
                            if choice.lower() == 'shoot':
                                print('You shoot the zombie in the head saving the woman. "Thank you", she says. "I thought I was going to die"')
                                print('The woman tells you about a group of people taking shelter at a nearby firehouse and offers you a place to stay there')
                                print('Congratulations! You have survied the into. Chapter 1 will becoming soon.')

                        # look-right-car-continue
                        if choice.lower() == 'continue':
                            print('You ignore the screams. You\'re not in any place to be offering help right now. You come across a mostly looted store but figured it can\'t hurt to look.')
                            print('As you\'re looking through the shelves a group of those monsters come in and block off your exit. You try to shoot them but theres too many.')
                            print('GAME OVER')


                # look-right-walk
                if choice.lower() == 'walk':
                    choice = input('As you walk down the street you hear a scream. Do you run towards the screams(help) or ignore them(continue): ')

                    # look-right-walk-help
                    if choice.lower() == 'help':
                        print('You run towards the screams. You see a woman being attacked by another one of those creatures. With no weapon in sight you grab the monster an pull it away from the woman. It turns it\'s attention to you now, biting a chunk out of your arm.')
                        print('The woman runs away terrified. You manage to beat the zombie with a nearby rock but quickly pass out from blood loss. When you wake up your\'re consumed with the urge to eat. The rest of your days are spent wondering around mindlessly looking for flesh')
                        print('GAME OVER')
                        
                    # look-right-walk-continue
                    if choice.lower() == 'continue':
                        print('You ignore the screams. You\'re not in any place to be offering help right now. You come across a mostly looted store but figured it can\'t hurt to look.')
                        print('As you\'re looking through the shelves a group of those monsters come in and block off your exit. You try to fight them off but theres too many of them.')
                        print('GAME OVER')


game()