#!usr/bin python3

from inspect import currentframe, getframeinfo

cf = currentframe()

import time

import math

a = str(input("What do you want to calculate ?"))

a = " ".join(a)

split = str.split(a)

temp_nb = []

prioridad_l = ["*", "raccord", "*", -1, "exp", "log", "ln", -1, "*", "/", -1, "+", "-"]

ressources = ["[", "]", "t", "v", "m", "M", "ro", "+", "-", "(", ")", "*", "/", "**", "exp", "ln", "log"]

str_nb = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "0.3"]

formula = []

formula_f = []

t = 0

C = 3

resultat = []

para = 0

position = 0

t2 = 0

nb_potential = 0

cro_count = 0

u2 = 0

index_l = []

t_plusdinspi = 0

while t < len(split):

    u = 0

    resultat.append(0)

    index_l.append(0)

    if split[t] == "r":

        formula.append("r")

    if split[t] == "|":

        formula.append("|")

    if split[t] == "!":

        formula.append("!")

    if split[t] == "e":

        formula.append("exp")

    if split[t] == "l" and split[t + 1] == "o" and split[t + 2] == "g":
        formula.append("log")

    if split[t] == "l" and split[t + 1] == "n":

        formula.append("ln")

    if split[t] == "s" and split[t + 1] == "i" and split[t - 1] != "a":

        formula.append("sin")

    if split[t] == "t" and split[t + 1] == "a" and split[t - 1] != "a":

        formula.append("tan")

    if split[t] == "c" and split[t + 1] == "o" and split[t - 1] != "a":

        formula.append("cos")

    if split[t] == "a" and split[t + 1] == "s":

        formula.append("asin")

    if split[t] == "a" and split[t + 1] == "c":

        formula.append("acos")

    if split[t] == "a" and split[t + 1] == "t":

        formula.append("atan")

    if split[t] == "C" and split[t + 1] == "_":

        formula.append("C")

        split.insert(t + 2, "0.3")

        t_plusdinspi = t + 2

        laterriblefin = 0

        passela = 0

        while laterriblefin == 0:   

            if str_nb.count(split[t_plusdinspi]) > 0:

                if split[t_plusdinspi] != "0.3":

                    lajoutstr = split[t_plusdinspi]

                    lajoutstr2 = formula[-1]

                    lajoutstr3 = lajoutstr2 + lajoutstr

                    formula[-1] = lajoutstr3

            if t_plusdinspi + 2 > len(split):

                laterriblefin = 1

            if str_nb.count(split[t_plusdinspi]) == 0:

                laterriblefin = 1

            t_plusdinspi += 1

        if laterriblefin == 1:

            t_plusdinspi = t + 2

            while str_nb.count(split[t_plusdinspi]) > 0 and t_plusdinspi + 1 < len(split):

                split.pop(t_plusdinspi)

            if t_plusdinspi + 1 == len(split) or str_nb.count(split[t_plusdinspi]) > 0:

                split.pop(t_plusdinspi - 1)

                if str_nb.count(split[t_plusdinspi - 1]) > 0:

                    split.pop(t_plusdinspi - 1)

    if split[t] == "m" and split[t + 1] == "_":

        formula.append("m")

        split.insert(t + 2, "0.3")

        t_plusdinspi = t + 2

        laterriblefin = 0

        passela = 0

        while laterriblefin == 0:   

            if str_nb.count(split[t_plusdinspi]) > 0:

                if split[t_plusdinspi] != "0.3":

                    lajoutstr = split[t_plusdinspi]

                    lajoutstr2 = formula[-1]

                    lajoutstr3 = lajoutstr2 + lajoutstr

                    formula[-1] = lajoutstr3

            if t_plusdinspi + 2 > len(split):

                laterriblefin = 1

            if str_nb.count(split[t_plusdinspi]) == 0:

                laterriblefin = 1

            t_plusdinspi += 1

        if laterriblefin == 1:

            t_plusdinspi = t + 2

            while str_nb.count(split[t_plusdinspi]) > 0 and t_plusdinspi + 1 < len(split):

                split.pop(t_plusdinspi)

            if t_plusdinspi + 1 == len(split) or str_nb.count(split[t_plusdinspi]) > 0:

                split.pop(t_plusdinspi - 1)

                if str_nb.count(split[t_plusdinspi - 1]) > 0:

                    split.pop(t_plusdinspi - 1)

    if split[t] == "v" and split[t + 1] == "_":

        formula.append("v")

        split.insert(t + 2, "0.3")

        t_plusdinspi = t + 2

        laterriblefin = 0

        passela = 0

        while laterriblefin == 0:   

            if str_nb.count(split[t_plusdinspi]) > 0:

                if split[t_plusdinspi] != "0.3":

                    lajoutstr = split[t_plusdinspi]

                    lajoutstr2 = formula[-1]

                    lajoutstr3 = lajoutstr2 + lajoutstr

                    formula[-1] = lajoutstr3

            if t_plusdinspi + 2 > len(split):

                laterriblefin = 1

            if str_nb.count(split[t_plusdinspi]) == 0:

                laterriblefin = 1

            t_plusdinspi += 1

        if laterriblefin == 1:

            t_plusdinspi = t + 2

            while str_nb.count(split[t_plusdinspi]) > 0 and t_plusdinspi + 1 < len(split):

                split.pop(t_plusdinspi)

            if t_plusdinspi + 1 == len(split) or str_nb.count(split[t_plusdinspi]) > 0:

                split.pop(t_plusdinspi - 1)

                if str_nb.count(split[t_plusdinspi - 1]) > 0:

                    split.pop(t_plusdinspi - 1)

    if split[t] == "t" and split[t + 1] == "_":

        formula.append("t")

        split.insert(t + 2, "0.3")

        t_plusdinspi = t + 2

        laterriblefin = 0

        passela = 0

        while laterriblefin == 0:   

            if str_nb.count(split[t_plusdinspi]) > 0:

                if split[t_plusdinspi] != "0.3":

                    lajoutstr = split[t_plusdinspi]

                    lajoutstr2 = formula[-1]

                    lajoutstr3 = lajoutstr2 + lajoutstr

                    formula[-1] = lajoutstr3

            if t_plusdinspi + 2 > len(split):

                laterriblefin = 1

            if str_nb.count(split[t_plusdinspi]) == 0:

                laterriblefin = 1

            t_plusdinspi += 1

        if laterriblefin == 1:

            t_plusdinspi = t + 2

            while str_nb.count(split[t_plusdinspi]) > 0 and t_plusdinspi + 1 < len(split):

                split.pop(t_plusdinspi)

            if t_plusdinspi + 1 == len(split) or str_nb.count(split[t_plusdinspi]) > 0:

                split.pop(t_plusdinspi - 1)

                if str_nb.count(split[t_plusdinspi - 1]) > 0:

                    split.pop(t_plusdinspi - 1)

    if split[t - 1] == "p" and split[t] == "H" and split[t + 1] == "_":

        formula.append("pH")
        
        split.insert(t + 2, "0.3")

        t_plusdinspi = t + 2

        laterriblefin = 0

        passela = 0

        while laterriblefin == 0:   

            if str_nb.count(split[t_plusdinspi]) > 0:

                if split[t_plusdinspi] != "0.3":

                    lajoutstr = split[t_plusdinspi]

                    lajoutstr2 = formula[-1]

                    lajoutstr3 = lajoutstr2 + lajoutstr

                    formula[-1] = lajoutstr3

            if t_plusdinspi + 2 > len(split):

                laterriblefin = 1

            if str_nb.count(split[t_plusdinspi]) == 0:

                laterriblefin = 1

            t_plusdinspi += 1

        if laterriblefin == 1:

            t_plusdinspi = t + 2

            while str_nb.count(split[t_plusdinspi]) > 0 and t_plusdinspi + 1 < len(split):

                split.pop(t_plusdinspi)

            if t_plusdinspi + 1 == len(split) or str_nb.count(split[t_plusdinspi]) > 0:

                split.pop(t_plusdinspi - 1)

                if str_nb.count(split[t_plusdinspi - 1]) > 0:

                    split.pop(t_plusdinspi - 1)

    if split[t - 1] == "r" and split[t] == "o" and split[t + 1] == "_":

        formula.append("ro")

        split.insert(t + 2, "0.3")

        t_plusdinspi = t + 2

        laterriblefin = 0

        passela = 0

        while laterriblefin == 0:   

            if str_nb.count(split[t_plusdinspi]) > 0:

                if split[t_plusdinspi] != "0.3":

                    lajoutstr = split[t_plusdinspi]

                    lajoutstr2 = formula[-1]

                    lajoutstr3 = lajoutstr2 + lajoutstr

                    formula[-1] = lajoutstr3

            if t_plusdinspi + 2 > len(split):

                laterriblefin = 1

            if str_nb.count(split[t_plusdinspi]) == 0:

                laterriblefin = 1

            t_plusdinspi += 1

        if laterriblefin == 1:

            t_plusdinspi = t + 2

            while str_nb.count(split[t_plusdinspi]) > 0 and t_plusdinspi + 1 < len(split):

                split.pop(t_plusdinspi)

            if t_plusdinspi + 1 == len(split) or str_nb.count(split[t_plusdinspi]) > 0:

                split.pop(t_plusdinspi - 1)

                if str_nb.count(split[t_plusdinspi - 1]) > 0:

                    split.pop(t_plusdinspi - 1)

    if split[t - 1] == "Q" and split[t] == "r" and split[t + 1] == "_":

        formula.append("Qr")
       
        split.insert(t + 2, "0.3")

        t_plusdinspi = t + 2

        laterriblefin = 0

        passela = 0

        while laterriblefin == 0:   

            if str_nb.count(split[t_plusdinspi]) > 0:

                if split[t_plusdinspi] != "0.3":

                    lajoutstr = split[t_plusdinspi]

                    lajoutstr2 = formula[-1]

                    lajoutstr3 = lajoutstr2 + lajoutstr

                    formula[-1] = lajoutstr3

            if t_plusdinspi + 2 > len(split):

                laterriblefin = 1

            if str_nb.count(split[t_plusdinspi]) == 0:

                laterriblefin = 1

            t_plusdinspi += 1

        if laterriblefin == 1:

            t_plusdinspi = t + 2

            while str_nb.count(split[t_plusdinspi]) > 0 and t_plusdinspi + 1 < len(split):

                split.pop(t_plusdinspi)

            if t_plusdinspi + 1 == len(split) or str_nb.count(split[t_plusdinspi]) > 0:

                split.pop(t_plusdinspi - 1)

                if str_nb.count(split[t_plusdinspi - 1]) > 0:

                    split.pop(t_plusdinspi - 1)

    if split[t] == "n" and split[t + 1] == "_":

        formula.append("n")

        split.insert(t + 2, "0.3")

        t_plusdinspi = t + 2

        laterriblefin = 0

        passela = 0

        while laterriblefin == 0:   

            if str_nb.count(split[t_plusdinspi]) > 0:

                if split[t_plusdinspi] != "0.3":

                    lajoutstr = split[t_plusdinspi]

                    lajoutstr2 = formula[-1]

                    lajoutstr3 = lajoutstr2 + lajoutstr

                    formula[-1] = lajoutstr3

            if t_plusdinspi + 2 > len(split):

                laterriblefin = 1

            if str_nb.count(split[t_plusdinspi]) == 0:

                laterriblefin = 1

            t_plusdinspi += 1

        if laterriblefin == 1:

            t_plusdinspi = t + 2

            while str_nb.count(split[t_plusdinspi]) > 0 and t_plusdinspi + 1 < len(split):

                split.pop(t_plusdinspi)

            if t_plusdinspi + 1 == len(split) or str_nb.count(split[t_plusdinspi]) > 0:

                split.pop(t_plusdinspi - 1)

                if str_nb.count(split[t_plusdinspi - 1]) > 0:

                    split.pop(t_plusdinspi - 1)

    if split[t] == "(":

        formula.append(split[t])

    if split[t] == ")":

        formula.append(split[t])

    moved = 0

    while t2 < len(str_nb):

        if split[t] == str_nb[t2] and cro_count != 1:

            position = len(formula)

            temp_nb.append(split[t])

            nb_potential = 1

            t2 = len(str_nb)

            u = 1

            u2 = 1

        if split[t] == "." and cro_count != 1:

            temp_nb.append(split[t])

            t2 = len(str_nb)   

            u = 1

            u2 = 1

        t2 +=  1

    t2 = 0

    if u == 0 and u2 == 1 or u2 == 1 and t + 1 == len(split):

        nb_potential = 0

        temp_nb = "".join(temp_nb)

        formula.insert(position, float(temp_nb))

        temp_nb = []

        u2 = 0

    if split[t] == "+" or split[t] == "-" or split[t] == "*" or split[t] == "/":

        formula.append(split[t])

    t += 1

