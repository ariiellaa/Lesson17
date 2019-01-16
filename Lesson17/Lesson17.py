import time 
import random

print()
print('-' * 60)
print('A wild Jigglypuff appears!')
time.sleep(0.2)
print('you only have one pokemon, Snorlax.')
time.sleep(0.2)
print('I choose you Snorlax!!!!!')
print()
time.sleep(0.2)

# starting HPs
snorlax_hp = 200
jiggly_hp = 125

print('Battle Options:')
time.sleep(0.2)
print('- [1] Sleep Heal')
time.sleep(0.2)
print('- [2] Tackle')
time.sleep(0.2)
print('- [3] Roundhouse kick')
time.sleep(0.2)
print('- [4] Hyper Beam')
time.sleep(0.2)
your_move = input('choose a move using the corresponding number:')
if your_move == '1':
	snorlax_hp = snorlax_hp + 50
	Print('Snorlax uses sleep Heal, his HP increases to ' + str(snorlax_hp))
elif your_move == '2':
	jiggly_hp = jiggly_hp - 10
	print('Snorlax uses tackle and deals 10 damage to jigglypuff!')
	time.sleep(0.2)
elif your_move == '3':
	jiggly_hp = jiggly_hp - 30
	print('Snorlax uses Roundhouse Kick and deals 30 damage to jigglypuff!')
	time.sleep(0.2)
elif your_move == '4':
	jiggly_hp = jiggly_hp - 40
	print('Snorlax uses hyperbeam and deals 40 damage to jigglypuff!')
	time.sleep(0.2)
print()

#jigglypuff attacks
enemy_move = random.randint(1,2)
enemy_move = str(enemy_move)

if enemy_move == '1':
	snorlax_hp = snorlax_hp - 30 
	jiggly_puff = jiggly_puff + 30 
	print ('Jigglypuff uses Drink Blood and deals 30 HP of damage whhile recovering.')
	time.sleep(0.2)
elif enemy_move == '2':
	snorlax_hp = snorlax_hp - 50 
	print('Jigglypuff uses Breath Fire and deals 50 HP og damage.')
	time.print(0.2)
print()

print('updated HP')
time.sleep(0.2)
print('- Snorlax Hp: ' + str(strsnorlax_hp))
time.sleep(0.2)
print('- jiggypuff HP: ' + str(jiggly_hp))
time.sleep(0.2)
print()
time.sleep(0.2)