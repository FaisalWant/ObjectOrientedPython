# backtopython5.py

# What's up with *.pyc?:

# CPython will cache the byte-compiled modules (.pyc)
# Cached .pyc files live in __pycache__/module.vers.pyc
# Automatically recompiled when source code is newer
# Doesn't change runtime speed, only loading speed

# COLLECTIONS.DEFAULTDICT:
# --------------------------
# Have:
# input_data = [('yellow', 1), ('blue', 2),
# ('yellow', 3), ('blue', 4), ('red', 1)]

# Want:
# output = {'blue': [2, 4], 'red': [1], 'yellow': [1, 3]}

# # One approach
# output = {}
# for k, v in input_data:
# if k not in output:
# output[k] = []
# output[k].append(v)
# print(output)            # => {'blue': [2, 4], 'red': [1], 'yellow': [1, 3]}


# # A better approach
# input_data = [...]
# output = collections.defaultdict(lambda: list())   -->accepts one argument - a zero-argument factory function to supply missing keys
# for k, v in input_data:      # When key is missing, go to the factory
# 	output[k].append(v)
# 	print(output)            # => defaultdict(<function <lambda> at 0x........>,{'red': [1], 'yellow': [1, 3], 'blue': [2, 4]})


# # Have: s = 'mississippi'

# # Want: d = {'i': 4, 'p': 2, 'm': 1, 's': 4}
# s = 'mississippi'
# d = collections.defaultdict(int) # or... lambda: 0
# for letter in s:
# 	d[letter] += 1
# 	print(d)
# # => defaultdict(<class 'int'>, {'i': 4, 'p': 2, 'm': 1, 's': 4})
# --------------------------------------
# |collections.Counter                 |
# |dict subclass for counting hashable |
# |objects                             |
# --------------------------------------
# # Have: s = 'mississippi'
# # Want: [('s', 4), ('m', 1), ('i', 4), ('p', 2)]

# s = 'mississippi'
# count = collections.Counter(s)
# print(count)                  # => Counter({'i': 4, 'm': 1, 'p': 2, 's': 4})
# print(list(count.items()))    # => [('s', 4), ('m', 1), ('i', 4), ('p', 2)]

# # Tally occurrences of words in a list

# colors = ['red', 'blue', 'red', 'green', 'blue']
# # One approach
# counter = collections.Counter()
# for color in colors:
# counter[color] += 1
# print(counter)               # Counter({'blue': 2, 'green': 1, 'red': 2})


# # A better approach
# counter = collections.Counter(colors)
# print(counter)               # Counter({'blue': 2, 'green': 1, 'red': 2})


# # Get most common elements!
# Counter('abracadabra').most_common(3)               # => [('a', 5), ('b', 2), ('r', 2)]

# # Supports basic arithmetic
# Counter('which') + Counter('witch')                 # => Counter({'c': 2, 'h': 3, 'i': 2, 't': 1, 'w': 2})
# Counter('abracadabra') - Counter('alakazam')        # => Counter({'a': 1, 'b': 2, 'c': 1, 'd': 1, 'r': 2})

# REGULAREXPRESSION:
# -------------------------------
# # Search for pattern match anywhere in string; return None if not found
# m = re.search(r"(\w+) (\w+)", "Physicist Isaac Newton")
# m.group(0)                             # "Isaac Newton" - the entire match
# m.group(1)                             # "Isaac" - first parenthesized subgroup
# m.group(2)                             # "Newton" - second parenthesized subgroup

# # Match pattern against start of string; return None if not found

# m = re.match(r"(?P<fname>\w+) (?P<lname>\w+)", "Malcolm Reynolds")
# m.group('fname')                       # => 'Malcolm'
# m.group('lname')                       # => 'Reynolds

# # Substitute occurrences of one pattern with another

# re.sub(r'@\w+\.com', '@stanford.edu', 'sam@go.com poohbear@bears.com')    # => sam@stanford.edu poohbear@stanford.edu
# pattern = re.compile(r'[a-z]+[0-9]{3}')                                   # compile pattern for fast ops
# match = re.search(pattern, '@@@abc123')                                   # pattern is first argument
# match.span()                                                              # (3, 9)


# def is_phone(num):

# 	return bool(re.match('\d{3} \d{3}-\d{4}', num))

# def get_area_code(num):
# 	m = re.match('(?P<areacode>\d{3}) \d{3}-\d{4}', num)
# 	if not m:
# 	    return None
# 	return m.group('areacode')