t = 0

formula2 = []

while t < len(formula):

    formula2.append(formula[t])

    t += 1

t = 0

para = 0

cro_count = 0

ajout_l = []

t2 = 0

t2b = 0

c = formula.count("(")

para_end_count = 0

score_para = []

num_para = []

t3 = 0

t4 = 0

while t3 < len(formula):

    if formula[t3] == "(":

        num_para.insert(para, para)

        para += 1

    t3 += 1

t3 = 0

para_end_count = 0

prem_l = []

len_l = []

while t3 < len(num_para):

    len_l.insert(0, 0)

    score_para.insert(0, 0)

    prem_l.insert(0, 0)

    t3 += 1

t3 = 0

u = 0

t4 = 0

t4 = 0

prem = 0

num_para2 = []

while t4 < len(num_para):

    num_para2.insert(t4, num_para[t4])

    t4 += 1

t4 = 0

para = 0

depart_l = []

fin_l = []

while t3 < len(formula):

    if formula[t3] == "(":

        depart_l.append(t3)

        para += 1

        while t4 < para:

            score_para[t4] += 1

            t4 += 1

        t4 = 0

    if formula[t3] == ")":

        fin_l.append(t3)

        while t4 < para:

            score_para[t4] -= 1

            if score_para[t4] > 0:

                len_l[t4] += 1

            if score_para[t4] == 0 and prem_l[t4] != -2:

                prem_l[t4] = -2

                u = num_para2[t4]

                num_para.insert(num_para.index(u) + len_l[t4] * 2 + 1, u)

            t4 += 1

        t4 = 0

    t3 += 1

