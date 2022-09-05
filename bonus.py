# Generate Random data points that simulate new universal screener scale scores - in this case all 4th graders at an elementary school as an example

import random
#Generate 150 random numbers between 100 and 700
randomlist = random.sample(range(500, 700), 150)

import statistics as stats

variance = stats.pvariance(randomlist)
deviation = stats.pstdev(randomlist)

print('Scores = ', randomlist)

print('Variance of Scores: ', (variance))
print('Standard Deviation of Scores: ', (deviation))
print('My name is Kim Leach. This is the Variance and Standard Deviation of 150 4th grade assesment scale scores that were randomly generated to simulate students who tested as Advanced.')