##################################################################
# AmandaVCD is a free software which was made with the help of:  #
#                                                                #
#          @xel (programming)                                    #
#          @xel (designing)                                      #
#                                                                #
##################################################################
fname = input('name of file: ')

fopen = open(fname, 'r')

begincard = 'BEGIN:VCARD'
endcard = 'END:VCARD'
i = 0
cutline = fopen.readline()
while not cutline == '':
    if cutline[0:11] == begincard:
        i=i+1
        print(i)
        filnam='%i.vcf'%(i)
        testopen = open(filnam, 'w')
        if cutline[0:9] == endcard:
            testopen.write('END:VCARD')
            testopen.close()
            cutline = fopen.readline()
        else:
            testopen.write(cutline)
            cutline = fopen.readline()
    else:
        if cutline[0:9] == endcard:
            testopen.write('END:VCARD')
            testopen.close()
            cutline = fopen.readline()
        else:
            testopen.write(cutline)
            cutline = fopen.readline()
#EOF