t3 = 0

t4 = 0

num_para2 = []

while t4 < len(num_para):

    num_para2.insert(t4, num_para[t4])

    t4 += 1 

t4 = 0

t5 = 0

egal = 0

passed = 0

passed2 = 0

autorise = 0

nouveau_para = -1

t6_f = 0

ctn = 0

t6 = 0

t7 = 0

para_joker = 0

last = 0

t8 = 0

rela_t = 0

last_index = []

long_num_para = len(num_para)

rela_t_f = 0

num_para_persistant = []

t_subliminal = 0

while t_subliminal < len(num_para):

    num_para_persistant.append(num_para[t_subliminal])

    t_subliminal += 1 

t = 0

while t < len(formula):

    if type(formula[t]) == float and formula[t - 1] == "-" and type(formula[t - 2]) == str \
            or type(formula[t]) == float and formula[t - 1] == "-" and t == 1:

        formula[t - 1] = -formula[t]

        formula.pop(t)

    t += 1

t = 0

t_tron = 0

c_la = -1

while t_tron < len(formula):

    if formula[t_tron] == "(":

        c_la += 1

    if t_tron + 2 < len(formula):

        if formula[t_tron] == "(" and type(formula[t_tron + 1]) == float and formula[t_tron + 2] == ")":

            formula[t_tron] = formula[t_tron + 1]

            formula.pop(t_tron + 1)

            formula.pop(t_tron + 1)

            num_para.remove(c_la)

            num_para.remove(c_la)

            num_para2.remove(c_la)

            num_para2.remove(c_la)

    t_tron += 1

