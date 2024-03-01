def top_n (items, n):
    """Return the top n items in an array, in desc order.
    
    Args:
        items (array): list or array-like object
        n (init): num of items to return
        
    Return:
        array: top n, items in desc order
        
    Egs:
        >>> top_n ([8,3,2,7,4], 3)
        [8,7,3]
    """
    
    for i in range(n): #keep sorting until we have the top n items
        for j in range(len(items)-1-i):
            
            if items[j] > items[j+1]: #if this is it
                items[j], items[j+1] = items[j+1], items[j] #swaps the two
                
    #Get last two items
    top_n = items[-n:]
    
    #Return in desc order
    return top_n[::-1]