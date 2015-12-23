import random
import sys

spells = {
    'MagicMissile': 53,
    'Drain': 73,
    'Shield': 113,
    'Poison': 173,
    'Recharge': 229
}
boss_hit = 58
boss_damage = 9
own_hit = 50
own_mana = 500
own_armor = 0


def play_game():
    b_hit = boss_hit
    o_hit = own_hit
    o_armor = own_armor
    o_mana = own_mana
    shield_timer = 0
    poison_timer = 0
    recharge_timer = 0
    spend_mana = 0
    i = 0

    while o_hit > 0 and b_hit > 0:
        # Difficulty hard, you lose 1 point every round
        o_hit -= 1

        # if i % 2 == 0:
        #     print('-- Player turn --')
        # else:
        #     print('-- Boss turn --')
        # print('- Player has ' + str(o_hit) + ' hit points, ' + str(o_armor) + ' armor, ' + str(o_mana) + ' mana')
        # print('- Boss has ' + str(b_hit) + ' hit points')

        if o_hit > 0 and b_hit > 0:
            if i % 2 == 0:  # My turn
                spell = None

                for j in xrange(100):
                    spell = random.choice(spells.keys())
                    if not (spell == 'Shield' and shield_timer > 0) or \
                            (spell == 'Poison' and poison_timer > 0) or \
                            (spell == 'Recharge' and recharge_timer > 0):
                        if o_mana >= spells[spell]:
                            o_mana -= spells[spell]
                            spend_mana += spells[spell]
                            break
                        else:
                            spell = None

                if spell == 'MagicMissile':
                    # print('Player casts Magic Missile.')
                    b_hit -= 4
                elif spell == 'Drain':
                    # print('Player casts Drain.')
                    b_hit -= 2
                    o_hit += 2
                elif spell == 'Shield':
                    # print('Player casts Shield.')
                    shield_timer = 6
                    o_armor = 7
                elif spell == 'Poison':
                    # print('Player casts Poison.')
                    poison_timer = 6
                elif spell == 'Recharge':
                    # print('Player casts Recharge.')
                    recharge_timer = 5
                else:
                    return sys.maxint
            else:  # Boss turn
                # print('Boss attacks for ' + str(boss_damage - o_armor) + ' damage')
                o_hit -= (boss_damage - o_armor) if (boss_damage - o_armor) > 1 else 1

        # print('')

        if o_hit > 0 and b_hit > 0:
            if shield_timer == 0:
                o_armor = 0
            if shield_timer > 0:
                # print('Shield timer')
                shield_timer -= 1
            if poison_timer > 0:
                # print('Poison timer')
                b_hit -= 3
                poison_timer -= 1
            if recharge_timer > 0:
                # print('Recharge timer')
                o_mana += 101
                recharge_timer -= 1

        i += 1

    return spend_mana if o_hit > 0 else sys.maxint

min_mana = sys.maxint
for i in xrange(1000000):
    costs = play_game()
    if costs < min_mana:
        min_mana = costs

print(min_mana)
