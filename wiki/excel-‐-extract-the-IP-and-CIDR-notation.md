~~~
=SUBSTITUTE(RIGHT(A1,LEN(A1)-FIND("_",A1,FIND("_",A1)+1)), "_", "/")

=MID(A1,FIND("_",A1)+1,FIND("_",A1,FIND("_",A1)+1)-FIND("_",A1)-1)

=SUBSTITUTE(RIGHT(A1,LEN(A1)-FIND("_",A1,FIND("_",A1)+1)), "_", "/")




~~~