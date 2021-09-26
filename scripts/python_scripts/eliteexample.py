import random
import math


#1)Create a class diagram for the game

#2)playtest, looking for bugs in the program and fix them. 

#3)make other players ships repair when able/needed

#4)create a new solid or liquid product and fully integrate into the existing planets and ships

#5) make it so non-player ships pick up/drop off cargo, especially when low on anything

#6) Create a "colonists" resource, representing the population of a planet

#7) Colonists should be free to buy, and the 'sell' price should be inversely related to the population of a planet and not too high.

#8)Create a link between the population of a planet and amount of each product produced.

#9)Add in crew amount for a ship, which eat food,die in attacks etc.


class Thing:
    def __init__(self,name,coords):
        self.name=name #string
        self.coords=coords #list

    def distance(self,other):
        return math.ceil(((self.coords[0]-other.coords[0])**2+(self.coords[1]-other.coords[1])**2)**0.5)

class Product:
    all_products=list()
    product_names=list() #these are class attributes 
    def __init__(self,name,form):
        self.name=name
        self.form=form #solid,liquid
        Product.all_products.append(self)
        Product.product_names.append(self.name)


    

class Ship(Thing):
    
    def __init__(self,name,location,pcapacities,maxdamage,weaponstrength,faction,fuel_eff):
        self.fuel_eff=fuel_eff
        self.coords=location.coords
        self.name=name
        self.faction=faction
        self.pcapacities=pcapacities
        self.maxdamage=maxdamage
        self.damage=0
        self.weaponstrength=weaponstrength
        self.pamounts=dict()
        for k in Product.product_names:
            self.pamounts[k]=0
        self.pamounts["fuel"]=self.pcapacities["liquid"]
        Game.all_ships.append(self)

    def __str__(self):
        s=str()
        s+="-"*10+"ship:"+self.name+"-"*10+"\n"
        s+="weapon strength:"+str(self.weaponstrength)+"\n"
        s+="damage:"+str(self.damage)+"  ("+str(self.maxdamage)+") \n Capacities:\n"
        for k in self.pcapacities:
            s+=k+":"+str(self.pcapacities[k])+"\n"
        s+="amounts:\n"
        for k in self.pamounts:
            s+=k+":"+str(self.pamounts[k])
        return s

    def move(self,planet):
        self.pamounts["fuel"]-=int(planet.distance(self)*self.fuel_eff) #make sure you understand what is happening here!
        self.coords=planet.coords

    def update(self):
        if self.faction!="player":
            if random.randint(0,1)==1:
                p=random.randint(0,len(Game.all_planets)-1)
                if Game.all_planets[p].distance(self)<self.pamounts["fuel"]:
                    self.move(Game.all_planets[p])
        self.coords=location.coords

    def attack(self,other):
        strength= random.randint(self.strength)
        print("a barrage hits ",other.name," causing ",strength," damage")
        other.damage+=strength

    def combat(self,other):
        print("you are attacked by ",other.name)
        while(True):
            self.attack(other)
            if self.damage>self.maxdamage:
                game.lost=True
                break

            other.attack(self)
            if other.damage>self.maxdamage:
                break
            print(self.name," damage:",self.damage," (",self.maxdamage,")")
            print(other.name," damage:",other.damage," (",other.maxdamage,")")
            response=input("escape y/n?")
            if escape=="y":
                break
        
        


    
        

class Planet(Thing):
    def __init__(self,name,coords,pcosts,pprod):
        Thing.__init__(self,name,coords)
        self.pprod=pprod #dic:amount of each product produced
        self.pcosts=pcosts #dict amount of each product produced
        self.pamounts=dict()
        for k in pprod:
            self.pamounts[k]=pprod[k]*10
        Game.all_planets.append(self)
        
    def __str__(self):
        s=str()
        s+="-"*10+"planet: "+self.name+"-"*10+"\n"
        s+="coords:"+str(self.coords)+"\n"
        s+="PRODUCT COSTS: \n"
        for k in self.pcosts:
            s+=k+":"+str(self.pcosts[k])+"\n"
        s+="PRODUCT AMOUNTS: \n"
        for k in self.pamounts:
            s+=k+":"+str(self.pamounts[k])+"\n"

        return s

    def update(self):
        for k in self.pamounts:
            self.pamounts[k]+=self.pprod[k]
        for k in self.pcosts:
            self.pcosts[k]+=random.randint(-1,1)
        
            
        


