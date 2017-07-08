df<-data.frame(task=c("right","left","up","down","front","back"),measure=c("m1","m2","m3","m4","m5","m6"))

df


df$task<-factor(df$task,levels = c("up","down","left","right","front","back"))

df


library(raster)

ls_url<-"https://github.com/tuyenhavan/Landsat-Data/blob/LS7/Landsat.rar"

temp<-tempfile()

download.file(ls_url,temp)

unzip(temp,"tif$")

myls<-stack("tif$")