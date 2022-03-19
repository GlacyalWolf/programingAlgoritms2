from easyinput import read


dicPlayers={}
for i in range(read(int)):
    
    name,punctuation=read(str,int)
    
    player={punctuation : name}

    dicPlayers.update(player)
    
orderPlayers=sorted(dicPlayers,reverse=True)

for i in range(len(orderPlayers)):
    if(i==0):
        print(f"Gold: {dicPlayers.get(orderPlayers[i])}")
    elif(i==1):
        print(f"Silver: {dicPlayers.get(orderPlayers[i])}")
    elif(i==2):
        print(f"Bronze: {dicPlayers.get(orderPlayers[i])}")
    else:
        print(f"{dicPlayers.get(orderPlayers[i])}")


