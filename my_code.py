# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  Jonah explained some of the concepts to me and also Megan. 

   # Do not change function name!
    # User code goes here
gcf=0
def find_gcf(x,y):
    for i in range(1,y+1):
        if x % (i) == 0 and y % (i) == 0:
            gcf = i
    return(gcf)

if __name__ == '__main__':

    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    print(find_gcf(x,y))


    
    # Test your code with this first
    # Change the argument to try different values
    # After you are satisfied with your results, use input() to prompt the user for two values:
    #x = int(input("Enter a number: "))
    #y = int(input("Enter another number: "))

