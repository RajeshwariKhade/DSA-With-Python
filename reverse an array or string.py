def reverse_an_array_or_String(Arr,Start,End):
    while Start < End :
        Arr[Start],Arr[End]=Arr[End],Arr[Start]
        Start +=1
        End -= 1
Arr = [1,2,3,4,5,6]
print(Arr)
reverse_an_array_or_String(Arr,0,5)
print("reverse An Array or String",Arr)