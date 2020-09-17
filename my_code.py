# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  Jonah explained some of the concepts to me. 

   # Do not change function name!
    # User code goes here
def find_gcf(x,y):
    gcf=0
    for i in range(1,y):
        if x % (i + 1) == 0 and y % (i + 1) == 0:
            gcf = i + 1 
    return(gcf)

    #if __name__ == '__main__':

x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
print(find_gcf(x,y))


    
    # Test your code with this first
    # Change the argument to try different values
    # After you are satisfied with your results, use input() to prompt the user for two values:
    #x = int(input("Enter a number: "))
    #y = int(input("Enter another number: "))

