
##########################################################
##########################################################
####################### Exercise 1 #######################
##########################################################
##########################################################
# Compute the number of feet corresponding to a number of miles.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
miles = 13


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
#miles = 57


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
#miles = 82.67


###################################################
# Miles to feet conversion formula
# Student should enter formula on the next line.

feet = miles * 5280

###################################################
# Test output
# Student should not change this code.

print str(miles) + " miles equals " + str(feet) + " feet."


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#13 miles equals 68640 feet.

# Test 2 output:
#57 miles equals 300960 feet.

# Test 3 output:
#82.67 miles equals 436497.6 feet.

##########################################################
##########################################################
####################### Exercise 2 #######################
##########################################################
##########################################################
# Compute the number of seconds in a given number of hours, minutes, and seconds.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
hours = 7
minutes = 21
seconds = 37


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
#hours = 10
#minutes = 1
#seconds = 7


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
#hours = 1
#minutes = 0
#seconds = 1


###################################################
# Hours, minutes, and seconds to seconds conversion formula
# Student should enter formula on the next line.

total_seconds = hours * 60 * 60 + minutes * 60 + seconds

###################################################
# Test output
# Student should not change this code.

print str(hours) + " hours, " + str(minutes) + " minutes, and",
print str(seconds) + " seconds totals to " + str(total_seconds) + " seconds."


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
# Test 1 output:
#7 hours, 21 minutes, and 37 seconds totals to 26497 seconds.

# Test 2 output:
#10 hours, 1 minutes, and 7 seconds totals to 36067 seconds.

# Test 3 output:
#1 hours, 0 minutes, and 1 seconds totals to 3601 seconds.