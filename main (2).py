feliz_ano_novo = {
  "6": "F",
  "5": "E",
  "50": "L",
  "1": "I",
  "26": "Z",
  "MM": "2000",
  "R": "18"
}
# chaves individuais 
print(feliz_ano_novo["6"])
print(feliz_ano_novo["5"])
print(feliz_ano_novo["50"])
print(feliz_ano_novo["1"])
print(feliz_ano_novo["26"])
#print(feliz_ano_novo["MM"])
#print(feliz_ano_novo["R"])


parte1 = "MM:2000" 
parte2 = "R:18"

numero1 = parte1[3:]
numero2 = parte2[2:]



inteiro1 = int(numero1) 
inteiro2 = int(numero2)


resultado_para_feliz_2018 = inteiro1 + inteiro2
resultado_para_feliz_2018 = str(resultado_para_feliz_2018)

#print(" ".join(str(resultado_para_feliz_2018)))



print (resultado_para_feliz_2018) 
#str(resultado_para_feliz_2018)