t_tron = 0

moved = 0

t2 = 0

position_l = []

position = 0

while t2 < len(formula):

    if formula[t2] == "(":

        position_l.append(t2)

        position += 1

    if formula[t2] == ")":

        position_l.append(t2)

    t2 += 1

t2 = 0

para = 0

complete = 0

depart = 0

t = 0

t_num_para = 0

sommus_l = []

t_sommus = 0

while t < len(formula):

    sommus_l.append(0)

    t += 1

t = 0

moved = 0

para_ferm = 0

beg = 0

deca = 0

sommus_val = 0

t = 0

prc = 0

t_dvr = 0

formula_lf = []

t_fact = 0

facto = 0

while len(num_para) > 0:

    t = para + sommus_val

    while formula[t] != ")":   

        t += 1

    para_ferm = t 

    if beg == 1:

        formula.pop(para + sommus_val)   

        formula.pop(para_ferm - 1)

        sommus_l[para] = sommus_l[para] - 1
    
        sommus_l[para + (para_ferm - para - sommus_val) - 1] = sommus_l[para + (para_ferm - para - sommus_val) - 1] - 1
        
        num_para.remove(deca)

        num_para.remove(deca)

    eldmn = 0

    t = 0

    beg = 1

    while t < len(num_para):

        if num_para[t - 1] == num_para[t] and t > 0:

            deca = num_para[t]

            para = position_l[num_para_persistant.index(deca)]

            t = len(num_para)

        t += 1

    sommus_val = 0

    while t_sommus < para:

        sommus_val = sommus_val + sommus_l[t_sommus]

        t_sommus += 1

    t_sommus = 0

    prc = 0

    t = para + sommus_val

    tdeff = para + sommus_val

    while formula[t] != ")" and len(num_para) > 0:

        if type(formula[t - 1]) == float and formula[t] == "!":

            formula[t - 1] = int(formula[t - 1])

            formula[t - 1] = math.factorial(formula[t - 1])

            formula[t - 1] = float(formula[t - 1])

            formula.pop(t)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 1   

            moved = 1

            t = para + sommus_val

        if formula[t - 1] == "r" and type(formula[t]) == float:

            formula[t - 1] = math.radians(formula[t])

            formula.pop(t)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 1   

            moved = 1

            t = para + sommus_val

        if formula[t - 1] == "ln" and type(formula[t]) == float:

            formula[t - 1] = math.log(formula[t])

            formula.pop(t)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 1   

            moved = 1

            t = para + sommus_val

        if formula[t - 1] == "exp" and type(formula[t]) == float:

            formula[t - 1] = math.exp(formula[t])

            formula.pop(t)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 1

            moved = 1

            t = para + sommus_val

        if formula[t - 1] == "log" and type(formula[t]) == float:

            formula[t - 1] = math.log(formula[t]) / math.log(10)

            formula.pop(t)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 1

            moved = 1

            t = para + sommus_val

        if formula[t - 1] == "sin" and type(formula[t]) == float:

            formula[t - 1] = math.sin(formula[t])

            formula.pop(t)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 1

            moved = 1

            t = para + sommus_val

        if formula[t - 1] == "tan" and type(formula[t]) == float:

            formula[t - 1] = math.tan(formula[t])

            formula.pop(t)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 1

            moved = 1

            t = para + sommus_val           

        if formula[t - 1] == "cos" and type(formula[t]) == float:

            formula[t - 1] = math.cos(formula[t])

            formula.pop(t)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 1

            moved = 1

            t = para + sommus_val

        if formula[t - 1] == "sqr" and type(formula[t]) == float:

            formula[t - 1] = math.sqrt(formula[t])

            formula.pop(t)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 1

            moved = 1

            t = para + sommus_val 

        if formula[t - 1] == "acos" and type(formula[t]) == float:

            formula[t - 1] = math.acos(formula[t])

            formula.pop(t)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 1

            moved = 1

            t = para + sommus_val

        if formula[t - 1] == "asin" and type(formula[t]) == float:

            formula[t - 1] = math.asin(formula[t])

            formula.pop(t)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 1

            moved = 1

            t = para + sommus_val

        if formula[t - 1] == "atan" and type(formula[t]) == float:

            formula[t - 1] = math.atan(formula[t])

            formula.pop(t)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 1

            moved = 1

            t = para + sommus_val

        if formula[t - 1] == "atanh" and type(formula[t]) == float:

            formula[t - 1] = math.atanh(formula[t])

            formula.pop(t)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 1

            moved = 1

            t = para + sommus_val      

        if formula[t - 1] == "asinh" and type(formula[t]) == float:

            formula[t - 1] = math.asinh(formula[t])

            formula.pop(t)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 1

            moved = 1

            t = para + sommus_val

        if formula[t - 1] == "acosh" and type(formula[t]) == float:

            formula[t - 1] = math.acosh(formula[t])

            formula.pop(t)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 1

            moved = 1

            t = para + sommus_val

        t += 1

    t = para + sommus_val 

    while formula[t] != ")" and len(num_para) > 0:

        if formula[t - 1] == "*" and formula[t - 2] == "*" and type(formula[t]) == float\
                and type(formula[t - 3]) == float:

            formula[t - 3] = formula[t - 3] ** formula[t]

            formula.pop(t - 2)

            formula.pop(t - 2)

            formula.pop(t - 2)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 3

            moved = 1

            t = para + sommus_val

        t += 1

    t = para + sommus_val

    tdeff = para + sommus_val

    while formula[t] != ")" and len(num_para) > 0:

        if formula[t - 1] == "*" and type(formula[t - 2]) == float and type(formula[t]) == float:

            formula[t - 2] = formula[t - 2] * formula[t]

            formula.pop(t - 1)

            formula.pop(t - 1)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 2

            moved = 1

            t = para + sommus_val

        if formula[t - 1] == "/" and type(formula[t - 2]) == float and type(formula[t]) == float:

            formula[t - 2] = formula[t - 2] / formula[t]

            formula.pop(t - 1)

            formula.pop(t - 1)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 2

            moved = 1

            t = para + sommus_val

        t += 1

    t = para + sommus_val

    while formula[t] != ")" and len(num_para) > 0:

        if formula[t - 1] == "+" and type(formula[t - 2]) == float and type(formula[t]) == float:

            formula[t - 2] = formula[t - 2] + formula[t]

            formula.pop(t - 1)

            formula.pop(t - 1)

            sommus_l[para + abs(t - tdeff)] = sommus_l[para + abs(t - tdeff)] - 2

            moved = 1

            t = para + sommus_val

        if formula[t - 1] == "-" and type(formula[t - 2]) == float and type(formula[t]) == float:

            formula[t - 2] = formula[t - 2] - formula[t]

            formula.pop(t - 1)

            formula.pop(t - 1)

            sommus_l[para + abs(tdeff - t)] = sommus_l[para + abs(t - tdeff)] - 2

            moved = 1

            t = para + sommus_val

        t += 1

    t = para + sommus_val

    while formula[t] != ")" and len(num_para) > 0:

        if formula[t - 2] == "|" and formula[t] == "|" and type(formula[t - 1]) == float:
            
            formula[t - 2] = abs(formula[t - 1])

            formula.pop(t - 1)

            formula.pop(t - 1)

            sommus_l[para + abs(tdeff - t)] = sommus_l[para + abs(t - tdeff)] - 2

            moved = 1

            t = para + sommus_val

        t += 1

