#All comments are in one section to help in ease of reading:
# 1. the data is loaded as " car.train" + panda is used as framework
# 2. We need to know find the root node through the train data. + we will find gini
# 3. GINI_INDEX():
# 4. First give each column a name to help in counting: for example:
#                       column1 = buying
#                       column2 = maint
#                       column3 = door
#                       column4 = persons, col5= lug_boot, col6= safety, col7= class
# features: buying (attributes: low, med, high, vhigh)
#           maint (attributes: low, med, high, vhigh)
#           doors: (2, 3, 4, 5more)
#           persons: (2,4, more)
#           lug_boot: (small, med, high)
#           safety: (low, med, high)
#           class: (acc, unacc)
# 5. Now we need to build a frequency table in which each category attribute is saved or counted relative
#    to the class column. For example:
#                     freq.table: parts = features(attributes) | class(acc or unacc)
#buying_frequency table:
#             | acc | unacc | sum
#         low | 80  | 10    | 90
#         med | 20  | 0     | 20
#        high | 50  | 50    | 100
#       vhigh | 10  | 20    | 30
#                             800 #total sum
# now we find the gini of buying(low): 1 - (80/90)^2 - (10/90)^2 = A
#                 gini of buying(med): 1 - (20/20)^2 - (0/20)^2  = B
#                 gini of buying(high): 1- (50/100).....         = C
#                 gini of buying(vhigh): 1 - (10/30)^2....       = D
#now we find the gini sum of buying:
# gini_sum(buying): [(90/240)*A] + [(20/240)*B] + [(100/240)*C} + [(20/240)*D]
# recursively we will make frequency table for each feature and find gini_sum
# 6. Select the lowest gini_sum as the root node
#
# 7. Then we need to continue to recursively find the gin_sum of the parents
#    nodes on the second level....(I haven't figured how to go further)....
# 8. I don't know how to go from the root node to leaf node..
###########################################################################################
import pandas as pd


data = pd.read_csv("C:\\Users\\farid\\Desktop\\CS7265\\car.training.csv", header=None)
data.rename(columns={0: 'buying', 1: 'maint', 2: 'doors', 3: 'persons', 4: 'lug_boot', 5: 'safety', 6: 'class'}, inplace=True)
data.to_csv('car.training', index=False)
print(data)

print('\n')


class_sum = 400
total_sum = 800 #these sum represent the total of acc and unacc column total and total sum. it is the same for all features
# ft stands for frequency table
buy_ft = data.groupby(["buying", "class"]).size().reset_index(name='sum')
print(buy_ft)
#gini index:
sum0 = buy_ft.iloc[0 , 2]
sum1 = buy_ft.iloc[1 , 2]
sum2 = buy_ft.iloc[4 , 2]
sum3 = buy_ft.iloc[5 , 2]
sum4 = buy_ft.iloc[2 , 2]
sum5 = 0
sum6 = buy_ft.iloc[3 , 2]
sum7 = 0
gini_buy_high = 1 - (sum0/class_sum)**2 - (sum1/class_sum)**2
gini_buy_vhigh = 1 - (sum2/class_sum)**2 - (sum3/class_sum)**2
gini_buy_low = 1 - (sum4/class_sum)**2 - (sum5/class_sum)**2
gini_buy_med = 1- (sum6/class_sum)**2 - (sum7/class_sum)**2
add1 = sum0 + sum1
add2 = sum4 + sum5
add3 = sum6 + sum7
add4 =  sum2 + sum3
ginisum_buy = [(gini_buy_high * (add1/total_sum)) + (gini_buy_low * (add2/total_sum)) + (gini_buy_med * (add3/total_sum)) + (gini_buy_vhigh * (add4/total_sum))]
print("gini of buy node:" , ginisum_buy)
print('\n')



maint_ft = data.groupby(["maint", "class"]).size().reset_index(name='sum')
print(maint_ft)
#gini index
sum0 = maint_ft.iloc[0 , 2]
sum1 = maint_ft.iloc[1 , 2]
sum2 = maint_ft.iloc[6 , 2]
sum3 = maint_ft.iloc[7 , 2]
sum4 = maint_ft.iloc[2 , 2]
sum5 = maint_ft.iloc[3 , 2]
sum6 = maint_ft.iloc[4 , 2]
sum7 = maint_ft.iloc[5 , 2]
gini_m_high = 1 - (sum0/class_sum)**2 - (sum1/class_sum)**2
gini_m_vhigh = 1 - (sum2/class_sum)**2 - (sum3/class_sum)**2
gini_m_low = 1 - (sum4/class_sum)**2 - (sum5/class_sum)**2
gini_m_med = 1- (sum6/class_sum)**2 - (sum7/class_sum)**2
add11 = sum0 + sum1
add21 = sum4 + sum5
add31 = sum6 + sum7
add41 =  sum2 + sum3
ginisum_m = [(gini_m_high * (add11/total_sum)) + (gini_m_low * (add21/total_sum)) + (gini_m_med * (add31/total_sum)) + (gini_m_vhigh * (add41/total_sum))]
print("gini of maint node:" , ginisum_m)
print('\n')

