set.seed(41)
id = 1:100
roll = sample(1:6, 100, replace =T)
flip= sample(c("H","T","E"), prob=c(0.45,0.45,0.1), 100, replace =T)
data = data.frame(id,roll,flip)
print(table(data$flip))

maxcount = 0
maxitem = "O"
count =0
preitem = "O"
for (index in 1:nrow(data["flip"])){
    if (preitem == data$flip[index]){
        count = count +1
    }
    else{
        if(count>maxcount){
            maxitem = preitem
            maxcount = count
        }
        preitem = data$flip[index]
        count = 0
        
    
    }
    
}
print(maxcount)
print(maxitem)