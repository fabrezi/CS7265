#All comments are in one section to help in ease of reading:
# 1. the data is loaded as " car.train" + panda is used as framework
# 2. We need to know find the root node through the train data. + we will find gini
# 3. GINI_INDEX():
# 4. First give each column a name to help in counting: for example:
#                       column1 = buying
#                       column2 = maint
#                       column3 = door
#                       column4 = persons, col5= lug_boot, col6= safety, col7= class
# 5. Now we need to build a frequency table in which each category attribute is saved or counted relative
#    to the class column. For example:
#                     freq.table
#buying_frequency table:
#             | acc | unacc | sum
#         low | 80  | 10    | 90
#         med | 20  | 0     | 20
#        high | 50  | 50    | 100
#       vhigh | 10  | 20    | 30
#                             240 #total sum
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
#    nodes on the second level....(I havent figured how to go further)....
# 8. I don't know how to go from the root node to leaf node.. hunts algorithm.
###########################################################################################
import pandas as pd


data = pd.read_csv("C:\\Users\\farid\\Desktop\\CS7265\\car.training.csv", header=None)
data.rename(columns={0: 'buying', 1: 'maint', 2: 'doors', 3: 'persons', 4: 'lug_boot', 5: 'safety', 6: 'class'}, inplace=True)
data.to_csv('car.training', index=False)
data.info
print(data)