t = 0

while t < len(formula):

    if formula[t - 1] == "r" and type(formula[t]) == float:

        formula[t - 1] = math.radians(formula[t])

        formula.pop(t)

        t = 0

        moved = 0
       
    if type(formula[t - 1]) == float and formula[t] == "!":

        formula[t - 1] = int(formula[t - 1])

        formula[t - 1] = math.factorial(formula[t - 1])

        formula[t - 1] = float(formula[t - 1])

        formula.pop(t)

        t = 0

    if formula[t - 1] == "ln" and type(formula[t]) == float:

        formula[t - 1] = math.log(formula[t])

        formula.pop(t)

        moved = 1

        t = 0

    if formula[t - 1] == "exp" and type(formula[t]) == float:

        formula[t - 1] = math.exp(formula[t])

        formula.pop(t)

        moved = 1

        t = 0

    if formula[t - 1] == "log" and type(formula[t]) == float:

        formula[t - 1] = math.log(formula[t]) / math.log(10)

        formula.pop(t)

        moved = 1

        t = 0

    if formula[t - 1] == "sin" and type(formula[t]) == float:

        formula[t - 1] = math.sin(formula[t])

        formula.pop(t)

        moved = 1

        t = 0

    if formula[t - 1] == "tan" and type(formula[t]) == float:

        formula[t - 1] = math.tan(formula[t])

        formula.pop(t)

        moved = 1

        t = 0       

    if formula[t - 1] == "cos" and type(formula[t]) == float:

        formula[t - 1] = math.cos(formula[t])

        formula.pop(t)

        moved = 1

        t = 0

    if formula[t - 1] == "sqr" and type(formula[t]) == float:

        formula[t - 1] = math.sqrt(formula[t])

        formula.pop(t)

        moved = 1

        t = 0

    if formula[t - 1] == "acos" and type(formula[t]) == float:

        formula[t - 1] = math.acos(formula[t])

        formula.pop(t)

        moved = 1

        t = 0

    if formula[t - 1] == "asin" and type(formula[t]) == float:

        formula[t - 1] = math.asin(formula[t])

        formula.pop(t)

        moved = 1

        t = 0

    if formula[t - 1] == "atan" and type(formula[t]) == float:

        formula[t - 1] = math.atan(formula[t])

        formula.pop(t)

        moved = 1

        t = 0

    if formula[t - 1] == "atanh" and type(formula[t]) == float:

        formula[t - 1] = math.atanh(formula[t])

        formula.pop(t)

        moved = 1

        t = 0 

    if formula[t - 1] == "asinh" and type(formula[t]) == float:

        formula[t - 1] = math.asinh(formula[t])

        formula.pop(t)

        moved = 1

        t = 0

    if formula[t - 1] == "acosh" and type(formula[t]) == float:

        formula[t - 1] = math.acosh(formula[t])

        formula.pop(t)

        moved = 1

        t = 0

    t += 1

