# package : group of modules(folder)
# module : the file which having .py extension, we can import the functionalites of the code and can reuse
# types: 2
#           pre-defined = in-built(already available) 3,20,000
#           user defined = user can design their own lib/modules/packages
# how to consider folder as package/module = create __init__.py in that folder

# syntax : from <package name>.<module name> import <function name>/*(all function)
# syntax : for single module : import <module name> as <alias name>

# user defined -----------
# source(main folder/package)
#     Choclate(sub-folder)
#         ferro(file)

from source.Choclate.ferro import display,show

print(display())
print(show())

from source.Choclate.ferro import * # imports all

print(display())
print(show())


from source.Choclate.ferro import display as dp, show as sh

print(dp())
print(sh())


# inbuilt-modules = os(os files/folder operations)
#                   time (time realted)
#                   datetime (date related)
#                   pandas (csv, data)
#                   numpy ()



