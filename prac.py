python is

high level language
object oriented
portable
robust
scalable
interapreted and byte-compiled


first python code compiled into byte code then byte-code executed by the pvm


package management:-python comes with a built-in package manager called pip 


python datatype:-There is no limit to how long an integer can be:it will depend on your machine memory constrains
    float number are 64-bit,the max value 1.8*10^308

numeric
    int
    float

text
    str

boolean
    bool

sequence
    list
    tuple
    range

mapping
    dict

set
    set: uordered,unique,mutable
    frozenset: unordered,unique,immutable

binary
    bytes
    bytearray
    memoryview

None
    nonetype


DATA STRUCTURE(list,tuple,dictionary,set)

    list
    A list is a collection of arbitrary item that are ordered and changeable(mutable)

    important characteristics of list
    ordered-The sequence of elements remains fixed in a list's lifetime
    Can contain any arbitrary objects (data), e.g. my_list = [123, “testing”, False]
    Elements can be accessed by using an index, e.g. my_list[1]
    Can be nested to any depth, e.g. my_list = [“a”, [“bb”, [“ccc”, “ddd”], “cc” ], “b” ]
    Mutable, e.g. my_list[2] = “new value”
    Dynamic, e.g. my_list.append(123)
