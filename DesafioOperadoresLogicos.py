trabalho_terca = False
trabalho_quinta = False
tv_50 = trabalho_terca and trabalho_quinta
tv_30 = trabalho_terca != trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
mais_saudavel = not sorvete

print ("tv_50 {} tv_30 {} sorvete {} mais_saudavel {}"
       .format( tv_50, tv_30, sorvete, mais_saudavel))
