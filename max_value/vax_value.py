def max(array):
    length = len(array)
    for i in range(length-1):
        if ( array[i]> array[i+1]):
            temp = array[i]
            array[i]=array[i+1]
            array[i+1]=temp
    max_value = array[length-1]
    return max_value



def main():
    scores = [60,50,95,80,70]
    max_value = max(scores)
    print("max ",max_value)
if __name__ =='__main__':
    main()  
