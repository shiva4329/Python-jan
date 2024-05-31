# joins in mysql ---->

# insert into A(Id,school_name) values(1,'A'),(2,'B'),(3,'C')
#
# select * from A
#
# insert into B(Id,stu_name,marks) values(2,'sam',80),(3,'don',99),(4,'ram',60)
#
# select * from B
#
# -- Inner join --> only matched/common data bsed on column (Id)
#
# select * from A inner join B on A.Id = B.Id
#
# select B.Id,school_name,stu_name,marks from A inner join B on A.Id = B.Id
#
# -- Left join -> common data+total left table data
#
# select * from A left join B on A.Id = B.Id
#
# -- righ join -> common data+total right table data
# select * from A right join B on A.Id = B.Id
#
# -- full join -> common data+total right and left table data
# select * from A full join B on A.Id = B.Id