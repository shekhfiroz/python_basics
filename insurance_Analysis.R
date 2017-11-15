#data_output=read.csv(file.choose("E:\\insurance_data\\details.csv"),header = TRUE)
#View(data_output)
getwd()
data_out=read.csv(file.choose())
View(data_out)
names(data_out)           
relevent_cloumn=data_out[,c("V_COMPANY_BRANCH","V_POLICY_NO","N_AGE_ENTRY")]
relevent_cloumn
plot(relevent_cloumn)


library(ggplot2)
company_branch=ggplot(data_out,aes(x=N_AGE_ENTRY))
company_branch
company_branch<-company_branch+geom_histogram(aes(fill=N_AGE_ENTRY),color="red")

company_branch



library(ggplot2)
company_branch=ggplot(data_out,aes(x=N_AGE_ENTRY))
company_branch
company_branch<-company_branch+geom_bar(aes(fill=N_AGE_ENTRY),color="red")
company_branch


company_branch<-ggplot(values,aes(x=N_AGE_ENTRY))
company_branch
company_branch<-company_branch+geom_bar(aes(fill=N_AGE_ENTRY),color="red",bins=70,alpha=0.5)
company_branch

