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
# 8. I don't know how to go from the root node to leaf node.. hunts algorithm.
###########################################################################################
import pandas as pd


data = pd.read_csv("C:\\Users\\farid\\Desktop\\CS7265\\car.training.csv", header=None)
data.rename(columns={0: 'buying', 1: 'maint', 2: 'doors', 3: 'persons', 4: 'lug_boot', 5: 'safety', 6: 'class'}, inplace=True)
data.to_csv('car.training', index=False)
#print(data)

print(                                                                         )



# ft stands for frequency table
buy_ft = data.groupby(["buying", "class"]).size()
#data.assign(sum) #we need to find a way to retirive the values form the
#output.
data.rename(columns={2: 'sum'}, inplace=True)
print(buy_ft)
#calculate gini index of each attribute of buy:
class_sum = 400 ; total_sum = 800 #these sum represent the total of acc and unacc column total and total sum. it is the same for all features
#gini (buy_high) = 1- (buy_high_acc/400)^2 - (buy_high_unacc/400)^2
#gini (buy_low) = 1 - (buy_low_acc/400)^2....
#gini (buy_med) = 1 - ....
#gini (buy_vhigh) = 1- ....
buy_low_acc = buy_ft.loc['low', 'acc']
print(buy_low_acc)
#buy_low_unacc = buy_ft.loc['low', 'unacc']
#print(buy_low_unacc)

#gini sum(buying) = (gini of buy_high * (buy_high_acc + buy_high_unacc)/800) + (gini of buy_vhigh * (buy_vhigh....)

maint_ft = data.groupby(["maint", "class"]).size()
print(maint_ft)
#gini of

doors_ft = data.groupby(["doors", "class"]).size()
print(doors_ft)


persons_ft = data.groupby(["persons", "class"]).size()
print(persons_ft)


lug_boot_ft = data.groupby(["lug_boot" , "class"]).size()
print(lug_boot_ft)


safety_ft = data.groupby(["safety", "class"]).size()
print(safety_ft)