t = 0

while t < len(formula):

    if formula[t - 1] == "*" and formula[t - 2] == "*" and type(formula[t]) == float\
            and type(formula[t - 3]) == float:

        formula[t - 3] = formula[t - 3] ** formula[t]

        formula.pop(t - 2)

        formula.pop(t - 2)

        formula.pop(t - 2)

        moved = 1

        t = 0

    t += 1

t = 0

tdeff = para + sommus_val

while t < len(formula):

    if formula[t - 1] == "*" and type(formula[t - 2]) == float and type(formula[t]) == float:

        formula[t - 2] = formula[t - 2] * formula[t]

        formula.pop(t - 1)

        formula.pop(t - 1)

        moved = 1

        t = 0

    if formula[t - 1] == "/" and type(formula[t - 2]) == float and type(formula[t]) == float:

        formula[t - 2] = formula[t - 2] / formula[t]

        formula.pop(t - 1)

        formula.pop(t - 1)

        moved = 1

        t = 0

    t += 1

t = 0

while t < len(formula):

    if formula[t - 1] == "+" and type(formula[t - 2]) == float and type(formula[t]) == float:

        formula[t - 2] = formula[t - 2] + formula[t]

        formula.pop(t - 1)

        formula.pop(t - 1)

        moved = 1

        t = 0

    if formula[t - 1] == "-" and type(formula[t - 2]) == float and type(formula[t]) == float:

        formula[t - 2] = formula[t - 2] - formula[t]

        formula.pop(t - 1)

        formula.pop(t - 1)

        moved = 1

        t = 0

    t += 1
    
while t < len(formula):

    if formula[t - 2] == "|" and formula[t] == "|" and type(formula[t - 1]) == float:
        
        formula[t - 2] = abs(formula[t - 1])

        formula.pop(t - 1)

        formula.pop(t - 1)

        moved = 1

        t = 0

    t += 1

print(formula)