class Game:
    all_planets=list()
    all_ships=list()
    
    
    def __init__(self):
        Product("iron","solid")
        Product("fuel","liquid")
        Product("food","solid")
        Planet("Earth",[0,0],{"iron":100,"fuel":100,"food":100},{"iron":2,"fuel":2,"food":2})
        Planet("IroniaIII",[36,42],{"iron":30,"fuel":60,"food":90},{"iron":8,"fuel":2,"food":1})
        Planet("Foodtopia",[0,10],{"iron":100,"fuel":30,"food":10},{"iron":1,"fuel":2,"food":8})
        Planet("oilworldIV",[0,50],{"iron":200,"fuel":5,"food":100},{"iron":0,"fuel":10,"food":1})
        Ship("rusty merchant ship",Game.all_planets[0],{"solid":40,"liquid":40},40,4,"player",0.2)
        Ship("naval vessel",Game.all_planets[1],{"solid":10,"liquid":50},60,20,"navy",0.1)
        Ship("pirates",Game.all_planets[2],{"solid":40,"liquid":30},50,10,"pirates",0.3)

        self.location=Game.all_planets[0] #players current location
        self.Ship=Game.all_ships[0] #players ship
        self.lost=False #game lost indicator
        self.gold=100
        self.overdraft=10000

    def lostcheck(self):
        if self.Ship.pamounts["food"]<0 or self.Ship.pamounts["fuel"]<0 or self.Ship.damage>self.Ship.maxdamage:
            print(self.Ship)
            print("you have lost the game")
            input()
            self.lost=True
        

    def get_player_input(self):
        print(self.Ship)
        print(self.location)
        print("-"*10+"options"+"-"*10)
        print("1: buy products")
        print("2: sell products")
        print("3: repair ship")
        print("4: travel to another planet")
        
        response=-1
        while(response not in range(5)):
            try:
                response=int(input("choose option: "))
            except:
                pass
        if response==1:
            self.buy(False)
        if response==2:
            self.buy(True)
        if response==3:
            self.repair()
        if response==4:
            self.travel()

    def travel(self):
        print("where do you want to travel to?")
        print("available fuel: ",self.Ship.pamounts["fuel"])
        for p in Game.all_planets:
            if p!=self.location:
                s=str(Game.all_planets.index(p))+":"
                s+=p.name
                s+=" fuel needed "+str(int(p.distance(self.location)*self.Ship.fuel_eff))
                print(s)
        response=int(input("input number of planet to travel to: "))
        
        
        planet=Game.all_planets[response]
        if str(int(planet.distance(self.location)*self.Ship.fuel_eff)):
            self.Ship.move(planet)
            self.location=planet

            

    def repair(self):
        print("\n Damage on ship is:"+str(self.Ship.damage)+"("+str(self.Ship.maxdamage)+") \n")
        print("iron available:"+str(self.Ship.pamounts["iron"]))
        response=int(input("how much to repair? "))
        self.Ship.pamounts["iron"]-=response
        self.Ship.damage-=response

    def debt(self):
        if self.gold<-self.overdraft:
            print("Gold remaining: $",self.gold)
            if random.randint(1,100)<95:
                print("\n\n\n\n\n\nWARNING: you are over your overdraft limit, galacti-bank officials may arrest you\n")
            else:
                print("\n\n\n\n\nWARNING: Galactibank officials are demanding repayment of debts")
                print("as you cannot repay you will be incarcerated in space-jail\n")
                self.lost=True

        elif self.gold<0:
            print("\n\n\n\n\nWARNING: you are in debt with the galacti-bank")
            print("all debt will accrue interest of 1%")
            print("debts of more than your overdraft limit of: 10000 risk arrest by bank enforcers\n")
            
          

            
    def buy(self,sell):
        #set sell to True if selling
        print("\n\n ----------BUYING-------\n")
        print("GOLD:\n $"+str(self.gold))
        for p in Product.all_products:
            form=p.form
            space=self.Ship.pcapacities[form]
            for q in Product.all_products:
                if q.form==form:
                    space-=self.Ship.pamounts[q.name]
            print(p.name+" @ $"+str(self.location.pcosts[p.name])+" ("+str(self.location.pamounts[p.name])+" available)  "+str(space)+" free in hold")
            if sell==True:
                do=" sell:"
            else:
                do=" buy:"
            response=int(input("enter amount to"+do+": "))
            if sell==False:
                
               
                self.Ship.pamounts[p.name]+=response
                self.location.pamounts[p.name]-=response
                self.gold-=response*self.location.pcosts[p.name]
    
                    
            else:
                self.Ship.pamounts[p.name]-=response
                self.location.pamounts[p.name]+=response
                self.gold+=response*self.location.pcosts[p.name]
            
            print("GOLD:\n $"+str(self.gold))

        
                
        

    def play(self):
        while(self.lost==False):
            self.get_player_input()
            self.debt()
            self.lostcheck()
        print("\n\n\n\n-------GAME OVER--------\n\n\n\n")
        
    
        
        



        
Game().play()

    
        