# -----------------------------
# |collections.Counter and re:|
# -----------------------------
# # Find the three most common words in Hamlet
# with open('hamlet.txt') as f:
# 	words = re.findall(r'\w+', f.read().lower())
# 	collections.Counter(words).most_common(3)   # => [('the', 1091), ('and', 969), ('to', 767)]



# COMBINATORICS:
# --------------

# def view(it): print(*[''.join(els) for els in it])
	
# 	view(itertools.product('ABCD', 'EFGH'))       # => AE AF AG AH BE BF BG BH CE CF CG CH DE DF DG DH
# 	view(itertools.product('ABCD', repeat=2))     # => AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# 	view(itertools.permutations('ABCD', 2))       # => AB AC AD BA BC BD CA CB CD DA DB DC
# 	view(itertools.combinations('ABCD', 2))       # => AB AC AD BC BD CD
# 	view(itertools.combinations_with_replacement('ABCD', 2)) # => AA AB AC AD BB BC BD CC CD DD


# INFINITE ITERATORS:
# -------------------
# # start, [step] -> start, start + step, ...
# itertools.count(10)                          # -> 10, 11, 12, 13, 14, ...

# # Cycle through elements of an iterable
# itertools.cycle('ABC')                       # -> 'A', 'B', 'C', 'A', ...

# # Repeat a single element over and over.
# itertools.repeat(10)                         # -> 10, 10, 10, 10, ...


# ----------------]
# |JSON:          ]
# ----------------]

# squares = {1:1, 2:4, 3:9, 4:16}
# # Serialize to/from string

# output = json.dumps(squares)                # output == "{1:1, 2:4, 3:9, 4:16}"
# json.loads(output)                          # => {1:1, 2:4, 3:9, 4:16}

# # Serialize to/from file
# with open('tmp.json', 'w') as outfile:
#     json.dump(squares, outfile)

# with open('tmp.json', 'r') as infile:
#    input = json.load(infile)


# # All variants support useful keyword arguments
# json.dumps(data, indent=4, sort_keys=True, separators=(',', ': '))



# RANDOM GENERATOR:
# ------------------
# # Random float x with 0.0 <= x < 1.0
# random.random() # => 0.37444887175646646

# # Random float x, 1.0 <= x < 10.0

# random.uniform(1, 10) # => 1.1800146073117523

# # Random integer from 1 to 6 (inclusive)
# random.randint(1, 6) # => 4 (https://xkcd.com/221/)

# # Random integer from 0 to 9 (inclusive)
# random.randrange(10) # => 7

# # Random even integer from 0 to 100 (inclusive)
# random.randrange(0, 101, 2)         # => 26

# # Choose a single element
# random.choice('abcdefghij') # => 'c'

# items = [1, 2, 3, 4, 5, 6, 7]
# random.shuffle(items)

# items # => [7, 3, 2, 5, 6, 4, 1]

# # k samples without replacement
# random.sample(range(5), k=3) # => [3, 1, 4]

# # Sample from statistical distributions (others exist)
# random.normalvariate(mu=0, sigma=3) # => 2.373780578271


# RUNNING MODULES AS SCRIPTS:
# ---------------------------
# # We can run a module (demo.py) as a script
# $ python3 demo.py # Doing so sets __name__ = '__main__'


# # We can even jump into the interpreter after we're done
# $ python3 -i demo.py

# # What if we want to do something like...
# $ python3 -i demo.py <arguments>


# # File: demo.py
# if __name__ == '__main__':
#    import sys
#    print(sys.argv)
# ———————————————————————————
# $ python3 demo.py 1 2 3
# ['demo.py', '1', '2', '3']

# $ python3 subdir/../demo.py foo
# ['subdir/../demo.py', 'foo']


# PATHLIB OBJECT ORIENTED FILESYSTEM PATHS:|
# -----------------------------------------

# p = pathlib.Path('/etc')

# q = p / 'ssh' # Overloaded __div__ method

# q # => PosixPath('/etc/ssh')

# q.exists() # => True

# q.is_dir() # => True

# # Print all python files somewhere in the current dir

# p = pathlib.Path.cwd() # Current working directory

# for f in p.glob('**/*.py'):
#     print(f)

# ======================
# SUBPROCESS and SHLEX:||
# ----------------------

# subprocess.call(["ls", "-l"]) # => 0

# # Automatically authenticate to Myth servers
# command = "kinit name@myth.stanford.edu --keytab=/etc/some-keytab"

# args = shlex.split(command) # args = ["kinit", ... ]

# subprocess.call(args) # => 0

