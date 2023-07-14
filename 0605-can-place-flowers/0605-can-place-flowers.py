class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                count += 1
                flowerbed[0] = 1
            
        for i,v in enumerate(flowerbed):
            if v == 1:
                continue
                
            if i == 0:
                if flowerbed[i+1] == 0:
                    count += 1
                    flowerbed[i] = 1
                continue
                
            if i == len(flowerbed)-1:
                if flowerbed[i-1] == 0:
                    count += 1
                    flowerbed[i] = 1
                continue
                
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                count += 1
                flowerbed[i] = 1
            
        return count >= n