#----------------------------------------------------------------------------------------
# FUNCTION 01 - ShoppingList
#   Action: Creates a list from a user's repeated input. List ends when nothing is entered.
#   Input: Text strings from user
#   Output: List of strings

def ShoppingList():
    list1=[]
    while list1>0:
        element=raw_input("Please enter what you need from the grocery store by typing the name of a prodoct and pressing enter. Entering a blank will end your list.")
        if element=="": #ends list input when nothing is entered
            break
        list1.append(element) #creates list from all user input
    return list1
#-------------------------------------------------------------
# FUNCTION 02 - SortShoppingList
#   Action: Sorts the user's list in alphabetical order using a bubble sort
#   Input: A list
#   Output: A sorted list in alphabetical order
def SortShoppingList(ShoppingList):
    for j in range (len(ShoppingList)-1):
        for i in range (len(ShoppingList)-1-j): #add -j to optimize BubbleSort
            if ShoppingList[i+1]<ShoppingList[i]:
                swap = ShoppingList[i]
                ShoppingList[i] = ShoppingList[i+1]
                ShoppingList[i+1]=swap
    return ShoppingList
#-------------------------------------------------------------
# FUNCTION 03 - StripShoppingList
#   Action: Remove duplicate elements from a user's list
#   Input: A sorted list
#   Output: A new list stripped of duplicates
def StripShoppingList(SortedList):
    L1=SortedList
    L2=[]
    for j in range(len(L1)):
        if L1[j] not in L2: 
            L2.append(L1[j]) #creates a new list with no duplicates
    return L2
            
#-------------------------------------------------------------
# FUNCTION 04 - ReportShoppingList
#   Action: Reports the original and stripped user lists, and prints final spelled count of duplicates.
#   Input: Two lists - one sorted, one stripped of duplicates
#   Output: A stripped list, a sorted list, and a the spelled numerical amount of duplicates for each element in the sorted list.
def ReportShoppingList(SortedList,StrippedList):
    sentence=""
    print
    print "Original list:"
    print SortedList
    print
    print "Stripped list:"
    print StrippedList
    print
    print "Number of occurrences for each item in original list:"
    L3=["zero","one","two","three","four","five"] #creates a list with spelled numbers
    for j in range(len(StrippedList)): #must use stripped list so it only checks for each element once
        print L3[SortedList.count(StrippedList[j])], StrippedList[j] #reports alphabetical number of elements for each unique element
    return SortedList
                   
#-------------------------------------------------------------------------------------------------

#links functions together to produce result

def main():
    my_list=ShoppingList()
    
    list_1=my_list
    list_2=SortShoppingList(list_1)
    list_3=StripShoppingList(list_2)
    list_4=ReportShoppingList(list_2,list_3) 
  
main()
