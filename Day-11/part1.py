monkeys = [
    {
        'starting_items':[79,98],
        'operation':('old','*',19),
        'test':23,
        'result':{
            True:2,
            False:3
        }
    },
    {
        'starting_items':[54,65,75,74],
        'operation':('old','+',6),
        'test':19,
        'result':{
            True:2,
            False:0
        }
    },
    {
        'starting_items':[79,60,97],
        'operation':('old','+','old'),
        'test':13,
        'result':{
            True:1,
            False:3
        }
    },
    {
        'starting_items':[74],
        'operation':('old','+',3),
        'test':17,
        'result':{
            True:0,
            False:1
        }
    }
]

for monkey in monkeys:
    for item in monkey['starting_items']:
        print(item)