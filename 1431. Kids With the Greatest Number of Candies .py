def KidsWiththeGreatestNumberofCandies(candies,extraCandies):
    maxcandie = max(candies)
    array = []
    for i in candies:
        extaaarray = i + extraCandies
        array.append(maxcandie==extaaarray or maxcandie<extaaarray)
    return array
candies = [2,3,5,1,3]
reults = KidsWiththeGreatestNumberofCandies(candies,3)
print(reults)
