# Print out all of the strings in the following array in alphabetical order, each on a separate line.

listOfStrings = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

# The expected output is:
# 'Cha Cha'
# 'Foxtrot'
# 'Jive'
# 'Paso Doble'
# 'Rumba'
# 'Samba'
# 'Tango'
# 'Viennese Waltz'
# 'Waltz'


listOfStrings.sort()
for i in listOfStrings:
    print(i)