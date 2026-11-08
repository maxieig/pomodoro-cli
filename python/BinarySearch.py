def binarySearch(itemList, item):
    lowerPos=0
    upperPos=len(itemList)-1
    found=False
    while lowerPos<=upperPos and not found:
        midPos=(lowerPos+upperPos)//2
        if itemList[midPos]==item:
            found=True
        else:
            if item<itemList[midPos]:
                upperPos=midPos-1
            else:
                lowerPos=midPos+1
    return found
itemList=[1,2,3,5,8]
item=int(input("Please enter the item to search for: "))
print(binarySearch(itemList, item))