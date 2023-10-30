from decimal import Decimal
import random

prb = ["1/{}=__._%?".format(i) for i in range(2,21)]
sol = [str(Decimal(100/i).quantize(Decimal('0.0'))) for i in range(2,21)]
sol[-5] = '6.3'                            # precision error fixed by hand
totest = dict(zip(prb, sol))

print(' ---- preview ----')
print(totest)
print(' --- begin test ---')

while True:
    txt = random.sample(prb,1)[0]
    print(txt, end=' ')
    ans = input()
    # if ans in ['exit()', 'exit']: 
    if ans == 'exit()' or ans == 'exit':   # press 'ctrl+c' to stop as well
        break
    print('Right') if ans == totest[txt] else print('Wrong, right answer = {}'.format(totest[txt]))


print(' --- end test ---')
print(' ---- review ----')
print(totest)
