#View(ChickWeight)

#for (n in 1:nrow(ChickWeight)){
#    if(ChickWeight$weight[n]>maxweight){
#            maxweight <- ChickWeight$weight[n]
#    }
#    if (ChickWeight$Time[n]==21){
#        print(maxweight)
#        maxweight <- 0
#    }
#}
getIndexes <- function(data, diet){
    startofdata <- -1
    for (index in 1:nrow(data)){
        if (diet == data$Diet[index] && startofdata==-1){
            startofdata <- index
        }
        if(diet != data$Diet[index] && startofdata!= -1){
            return (c(startofdata, index))
        }
    }
    return(c(startofdata, index))
}
# BTW i'm so sorry, i couldnt get the boxplot to display a vector of vectors through append(vectorofvectors, ChickWeight$weight[start:end]) 
#where diet in getIndexes are iterated 1:4
splice <- getIndexes(ChickWeight, 1)
start <- splice[1]
end <- splice[2]
A<-ChickWeight$weight[start:end]
splice <- getIndexes(ChickWeight, 2)
start <- splice[1]
end <- splice[2]
B<-ChickWeight$weight[start:end]
splice <- getIndexes(ChickWeight, 3)
start <- splice[1]
end <- splice[2]
C<-ChickWeight$weight[start:end]
splice <- getIndexes(ChickWeight, 4)
start <- splice[1]
end <- splice[2]
D<-ChickWeight$weight[start:end]
boxplot(A,B,C,D, names = c("Diet 1", "Diet 2", "Diet 3", "Diet 4"))

#print(tapply(ChickWeight$weight, ChickWeight$Diet, mean))