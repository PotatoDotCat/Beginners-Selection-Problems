print('you are searching for treasure in a rainforest thwere mwite bwe tweaswer uwu')
print('wowweeee a lake!!!!')
print('swim or wait?')
ans = str(input('>>'))
if ans == 'swim':
    print('you got eaten by bobstradamus the III, which is a shark smaller than a slice of toast. Skill issue, smh')
elif ans == "wait":
    print('yay u get picked up by bob the boatman')
    print('we are not finished yet!')
    print('you come to a cave. venture or walk?')
    bre = str(input(">>"))
    if bre == "venture":
        print('a boulder rolls past, that was close')
        print('you see a big fat juicy leg of ham in a clearing.What do you do? (eat/run/stare)')
        cronge = str(input(">>"))
        if cronge == 'eat':
            print('you died from diabetes. Seriously????')
        elif cronge == 'stare':
            print('your intrusive thoughts made you eat the leg of ham, giving you diabetes. You die')
        elif cronge == "run":
            print('the leg of ham chases after you, buut it gets tired so you survive.')
            print('you come across a fork in the path')
            print('which way do you go? (left/forward/right)')
            oof = str(input('>>'))
            if oof == 'left':
                print('HOW MANY TIMES DO I HAVE TO SAY THIS??? LEFT IS NOT RIGHT')
            elif oof == 'forward':
                print('you fall into an invisible hole, never to be seen again.')
            elif oof == "right":
                print("yayyyyy you find the buried treasure!!!!!! you dont have a shovel so you dig for five years with your hand and finally get one gold coin. You win!")
            else:
                print('the grammar god sent his pet poodle to bite you. You died to rabies.')
        else:
            print('the grammar god clonked you over the head with a leg of ham, what an anticlimatic way to die')
    elif bre == "walk":
        print("lol u got squisheeed")
    else:
        print('the grammar god sent you to get the milk')
else: 
    print('you died to the grammar god for commiting sacrilege by typing an incoherent answer LOL')