doors_ft = data.groupby(["doors", "class"]).size().reset_index(name='sum')
print(doors_ft)
sum0 = maint_ft.iloc[4 , 2]
sum1 = maint_ft.iloc[5 , 2]
sum2 = maint_ft.iloc[6 , 2]
sum3 = maint_ft.iloc[7 , 2]
sum4 = maint_ft.iloc[0 , 2]
sum5 = maint_ft.iloc[1 , 2]
sum6 = maint_ft.iloc[2 , 2]
sum7 = maint_ft.iloc[3 , 2]
gini_dhigh = 1 - (sum0/class_sum)**2 - (sum1/class_sum)**2 #4
gini_dvhigh = 1 - (sum2/class_sum)**2 - (sum3/class_sum)**2 #5more
gini_dlow = 1 - (sum4/class_sum)**2 - (sum5/class_sum)**2 #2
gini_dmed = 1- (sum6/class_sum)**2 - (sum7/class_sum)**2 #3
add12 = sum0 + sum1
add22 = sum4 + sum5
add32 = sum6 + sum7
add42 =  sum2 + sum3
ginisum_d = [(gini_dhigh * (add12/total_sum)) + (gini_dlow * (add22/total_sum)) + (gini_dmed * (add32/total_sum)) + (gini_dvhigh * (add42/total_sum))]
print("gini of doors node:" , ginisum_d)
print('\n')

p_ft = data.groupby(["persons", "class"]).size().reset_index(name='sum')
print(p_ft)
sum0 = 0
sum1 = p_ft.iloc[0 , 2]
sum2 = p_ft.iloc[1 , 2]
sum3 = p_ft.iloc[2 , 2]
sum4 = p_ft.iloc[3 , 2]
sum5 = p_ft.iloc[4 , 2]
gini_2 = 1 - (sum0/class_sum)**2 - (sum1/class_sum)**2
gini_4 = 1 - (sum2/class_sum)**2 - (sum3/class_sum)**2
gini_mo = 1 - (sum4/class_sum)**2 - (sum5/class_sum)**2
add13 = sum0 + sum1
add23 = sum4 + sum5
add33 = sum6 + sum7
ginisum_p = [(gini_2 * (add13/total_sum)) + (gini_4 * (add23/total_sum)) + (gini_mo * (add33/total_sum)) + (gini_dvhigh * (add42/total_sum))]
print("gini of persons node:" , ginisum_p)
print('\n')

l_ft = data.groupby(["lug_boot" , "class"]).size().reset_index(name='sum')
print(l_ft)
sum0 = l_ft.iloc[0 , 2]
sum1 = l_ft.iloc[1 , 2]
sum2 = l_ft.iloc[2 , 2]
sum3 = l_ft.iloc[3 , 2]
sum4 = l_ft.iloc[4 , 2]
sum5 = l_ft.iloc[5 , 2]
gini_big = 1 - (sum0/class_sum)**2 - (sum1/class_sum)**2
gini_med = 1 - (sum2/class_sum)**2 - (sum3/class_sum)**2
gini_small = 1 - (sum4/class_sum)**2 - (sum5/class_sum)**2
add14 = sum0 + sum1
add24 = sum4 + sum5
add34 = sum6 + sum7
ginisum_l = [(gini_big * (add14/total_sum)) + (gini_med * (add24/total_sum)) + (gini_small * (add34/total_sum))]
print("gini of lug_boot node:" , ginisum_l)
print('\n')

s_ft = data.groupby(["safety", "class"]).size().reset_index(name='sum')
print(s_ft)
sum0 = s_ft.iloc[0 , 2]
sum1 = s_ft.iloc[1 , 2]
sum2 = s_ft.iloc[3 , 2]
sum3 = s_ft.iloc[4 , 2]
sum4 = s_ft.iloc[2 , 2]
sum5 = 0
gini_sh = 1 - (sum0/class_sum)**2 - (sum1/class_sum)**2
gini_smed = 1 - (sum2/class_sum)**2 - (sum3/class_sum)**2
gini_ssmall = 1 - (sum4/class_sum)**2 - (sum5/class_sum)**2
add15 = sum0 + sum1
add25 = sum4 + sum5
add35 = sum6 + sum7
ginisum_s = [(gini_sh * (add15/total_sum)) + (gini_smed * (add25/total_sum)) + (gini_ssmall * (add35/total_sum))]
print("gini of safety node:" , ginisum_s)
print('\n')


