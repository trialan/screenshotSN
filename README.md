# screenshotSN

Take screenshots of your computer, and get GPT-4o to analyse the content of the
screen. The idea is that if we ran this every minute, I could have a precise
read of my computer activity, and potentially use this as data for a "genuine
connection" social network that would share with my friends stuff like "Today
Thomas listened to these podcasts, watched this movie, and did research on
asteroid mining."

## Cost analysis
10 requests with `detail="auto"` led to 10152 input tokens and 2624 output tokens, this means it
costs 0.9 cents per screenshot analysed. This means it costs about $4/day to do
this, which is currently too cost prohibitive. Once costs are down by a factor
of 10x this would be a viable idea assuming you can charge $20/month. Setting
`detail="low"` leads to estimated cost of 0.5 cents/request, i.e. $2.5/day at
8hrs of daily usage, however this setting renders it useless as it gets the
answers wrong.