# # For more complex needs, use Popen
# # Emulate 'ps aux | grep Spotify'

# sp_ps = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)

# sp_grep = subprocess.Popen(["grep", "Spotify"], stdin=sp_ps.stdout)


# DEBUGGING TOOLS:
# --------------------------------------------------

# #1) pprint — data pretty printer:

# # Some horrendous data structure
# ugly = {
# 'data': {
# 'after': 't3_3q8aog',
# 'before': None,
# 'kind': 'pagination',
# 'children': [{'a':1}, {'a':2}, {'b':1}, {}],
# 'uuid': '40b6f818'
# }
# }
# ugly['recursive'] = ugly # Contains recursive reference

# print(ugly)
# |*********************************************************
# |# {'data': {'before': None, 'kind': 'pagination',
# |#'uuid': '40b6f818', 'after': 't3_3q8aog', 'children':
# |#[{'a': 1}, {'a': 2}, {'b': 1}, {}]}, 'recursive': {...}
# |# }
# **********************************************************

# pprint.pprint(ugly, width=56, depth=2)
# # {'data': {'after': 't3_3q8aog',
# # 'before': None,
# # 'children': [...],
# # 'kind': 'pagination',
# # 'uuid': '40b6f818'},
# # 'recursive': <Recursion on dict with id=4372885384>}

# # 2) timeit - time short snippets:

#    # Command Line Interface
# 	$ python3 -m timeit '"-".join(str(n) for n in range(100))'
# 	10000 loops, best of 3: 30.2 usec per loop
# 	$ python3 -m timeit '"-".join([str(n) for n in range(100)])'
# 	10000 loops, best of 3: 27.5 usec per loop
# 	$ python3 -m timeit '"-".join(map(str, range(100)))'
# 	10000 loops, best of 3: 23.2 usec per loop
   
#    # Python Interface

# import timeit

# 	timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# 	# => 0.3018611848820001
# 	timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
# 	# => 0.2727368790656328
# 	timeit.timeit('"-".join(map(str, range(100)))', number=10000)



# UNICODE DATA:
# -----------------
# unicodedata.lookup('SLICE OF PIZZA')
# # => '?'
# unicodedata.name('?')
# # => 'OK HAND SIGN'
# unicodedata.numeric('¾')
# # => 0.75


# COMMON ONE-LINERS:
# ------------------
# any([True, True, False]) # => True
# all([True, True, False]) # => False
# int('45') # => 45
# int('0x2a', 16) # => 42
# int('1011', 2) # => 11
# hex(42) # => '0x2a'
# bin(42) # => '0b101010'
# ord('a') # => 97
# chr(97) # => 'a'
# round(123.45, 1) # => 123.4
# round(123.45, -2) # => 100
# max(2, 3) # => 3
# max([0, 4, 1]) # => 4
# min(['apple', 'banana', 'pear'], key=len) # => 0
# sum([3, 5, 7]) # => 15
# pow(3, 5) # => 243 (= 3 ** 5)
# pow(3, 5, 10) # => 3 (= (3 ** 5) % 10, efficiently)
# quotient, remainder = divmod(10, 6)
# # quotient, remainder => (1, 4)

# # Flatten a list of lists (slower than itertools.chain)
# sum([[3, 5], [1, 7], [4]], []) # => [3, 5, 1, 7, 4]

# OTHER MODULES:
# 6.1. string — Common string operations
# 7.1. struct — Interpret bytes as packed binary data
# 8.1. datetime — Basic date and time types
# 9.5. fractions — Rational numbers
# 9.7. statistics — Mathematical statistics functions
# 10.3. operator — Standard operators as functions
# 12.1. pickle — Python object serialization
# 14.1. csv — CSV File Reading and Writing
# 16.1. os — Miscellaneous operating system interfaces
# 16.3. time — Time access and conversions
# 16.4. argparse — Parser for command-line options,
# arguments and sub-commands
# 16.6. logging — Logging facility for Python
# 17.1. threading — Thread-based parallelism
# 17.2. multiprocessing — Process-based parallelism
# 18.1. socket — Low-level networking interface
# 18.5. asyncio – Asynchronous I/O, event loop, coroutines
# and tasks
# 18.8. signal — Set handlers for asynchronous events
# 26.3. unittest — Unit testing framework
# 26.6. 2to3 - Automated Python 2 to 3 code translation
# 27.3. pdb — The Python Debugger
# 27.6. trace — Trace or track Python statement execution
# 29.12. inspect — Inspect live objects