# w.r.p to get student marks based on h.tno i/p
# if H.tno in list print(the marks)
# if not print "Not Found"


student_marks = {101:{'T':90,'H':85},102:{'T':25,'H':50},103:{'T':99,'H':40}} #nested dict (dict witin dict)


def ask_id(htno):
    if htno in student_marks.keys(): # if 102 in [101,102,103]:
        print('Yes')
        print(student_marks[htno]) # st_ma[102]

    else:
        print('Not Found')


htno = int(input('Enter Hall Ticket number : '))
ask_id(htno) # fn call

# x = {'a':10,'b':20,'c':30,'d':10,'e':20}

# # print(x[1]) # index dosent follow

# print(x['b'])