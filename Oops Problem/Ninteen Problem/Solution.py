class CricketPlayer:
    def __init__(self,cplayername,cplayedcountry,cplayerage,cpcountryfrom):
        self.cplayername=cplayername
        self.cplayedcountry=cplayedcountry
        self.cplayerage=cplayerage
        self.cpcountryfrom=cpcountryfrom


class Solution:
    def __init__(self,SetofPlayers):
        self.SetofPlayers=SetofPlayers

    def countPlayers(self,country):
        ct=0
        for obj in self.SetofPlayers:
            if obj.cpcountryfrom.lower()==country.lower():
                ct+=1
        return ct
    def getPlayerPlayedForMaxCountry(self):
        mx=0
        ans=""
        for obj in self.SetofPlayers:
            temp=len(obj.cplayedcountry)
            if temp>mx:
                mx=temp
                ans=obj.cplayername
        return ans        
                
if __name__=="__main__":
    n=int(input())
    playerlist=[] 
    for i in range(n):
        playerName = input()
        playedCountry = []
        for i in range(int(input())):
            temp = input()
            playedCountry.append(temp)
        playerAge = int(input())
        playerCountry = input()
        playerlist.append(CricketPlayer(playerName,playedCountry,playerAge,playerCountry))

    country=input()
    obj=Solution(playerlist)   
    o1=obj.countPlayers(country) 
    print(o1)
    o2=obj.getPlayerPlayedForMaxCountry()
    print(o2)
#################################################################################

# 3
# virat
# 5
# aus
# nze
# eng
# wi
# pak
# 35
# ind
# raina
# 3
# aus
# pak
# nze
# 34
# ind
# gayle
# 3
# aus
# ind
# pak
# 42
# wi
# ind
         