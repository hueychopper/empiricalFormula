import numpy as np
import math

print("#####################################################################################")
print("#                                                                                   #")
print("#                                                                                   #")
print("#                                                                                   #")
print("#       /---    /\  /\   |---     |----  ---   ---   /\  /\   |   | |       /\      #")
print("#      /---    /  \/  \  | __|    |--   |   | |     /  \/  \  |   | |      /--\     #")
print("#     /---    /        \ |     .  |      ---  |    /        \  ---  |___  /    \    #")
print("#                                                                                   #")
print("#                                                                                   #")
print("#                                                                                   #")
print("#                                                                                   #")
print("#####################################################################################")

elem_amount = int(input("How many elements: "))

def display_inputs(inputs):
    store_elem_name_mass = []
    mole_list = []

    if(inputs > 0):
        for i in range(1, inputs + 1):
            elem_types = str(input("element name: "))
            elem_mass = float(input("element mass: "))
            percents = float(input("element percentage of mass: "))

            # f_amnt = [str(elem_types[i])]
            # m_amnt = [float(elem_mass[i])]

            if elem_types and elem_mass and percents:
                store_elem_name_mass.append(elem_types)
                store_elem_name_mass.append(elem_mass)
                store_elem_name_mass.append(percents)
                #print(store_elem_name_mass)
                mole_num = percents / elem_mass
                total = round(mole_num)
                words = "It is"
                if total:
                    #mole_list.append(mole_num)
                    mole_list.append(total)
                    print(f'{words} {mole_num} rounded is {total}'.format(mole_num, total))  

                    mol_config = np.array(mole_list)
                    final = min(mol_config)   

        def final_formula(name, subscript):
            #find all string in list
            res = len([val for val in store_elem_name_mass if isinstance(val, str)])
            #loop through and divide all moles by smallest
            for x in mol_config:
                ur_moles = x / subscript
                ronded = round(ur_moles)
                print(ronded)
                mole_list.insert(0, ronded)
                try:
                    if res == 3:
                        mole_list.pop(3)
                except IndexError:
                    print(mole_list)
            print(ronded)

            mole_list.sort()
            print(store_elem_name_mass)
            print(mole_list)
        
            prompt = str(input("Would you like to see formula? [y/n]:  "))
            if prompt == "yes" or prompt == "y":
                if elem_types in store_elem_name_mass:
                    if res == 2:
                        print("is 2")
                        print(f'{store_elem_name_mass[0]}, {mole_list[0]}, {store_elem_name_mass[3]}, {mole_list[1]} is the formula')
                    elif res == 3:
                        print("is 3")
                        print(mole_list)
                        print(f'{store_elem_name_mass[0]}, {mole_list[0]}, {store_elem_name_mass[3]}, {mole_list[1]}, {store_elem_name_mass[6]}, {mole_list[2]} is your formula'.format())
                    elif res == 4:
                        print(f'{store_elem_name_mass[0]}, {mole_list[0]}, {store_elem_name_mass[3]}, {mole_list[1]}, {store_elem_name_mass[6]}, {mole_list[2]}, {store_elem_name_mass[9]}, {mole_list[3]}')
                    else:
                        print("there seems to be no output")
            else:
                    print("ok have fun at school")


        final_formula(elem_types, final)
    else:
        print("no")

display_inputs(elem_amount)



