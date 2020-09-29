import re


regPat = re.compile(r'(\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b)(\'])(\s)+((\w)+-(\w)+-(\w)+-(\w)+)')
# this line of code will compile the regex pattern and save the
# output of the compilation to a regex pattern object called "regPat"
# that regex pattern object will do the following:
    # part 1
        # (\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b)
            # this pattern will look for an ip address and place it in a
            # numbered group (group(1))

    # part 2
        # (\'])
            # this pattern will look for the literal characters of ' & ]
            # the ' is escaped with the \ character because ' it is a regex
            # special character
            # when a match is made, the value is placed in a numbered
            # group (group(2))

    # part 3
        # (\s)
            # this pattern will look for the space characters 
            # when a match is made the value is placed in a numbered
            # group (group(3))

    # part 4
        # ((\w)+-(\w)+-(\w)+-(\w)+)
            # this pattern will match the following:
                # ((\w)+    any word charater that appears 1 time or more
                # -         a literal - character
                # the above patterns are repeated 3 times
                    # in conclusion the patten make a match when:
                        # if you see a word char that appears 1 or more times
                        # then it is followed by a - char
                        # then it is followed by a word char that appears 1
                        # or more times
                        # then it is followed by a - char
                        # then it is followed by a word char that appears 1
                        # or more times
                        # then it is followed by a - char
                        # then it is followed by a word char that appears 1
                        # or more times
                            # an example of a matched is:
                                # Host-Name-234-23
            # when a match is made the value is placed in numbered
            # group (group(4))

    # for the entire regex pattern to work the following MUST happen:
        # the results of part 1 must be imediately followed by the
        # results of part 2, which must be imediately followed by the
        # results of part 3, which must be imediately followed by the
        # results of part 4

     # for example:
        # for the line in the file raw_ip_address_hostname_mapping
        # that contains:
            # ['192.168.1.1']    Host-Name-320-139
        
        # the regex pattern will return:
            # group(1) = 192.168.1.1
            # group(2) = ']
            # group(3) = (space char)
            # group(4) = Host-Name-320-139

    # this is done to the first line in the file, after a complete
    # match of the entire regex pattern is found and the groups for
    # that line has been identified, the code goes to the next line
    # and so on and so on
    
    # if there is no match of the pattern on a line, the regex engine
    # stores a "none" value in the object and moves to the next line 

   


rawData = open('Phase 1 Stuff/regexToGet-IPAddressToHostnameMapping/raw_ip_address_hostname_mapping')
# this line of code will create a file object after openning the file
# raw_ip_address_hostname_mapping and save that file object to the
# variable "rawData"



rawDataContent = rawData.read()
# this line of code will use the "read" method of the file object to
# read the content of the file and save the value to the variable
# "rawDataContent"


finalDraftMO = regPat.finditer(rawDataContent)
# this line of code will use the finditer method from the regex
# pattern object called "regPat"

# that object is created by the regex engine to perform pattern
# matching on any string or text or file data that was passed into
# that object

# the method will return a match object (MO), that will contain the
# following: 
    #  all the matched values and other methods to be used on the matched
    # values

    # if the regex pattern specifies that some of the matched values must
    # be placed in 1 or more groups, then all the groups from each
    # line of the file data will be saved and separated by placing
    # them in a python list

# one of these methods is the group methods where any regex groups
# that contains vaules that were matched by the regex engine can be
# called upon individually.

# If the groups created are numbered groups, then each group will be
# identified by a number starting from 1 assigned to the first group.

# for example:
    # if 3 groups of values were matched on 1 line of the file data,
    # then the following is how to return/use the values from the groups
        # 1st group = finalDraftMO.group(1)
        # 2nd group = finalDraftMO.group(2)
        # 3rd group = finalDraftMO.group(3)
            # finalDraftMO is the variable that holds the matched
            # object after the regex engine has gone thru the string or
            # text or file data that was passed into the regex object
            # (regPat)
    
    # the 1st, 2nd and 3rd groups represents all the matched values
    # from just 1 line of the file data

    # the rest of the lines in the file data will have their own 3
    # groups that contains the matched values from their respective
    # lines 
        
# when the regex engine is evaluating a line from the file data with
# the regex pattern object, the following happens:
    # all the text from the file data that matched the regex pattern
    # will be placed into groups as defined by the regex pattern

    # the regex engine takes all the groups there were matched and
    # placed them in a list so they can separated from each other

    # the engine then goes on to the next line and does the samething
    # mentioned above until there are no lines left from the file
    # data
    
    # with all the groups categoriezed by the line within the file
    # data they came from and placed in a list, they can be used with
    # a "for loop" to:
        # pull the values from the groups that came from same line in
        # the file data

        # pull the values from groups that came from all the lines in
        # the file data
        
rawData.close()
# this line of code will close the file object when the code is
# done using the data within the file

# this is similar to closing a text editor that openned the file

mapping = open('Phase 1 Stuff/regexToGet-IPAddressToHostnameMapping/mapping.txt', 'a')
# this line of code with open a file called mapping.txt (if that exist), or create a
# file (if that file does not exist) and name it mapping.txt

# it will save that file as a file object and save that object in a
# variable called mapping

for r in finalDraftMO:
    mapping.write(r.group(1))   #1
    mapping.write(" ")          #2
    mapping.write(r.group(4))   #3
    mapping.write("\n")         #4
# the line of code will do the following:
    # create a "for" loop to interate over the items/things in the MO
    # finalDraftMO 
    
    # each item/thing that the code interates over will be saved in a
    # variable called "r"

    # the variable "r" will contain all the groups that produced a
    # match per line from the file data

    # for example:
        # when "r" represents the groups that were matched from the
        # 1st line of the file data the following happens:
            # line (#1) of the "for loop" will write the value from
            # group(1) (r.group(1)) on the 1st line of the text file
            # mapping.txt
            
            # line (#2) of the "for loop" will write a space after
            # the value of group(1) is written to the line

            # line (#3) of the "for loop" will write the value from
            # group(2) (r.group(2)) on the 1st line of the text file
            # mapping.txt

            # line (#4) of the "for loop" will write a new line after
            # the value of group(4) is written to the line

        # if the groups and their values that are represented by "r"
        # from the "for loop" are:
            # group(1) = 192.168.1.1
            # group(2) = ']
            # group(3) = (space char)
            # group(4) = Host-Name-320-139

        # lines #1-#4 of the "for loop" will produce the following
        # line in the file mapping.txt
            # 192.168.1.1 Host-Name-320-139 (followed by a new line)

    # once that line is written in the file mapping.txt the "for
    # loop" moves on to the next item in finalDraftMO Match Object
    # that represents all the groups matched from the 2nd line of
    # the file raw_ip_address_hostname_mapping 
        # remember the content of that file is represented by the variable:
            # rawDataContent

mapping.close()
# this line of code closes the file mapping.txt after the "for loop"
# has interated thru all the items and save that file.