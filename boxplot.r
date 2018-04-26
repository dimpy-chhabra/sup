data <- read.csv("data_news_Trump.csv")

data2 <- read.csv("data_news_hillary.csv")

	

	a <- data$source
	b <- data$desc_subjectivity
	c <- data$desc_polarity
	d <- data$titl_subjectivity
	e <- data$titl_polarity

	a2 <- data2$source
	c2 <- data2$desc_polarity

scatter.smooth(x=c, y=a, main="Polarity Vs. News Channel: Trump")  # scatterplot(Bivariate)
scatter.smooth(x=c2, y=a2, main="Polarity Vs. News Channel: Hillary")  # scatterplot(Bivariate)

par(mfrow=c(1, 2))  # divide graph area in 2 columns

boxplot(c, main="Trump's News Polarity", sub=paste("Outlier rows: ", boxplot.stats(c)$out))  # box plot for 'speed' (Univariate)

boxplot(c2, main="Hillary's News Polarity", sub=paste("Outlier rows: ", boxplot.stats(d)$out))  # box plot for 'distance' (Univariate)

#linearMod <- lm(dist ~ speed, data=data)  # build linear regression model on full data

#print(linearMod)