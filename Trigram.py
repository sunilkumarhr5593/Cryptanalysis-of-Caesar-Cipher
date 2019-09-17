import pandas
import itertools
from math import log
import math
import numpy as np

df_trigram = pandas.read_csv('count3l.txt',index_col=None, delim_whitespace=True, names=('trigram', 'prob'))
#print(df_trigram)

new_sum_3 = df_trigram.sum(axis = 0, skipna = False)  # sums all prob of bigram
total_prob_3 = (new_sum_3[0]) 
#print("The log value total occurence from the trigram data is: ",np.log2(total_prob_3))           # total prob of all bigram
#print()

avg_prob_3 = []

df1_3 = (df_trigram.iloc[:,1]) / (total_prob_3) #first row of data frame
avg_prob_3 = np.log2(df1_3)
#print(avg_prob_3)
#print(total_prob)  

trigram_prob = [] 
tprob= df_trigram.iloc[:,0]
trigram_prob = tprob                                                                 ##########
#print(bigram_prob)  

max_prob = max(avg_prob_3) 
#print("The log value of max prob is: ",max_prob)

dict_prob_3 = dict((trigram_prob[index], avg_prob_3[index]) for index in range(len(trigram_prob)))
#print("The bigram:",dict_prob_3, sep = " ")

### testing purpose
#print(list(dict_prob_3.keys())[2])   # output >>> Key2
#print(list(dict_prob_3.values())[2])  # output >>> Value2

############ Cryptanalysis of Caesar cipher #########################################

alphabets = 'abcdefghijklmnopqrstuvwxyz'   # Alphabets in english language
text = input('Enter the string :')        # Input message
print()
#text = "hello"
shift = 12 

def encrypt(n, plaintext):                 # Function used for encryption to get cipher text
    result = ''

# Since lower case alphabets is used as the plain text.
# Here index of the input string will be considered and shift value will be added,
# and performs modulo operation for encryption
    for l in plaintext.lower():    
        try:
            i = (alphabets.index(l) + shift) % 26   
            result += alphabets[i]
        except ValueError:
            result += l

    return result.lower()

encrypted = encrypt(shift, text)         #Encrypts the text message using shift value
print('The encrypted text is:', encrypted)
#print()

#==================below is to calculate prob of encrypted text===================================

string = encrypted
string = string.replace(" ", "")
n = 3
temp = []
out = [(string[i:i+n]) for i in range(len(string)+1- n)]
temp = out
#print("The encrypted text is split as trigram: ",temp)

prob_list_3 = []
for i in range(len(temp)):
    prob_3 = dict_prob_3.get(temp[i])
    prob_list_3 = prob_3
    #print(prob_list)
    prob_max_3 = np.max(prob_list_3)
    
#print("the candidate with max prob is '{}' and the candidate is '{}' ".format(prob_max_3, temp[i]))
#print()

add = 0
for i in range(len(temp)):
    res = float(dict_prob_3.get(temp[i]))
    add = res+add 
    
#print("The total prob of encrypted text is: ",add)
print()
  
##### Need to get the last element from add and print in output ??????????????##############
#######################################################################################################
    
def decrypt(n, encrypted):                 # Function used for decryption to get back plain text
    result = ''

    for l in encrypted:
        try:
            i = (alphabets.index(l) - shift) % 26
            result += alphabets[i]
        except ValueError:
            result += l

    return result    

decrypted = decrypt(shift, encrypted)    #Decrypts the encrypted message to get back plain text

print('The text decrypted from cipher text is:', decrypted)
#print()
#==================below is to calculate prob of decrypted text===================================

string1_list = []
string1 = decrypted

string1 = string1.split()
#print(string1)
#string1 = string1.replace(" ", "")
#string1 = string1.split()
string1_list = string1
print("The candidates of decrypted text are: ",string1_list)
#print()
#print(len(string1_list[1]))
#add_list_dec_prob = []

n = 3
out1_add = []

for x in range(len(string1_list)):
    #print(len(string1_list))    
    out1 = [(string1_list[x][i:i+n]) for i in range(len(string1_list[x])+1 -n)]
    #print("Candidates split as bigram for prob calculation: ",out1)
    res1 = [dict_prob_3.get(out1[i]) for i in range(len(out1))]
    #print(res1)
    res2 = np.sum(res1)
    #print(res2)
    out1_add = np.append(out1_add,res2)

out1_sum_list = []
out1_sum = np.sum(out1_add)
out1_sum_list = out1_sum    
#print(out1_sum_list)

dictionary = dict(zip(string1_list, out1_add))   
print()
print("The candidate and prob values are: ",dictionary) 
print()

maximum = max(dictionary, key=dictionary.get)
print("the candidate with max prob is '{}' and the candidate is '{}' ".format(dictionary[maximum], maximum))   
 
###################### Brute force attack ###################################################
    
print()
print("The brute force attack tells that the text was encrypted at key: ",shift)  
print()

for shift in range(len(alphabets)):    
    brute_force = ' '
    for symbol in encrypted:           
        if symbol in alphabets:
            num = alphabets.find(symbol)    
            num = num - shift                 
            if num < 0:
                num = num + len(alphabets)
            brute_force = brute_force + alphabets[num]
        else:
                brute_force = brute_force + symbol
                
    print("<Brute force attack for Shift> #%s: is %s"%(shift,brute_force))
          
    for i in range(len(brute_force)):
        bf_string_3 = brute_force
        bf_string_3 = bf_string_3.replace(" ", "")
        n = 3
        bf_temp_3 = []
        bf_out_3 = [(bf_string_3[i:i+n]) for i in range(len(bf_string_3)+1- n)]
        bf_temp_3 = bf_out_3
        
    #print("The decrypted text is split as bigram: ",bf_temp)
    #print()

    add = 0
    for i in range(len(bf_temp_3)):
         #res = float(dict_prob.get(temp[i]))
         res = dict_prob_3.get(bf_temp_3[i])
         add = res+add 
         
       
    #print("The total prob of open text candidate is: ",add)   
    #print()
    
print()
print("The total probability of open text candidate is %s  "%out1_sum_list)  
print()    
        #print(brute_force)