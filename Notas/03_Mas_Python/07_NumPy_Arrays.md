[Contenidos](../Contenidos.md) \| [Anterior (6 Complejidad de algoritmos)](06_Complejidad.md) \| [Próximo (8 Cierre)](08_Cierre.md)

# 3.7 Numpy básico

## 1.4.1. The NumPy array object
Section contents

What are NumPy and NumPy arrays?
Creating arrays
Basic data types
Basic visualization
Indexing and slicing
Copies and views
Fancy indexing
1.4.1.1. What are NumPy and NumPy arrays?
NumPy arrays
Python objects: 
high-level number objects: integers, floating point
containers: lists (costless insertion and append), dictionaries (fast lookup)
NumPy provides: 
extension package to Python for multi-dimensional arrays
closer to hardware (efficiency)
designed for scientific computation (convenience)
Also known as array oriented computing

>>>
import numpy as np
a = np.array([0, 1, 2, 3])
a

 For example, An array containing:
values of an experiment/simulation at discrete time steps
signal recorded by a measurement device, e.g. sound wave
pixels of an image, grey-level or colour
3-D data measured at different X-Y-Z positions, e.g. MRI scan
…
Why it is useful: Memory-efficient container that provides fast numerical operations.

L = range(1000)

%timeit [i**2 for i in L]


a = np.arange(1000)

%timeit a**2

NumPy Reference documentation
On the web: http://docs.scipy.org/

Interactive help:

np.array?



Looking for something:

>>>
np.lookfor('create array') 






np.con*?




Import conventions
The recommended convention to import numpy is:

>>>
import numpy as np
1.4.1.2. Creating arrays
Manual construction of arrays
1-D:

>>>
a = np.array([0, 1, 2, 3])
a

a.ndim

a.shape

len(a)

2-D, 3-D, …:

>>>
b = np.array([[0, 1, 2], [3, 4, 5]])    # 2 x 3 array
b


b.ndim

b.shape

len(b)     # returns the size of the first dimension


c = np.array([[[1], [2]], [[3], [4]]])
c





c.shape

Exercise: Simple arrays

Create a simple two dimensional array. First, redo the examples from above. And then create your own: how about odd numbers counting backwards on the first row, and even numbers on the second?
Use the functions len(), numpy.shape() on these arrays. How do they relate to each other? And to the ndim attribute of the arrays?
Functions for creating arrays
 In practice, we rarely enter items one by one…
Evenly spaced:

>>>
a = np.arange(10) # 0 .. n-1  (!)
a

b = np.arange(1, 9, 2) # start, end (exclusive), step
b

or by number of points:

>>>
c = np.linspace(0, 1, 6)   # start, end, num-points
c

d = np.linspace(0, 1, 5, endpoint=False)
d

Common arrays:

>>>
a = np.ones((3, 3))  # reminder: (3, 3) is a tuple
a



b = np.zeros((2, 2))
b


c = np.eye(3)
c



d = np.diag(np.array([1, 2, 3, 4]))
d




np.random: random numbers (Mersenne Twister PRNG):

>>>
a = np.random.rand(4)       # uniform in [0, 1]
a  


b = np.random.randn(4)      # Gaussian
b  


np.random.seed(1234)        # Setting the random seed
Exercise: Creating arrays using functions

Experiment with arange, linspace, ones, zeros, eye and diag.
Create different kinds of arrays with random numbers.
Try setting the seed before creating an array with random values.
Look at the function np.empty. What does it do? When might this be useful?
1.4.1.3. Basic data types
You may have noticed that, in some instances, array elements are displayed with a trailing dot (e.g. 2. vs 2). This is due to a difference in the data-type used:

>>>
a = np.array([1, 2, 3])
a.dtype


b = np.array([1., 2., 3.])
b.dtype

 Different data-types allow us to store data more compactly in memory, but most of the time we simply work with floating point numbers. Note that, in the example above, NumPy auto-detects the data-type from the input.
You can explicitly specify which data-type you want:

>>>
c = np.array([1, 2, 3], dtype=float)
c.dtype

The default data type is floating point:

>>>
a = np.ones((3, 3))
a.dtype

There are also other types:

Complex:    
>>>
d = np.array([1+2j, 3+4j, 5+6*1j])
d.dtype

Bool:   
>>>
e = np.array([True, False, False, True])
e.dtype

Strings:    
>>>
f = np.array(['Bonjour', 'Hello', 'Hallo'])
f.dtype     # <--- strings containing max. 7 letters  

Much more:  
int32
int64
uint32
uint64
1.4.1.4. Basic visualization
Now that we have our first data arrays, we are going to visualize them.

Start by launching IPython:

$ ipython # or ipython3 depending on your install
Or the notebook:

$ jupyter notebook
Once IPython has started, enable interactive plots:

>>>
%matplotlib  
Or, from the notebook, enable plots in the notebook:

>>>
%matplotlib inline 
The inline is important for the notebook, so that plots are displayed in the notebook and not in a new window.

Matplotlib is a 2D plotting package. We can import its functions as below:

>>>
import matplotlib.pyplot as plt  # the tidy way
And then use (note that you have to use show explicitly if you have not enabled interactive plots with %matplotlib):

>>>
plt.plot(x, y)       # line plot    
plt.show()           # <-- shows the plot (not needed with interactive plots) 
Or, if you have enabled interactive plots with %matplotlib:

>>>
plt.plot(x, y)       # line plot    
1D plotting:
>>>
x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
plt.plot(x, y)       # line plot    

plt.plot(x, y, 'o')  # dot plot    

../../_images/sphx_glr_plot_basic1dplot_001.png
2D arrays (such as images):
>>>
image = np.random.rand(30, 30)
plt.imshow(image, cmap=plt.cm.hot)    

plt.colorbar()    

../../_images/sphx_glr_plot_basic2dplot_001.png
See also More in the: matplotlib chapter
Exercise: Simple visualizations

Plot some simple arrays: a cosine as a function of time and a 2D matrix.
Try using the gray colormap on the 2D matrix.
1.4.1.5. Indexing and slicing
The items of an array can be accessed and assigned to the same way as other Python sequences (e.g. lists):

>>>
a = np.arange(10)
a

a[0], a[2], a[-1]

 Indices begin at 0, like other Python sequences (and C/C++). In contrast, in Fortran or Matlab, indices begin at 1.
The usual python idiom for reversing a sequence is supported:

>>>
a[::-1]

For multidimensional arrays, indexes are tuples of integers:

>>>
a = np.diag(np.arange(3))
a



a[1, 1]

a[2, 1] = 10 # third line, second column
a



a[1]

Note
In 2D, the first dimension corresponds to rows, the second to columns.
for multidimensional a, a[0] is interpreted by taking all elements in the unspecified dimensions.
Slicing: Arrays, like other Python sequences can also be sliced:

>>>
a = np.arange(10)
a

a[2:9:3] # [start:end:step]

Note that the last index is not included! :

>>>
a[:4]

All three slice components are not required: by default, start is 0, end is the last and step is 1:

>>>
a[1:3]

a[::2]

a[3:]

A small illustrated summary of NumPy indexing and slicing…

../../_images/numpy_indexing.png
You can also combine assignment and slicing:

>>>
a = np.arange(10)
a[5:] = 10
a

b = np.arange(5)
a[5:] = b[::-1]
a

Exercise: Indexing and slicing

Try the different flavours of slicing, using start, end and step: starting from a linspace, try to obtain odd numbers counting backwards, and even numbers counting forwards.

Reproduce the slices in the diagram above. You may use the following expression to create the array:

>>>
np.arange(6) + np.arange(0, 51, 10)[:, np.newaxis]






Exercise: Array creation

Create the following arrays (with correct data types):

[[1, 1, 1, 1],
 [1, 1, 1, 1],
 [1, 1, 1, 2],
 [1, 6, 1, 1]]

[[0., 0., 0., 0., 0.],
 [2., 0., 0., 0., 0.],
 [0., 3., 0., 0., 0.],
 [0., 0., 4., 0., 0.],
 [0., 0., 0., 5., 0.],
 [0., 0., 0., 0., 6.]]
Par on course: 3 statements for each

Hint: Individual array elements can be accessed similarly to a list, e.g. a[1] or a[1, 2].

Hint: Examine the docstring for diag.

Exercise: Tiling for array creation

Skim through the documentation for np.tile, and use this function to construct the array:

[[4, 3, 4, 3, 4, 3],
 [2, 1, 2, 1, 2, 1],
 [4, 3, 4, 3, 4, 3],
 [2, 1, 2, 1, 2, 1]]
1.4.1.6. Copies and views
A slicing operation creates a view on the original array, which is just a way of accessing array data. Thus the original array is not copied in memory. You can use np.may_share_memory() to check if two arrays share the same memory block. Note however, that this uses heuristics and may give you false positives.

When modifying the view, the original array is modified as well:

>>>
a = np.arange(10)
a

b = a[::2]
b

np.may_share_memory(a, b)

b[0] = 12
b

a   # (!)


a = np.arange(10)
c = a[::2].copy()  # force a copy
c[0] = 12
a


np.may_share_memory(a, c)

This behavior can be surprising at first sight… but it allows to save both memory and time.

Worked example: Prime number sieve

../../_images/prime-sieve.png
Compute prime numbers in 0–99, with a sieve

Construct a shape (100,) boolean array is_prime, filled with True in the beginning:
>>>
is_prime = np.ones((100,), dtype=bool)
Cross out 0 and 1 which are not primes:
>>>
is_prime[:2] = 0
For each integer j starting from 2, cross out its higher multiples:
>>>
N_max = int(np.sqrt(len(is_prime) - 1))
for j in range(2, N_max + 1):
    is_prime[2*j::j] = False
Skim through help(np.nonzero), and print the prime numbers

Follow-up:

Move the above code into a script file named prime_sieve.py
Run it to check it works
Use the optimization suggested in the sieve of Eratosthenes:
Skip j which are already known to not be primes
The first number to cross out is j^2
1.4.1.7. Fancy indexing
 NumPy arrays can be indexed with slices, but also with boolean or integer arrays (masks). This method is called fancy indexing. It creates copies not views.
Using boolean masks
>>>
np.random.seed(3)
a = np.random.randint(0, 21, 15)
a

(a % 3 == 0)


mask = (a % 3 == 0)
extract_from_a = a[mask] # or,  a[a%3==0]
extract_from_a           # extract a sub-array with the mask

Indexing with a mask can be very useful to assign a new value to a sub-array:

>>>
a[a % 3 == 0] = -1
a

Indexing with an array of integers
>>>
a = np.arange(0, 100, 10)
a

Indexing can be done with an array of integers, where the same index is repeated several time:

>>>
a[[2, 3, 2, 4, 2]]  # note: [2, 3, 2, 4, 2] is a Python list

New values can be assigned with this kind of indexing:

>>>
a[[9, 7]] = -100
a

 When a new array is created by indexing with an array of integers, the new array has the same shape as the array of integers:
>>>
a = np.arange(10)
idx = np.array([[3, 4], [9, 7]])
idx.shape

a[idx]


The image below illustrates various fancy indexing applications

../../_images/numpy_fancy_indexing.png
Exercise: Fancy indexing

Again, reproduce the fancy indexing shown in the diagram above.
Use fancy indexing on the left and array creation on the right to assign values into an array, for instance by setting parts of the array in the diagram above to zero.

## 1.4.2. Numerical operations on arrays
Section contents

Elementwise operations
Basic reductions
Broadcasting
Array shape manipulation
Sorting data
Summary
1.4.2.1. Elementwise operations
Basic operations
With scalars:

>>>
a = np.array([1, 2, 3, 4])
a + 1

2**a

All arithmetic operates elementwise:

>>>
b = np.ones(4) + 1
a - b

a * b


j = np.arange(5)
2**(j + 1) - j

These operations are of course much faster than if you did them in pure python:

>>>
a = np.arange(10000)
%timeit a + 1  

l = range(10000)
%timeit [i+1 for i in l] 

 Array multiplication is not matrix multiplication:
>>>
c = np.ones((3, 3))
c * c                   # NOT matrix multiplication!



Note Matrix multiplication:
>>>
c.dot(c)



Exercise: Elementwise operations

Try simple arithmetic elementwise operations: add even elements with odd elements
Time them against their pure python counterparts using %timeit.
Generate:
[2**0, 2**1, 2**2, 2**3, 2**4]
a_j = 2^(3*j) - j
Other operations
Comparisons:

>>>
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
a == b

a > b

 Array-wise comparisons:
>>>
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
c = np.array([1, 2, 3, 4])
np.array_equal(a, b)

np.array_equal(a, c)

Logical operations:

>>>
a = np.array([1, 1, 0, 0], dtype=bool)
b = np.array([1, 0, 1, 0], dtype=bool)
np.logical_or(a, b)

np.logical_and(a, b)

Transcendental functions:

>>>
a = np.arange(5)
np.sin(a)

np.log(a)

np.exp(a)

Shape mismatches

>>>
a = np.arange(4)
a + np.array([1, 2])  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: operands could not be broadcast together with shapes (4) (2)
Broadcasting? We’ll return to that later.

Transposition:

>>>
a = np.triu(np.ones((3, 3)), 1)   # see help(np.triu)
a



a.T



 The transposition is a view
As a result, the following code is wrong and will not make a matrix symmetric:

>>>
a += a.T
It will work for small arrays (because of buffering) but fail for large one, in unpredictable ways.

Note Linear algebra
The sub-module numpy.linalg implements basic linear algebra, such as solving linear systems, singular value decomposition, etc. However, it is not guaranteed to be compiled using efficient routines, and thus we recommend the use of scipy.linalg, as detailed in section Linear algebra operations: scipy.linalg

Exercise other operations

Look at the help for np.allclose. When might this be useful?
Look at the help for np.triu and np.tril.
1.4.2.2. Basic reductions
Computing sums
>>>
x = np.array([1, 2, 3, 4])
np.sum(x)

x.sum()

../../_images/reductions.png
Sum by rows and by columns:

>>>
x = np.array([[1, 1], [2, 2]])
x


x.sum(axis=0)   # columns (first dimension)

x[:, 0].sum(), x[:, 1].sum()

x.sum(axis=1)   # rows (second dimension)

x[0, :].sum(), x[1, :].sum()

 Same idea in higher dimensions:
>>>
x = np.random.rand(2, 2, 2)
x.sum(axis=2)[0, 1]     

x[0, 1, :].sum()     

Other reductions
— works the same way (and take axis=)

Extrema:

>>>
x = np.array([1, 3, 2])
x.min()

x.max()


x.argmin()  # index of minimum

x.argmax()  # index of maximum

Logical operations:

>>>
np.all([True, True, False])

np.any([True, True, False])

Note Can be used for array comparisons:
>>>
a = np.zeros((100, 100))
np.any(a != 0)

np.all(a == a)


a = np.array([1, 2, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])
((a <= b) & (b <= c)).all()

Statistics:

>>>
x = np.array([1, 2, 3, 1])
y = np.array([[1, 2, 3], [5, 6, 1]])
x.mean()

np.median(x)

np.median(y, axis=-1) # last axis


x.std()          # full population standard dev.

… and many more (best to learn as you go).

Exercise: Reductions

Given there is a sum, what other function might you expect to see?
What is the difference between sum and cumsum?
Worked Example: data statistics

Data in populations.txt describes the populations of hares and lynxes (and carrots) in northern Canada during 20 years.

You can view the data in an editor, or alternatively in IPython (both shell and notebook):

!cat data/populations.txt
First, load the data into a NumPy array:

>>>
data = np.loadtxt('data/populations.txt')
year, hares, lynxes, carrots = data.T  # trick: columns to variables
Then plot it:

>>>
from matplotlib import pyplot as plt
plt.axes([0.2, 0.1, 0.5, 0.8]) 
plt.plot(year, hares, year, lynxes, year, carrots) 
plt.legend(('Hare', 'Lynx', 'Carrot'), loc=(1.05, 0.5)) 
../../_images/sphx_glr_plot_populations_001.png
The mean populations over time:

>>>
populations = data[:, 1:]
populations.mean(axis=0)

The sample standard deviations:

>>>
populations.std(axis=0)

Which species has the highest population each year?:

>>>
np.argmax(populations, axis=1)

Worked Example: diffusion using a random walk algorithm

../../_images/random_walk.png Let us consider a simple 1D random walk process: at each time step a walker jumps right or left with equal probability.
We are interested in finding the typical distance from the origin of a random walker after t left or right jumps? We are going to simulate many “walkers” to find this law, and we are going to do so using array computing tricks: we are going to create a 2D array with the “stories” (each walker has a story) in one direction, and the time in the other:

../../_images/random_walk_schema.png
>>>
n_stories = 1000 # number of walkers
t_max = 200      # time during which we follow the walker
We randomly choose all the steps 1 or -1 of the walk:

>>>
t = np.arange(t_max)
steps = 2 * np.random.randint(0, 1 + 1, (n_stories, t_max)) - 1 # +1 because the high value is exclusive
np.unique(steps) # Verification: all steps are 1 or -1

We build the walks by summing steps along the time:

>>>
positions = np.cumsum(steps, axis=1) # axis = 1: dimension of time
sq_distance = positions**2
We get the mean in the axis of the stories:

>>>
mean_sq_distance = np.mean(sq_distance, axis=0)
Plot the results:

>>>
plt.figure(figsize=(4, 3)) 

plt.plot(t, np.sqrt(mean_sq_distance), 'g.', t, np.sqrt(t), 'y-') 

plt.xlabel(r"$t$") 

plt.ylabel(r"$\sqrt{\langle (\delta x)^2 \rangle}$") 

plt.tight_layout() # provide sufficient space for labels
../../_images/sphx_glr_plot_randomwalk_001.png
We find a well-known result in physics: the RMS distance grows as the square root of the time!

1.4.2.3. Broadcasting
Basic operations on numpy arrays (addition, etc.) are elementwise

This works on arrays of the same size.

Nevertheless, It’s also possible to do operations on arrays of different
sizes if NumPy can transform these arrays so that they all have
the same size: this conversion is called broadcasting.
The image below gives an example of broadcasting:

../../_images/numpy_broadcasting.png
Let’s verify:

>>>
a = np.tile(np.arange(0, 40, 10), (3, 1)).T
a




b = np.array([0, 1, 2])
a + b




We have already used broadcasting without knowing it!:

>>>
a = np.ones((4, 5))
a[0] = 2  # we assign an array of dimension 0 to an array of dimension 1
a




A useful trick:

>>>
a = np.arange(0, 40, 10)
a.shape

a = a[:, np.newaxis]  # adds a new axis -> 2D array
a.shape

a




a + b




 Broadcasting seems a bit magical, but it is actually quite natural to use it when we want to solve a problem whose output data is an array with more dimensions than input data.
Worked Example: Broadcasting

Let’s construct an array of distances (in miles) between cities of Route 66: Chicago, Springfield, Saint-Louis, Tulsa, Oklahoma City, Amarillo, Santa Fe, Albuquerque, Flagstaff and Los Angeles.

>>>
mileposts = np.array([0, 198, 303, 736, 871, 1175, 1475, 1544,
       1913, 2448])
distance_array = np.abs(mileposts - mileposts[:, np.newaxis])
distance_array










../../_images/route66.png
A lot of grid-based or network-based problems can also use broadcasting. For instance, if we want to compute the distance from the origin of points on a 5x5 grid, we can do

>>>
x, y = np.arange(5), np.arange(5)[:, np.newaxis]
distance = np.sqrt(x ** 2 + y ** 2)
distance





Or in color:

>>>
plt.pcolor(distance)    
plt.colorbar()    
../../_images/sphx_glr_plot_distances_001.png
Remark : the numpy.ogrid() function allows to directly create vectors x and y of the previous example, with two “significant dimensions”:

>>>
x, y = np.ogrid[0:5, 0:5]
x, y





x.shape, y.shape

distance = np.sqrt(x ** 2 + y ** 2)
 So, np.ogrid is very useful as soon as we have to handle computations on a grid. On the other hand, np.mgrid directly provides matrices full of indices for cases where we can’t (or don’t want to) benefit from broadcasting:
>>>
x, y = np.mgrid[0:4, 0:4]
x




y




See also Broadcasting: discussion of broadcasting in the Advanced NumPy chapter.
1.4.2.4. Array shape manipulation
Flattening
>>>
a = np.array([[1, 2, 3], [4, 5, 6]])
a.ravel()

a.T



a.T.ravel()

Higher dimensions: last dimensions ravel out “first”.

Reshaping
The inverse operation to flattening:

>>>
a.shape

b = a.ravel()
b = b.reshape((2, 3))
b


Or,

>>>
a.reshape((2, -1))    # unspecified (-1) value is inferred


 ndarray.reshape may return a view (cf help(np.reshape))), or copy
>>>
b[0, 0] = 99
a


Beware: reshape may also return a copy!:

>>>
a = np.zeros((3, 2))
b = a.T.reshape(3*2)
b[0] = 9
a



To understand this you need to learn more about the memory layout of a numpy array.

Adding a dimension
Indexing with the np.newaxis object allows us to add an axis to an array (you have seen this already above in the broadcasting section):

>>>
z = np.array([1, 2, 3])
z


z[:, np.newaxis]




z[np.newaxis, :]

Dimension shuffling
>>>
a = np.arange(4*3*2).reshape(4, 3, 2)
a.shape

a[0, 2, 1]

b = a.transpose(1, 2, 0)
b.shape

b[2, 1, 0]

Also creates a view:

>>>
b[2, 1, 0] = -1
a[0, 2, 1]

Resizing
Size of an array can be changed with ndarray.resize:

>>>
a = np.arange(4)
a.resize((8,))
a

However, it must not be referred to somewhere else:

>>>
b = a
a.resize((4,))   
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: cannot resize an array that has been referenced or is

Exercise: Shape manipulations

Look at the docstring for reshape, especially the notes section which has some more information about copies and views.
Use flatten as an alternative to ravel. What is the difference? (Hint: check which one returns a view and which a copy)
Experiment with transpose for dimension shuffling.
1.4.2.5. Sorting data
Sorting along an axis:

>>>
a = np.array([[4, 3, 5], [1, 2, 1]])
b = np.sort(a, axis=1)
b


Note Sorts each row separately!
In-place sort:

>>>
a.sort(axis=1)
a


Sorting with fancy indexing:

>>>
a = np.array([4, 3, 1, 2])
j = np.argsort(a)
j

a[j]

Finding minima and maxima:

>>>
a = np.array([4, 3, 1, 2])
j_max = np.argmax(a)
j_min = np.argmin(a)
j_max, j_min

Exercise: Sorting

Try both in-place and out-of-place sorting.
Try creating arrays with different dtypes and sorting them.
Use all or array_equal to check the results.
Look at np.random.shuffle for a way to create sortable input quicker.
Combine ravel, sort and reshape.
Look at the axis keyword for sort and rewrite the previous exercise.
1.4.2.6. Summary
What do you need to know to get started?

Know how to create arrays : array, arange, ones, zeros.

Know the shape of the array with array.shape, then use slicing to obtain different views of the array: array[::2], etc. Adjust the shape of the array using reshape or flatten it with ravel.

Obtain a subset of the elements of an array and/or modify their values with masks

>>>
a[a < 0] = 0
Know miscellaneous operations on arrays, such as finding the mean or max (array.max(), array.mean()). No need to retain everything, but have the reflex to search in the documentation (online docs, help(), lookfor())!!

For advanced use: master the indexing with arrays of integers, as well as broadcasting. Know more NumPy functions to handle various array operations.

Quick read

If you want to do a first quick pass through the Scipy lectures to learn the ecosystem, you can directly skip to the next chapter: Matplotlib: plotting.

The remainder of this chapter is not necessary to follow the rest of the intro part. But be sure to come back and finish this chapter, as well as to do some more exercices.

## 1.4.5. Some exercises
1.4.5.1. Array manipulations
Form the 2-D array (without typing it in explicitly):

[[1,  6, 11],
 [2,  7, 12],
 [3,  8, 13],
 [4,  9, 14],
 [5, 10, 15]]
and generate a new array containing its 2nd and 4th rows.

Divide each column of the array:

>>>
import numpy as np
a = np.arange(25).reshape(5, 5)
elementwise with the array b = np.array([1., 5, 10, 15, 20]). (Hint: np.newaxis).

Harder one: Generate a 10 x 3 array of random numbers (in range [0,1]). For each row, pick the number closest to 0.5.

Use abs and argsort to find the column j closest for each row.
Use fancy indexing to extract the numbers. (Hint: a[i,j] – the array i must contain the row numbers corresponding to stuff in j.)
1.4.5.2. Picture manipulation: Framing a Face
Let’s do some manipulations on numpy arrays by starting with an image of a racoon. scipy provides a 2D array of this image with the scipy.misc.face function:

>>>
from scipy import misc
face = misc.face(gray=True)  # 2D grayscale image
Here are a few images we will be able to obtain with our manipulations: use different colormaps, crop the image, change some parts of the image.

../../_images/faces.png
Let’s use the imshow function of matplotlib to display the image.

>>>
import matplotlib.pyplot as plt
face = misc.face(gray=True)
plt.imshow(face)    

The face is displayed in false colors. A colormap must be
specified for it to be displayed in grey.

>>>
plt.imshow(face, cmap=plt.cm.gray)    

Create an array of the image with a narrower centering : for example,
remove 100 pixels from all the borders of the image. To check the result, display this new array with imshow.

>>>
crop_face = face[100:-100, 100:-100]
We will now frame the face with a black locket. For this, we
need to create a mask corresponding to the pixels we want to be black. The center of the face is around (660, 330), so we defined the mask by this condition (y-300)**2 + (x-660)**2

>>>
sy, sx = face.shape
y, x = np.ogrid[0:sy, 0:sx] # x and y indices of pixels
y.shape, x.shape

centerx, centery = (660, 300) # center of the image
mask = ((y - centery)**2 + (x - centerx)**2) > 230**2 # circle
then we assign the value 0 to the pixels of the image corresponding to the mask. The syntax is extremely simple and intuitive:

>>>
face[mask] = 0
plt.imshow(face)    

Follow-up: copy all instructions of this exercise in a script called
face_locket.py then execute this script in IPython with %run face_locket.py.

Change the circle to an ellipsoid.

1.4.5.3. Data statistics
The data in populations.txt describes the populations of hares and lynxes (and carrots) in northern Canada during 20 years:

>>>
data = np.loadtxt('data/populations.txt')
year, hares, lynxes, carrots = data.T  # trick: columns to variables

import matplotlib.pyplot as plt
plt.axes([0.2, 0.1, 0.5, 0.8]) 

plt.plot(year, hares, year, lynxes, year, carrots) 

plt.legend(('Hare', 'Lynx', 'Carrot'), loc=(1.05, 0.5)) 

../../_images/sphx_glr_plot_populations_001.png
Computes and print, based on the data in populations.txt…

The mean and std of the populations of each species for the years in the period.
Which year each species had the largest population.
Which species has the largest population for each year. (Hint: argsort & fancy indexing of np.array(['H', 'L', 'C']))
Which years any of the populations is above 50000. (Hint: comparisons and np.any)
The top 2 years for each species when they had the lowest populations. (Hint: argsort, fancy indexing)
Compare (plot) the change in hare population (see help(np.gradient)) and the number of lynxes. Check correlation (see help(np.corrcoef)).
… all without for-loops.

Solution: Python source file

1.4.5.4. Crude integral approximations
Write a function f(a, b, c) that returns a^b - c. Form a 24x12x6 array containing its values in parameter ranges [0,1] x [0,1] x [0,1].

Approximate the 3-d integral

\int_0^1\int_0^1\int_0^1(a^b-c)da\,db\,dc

over this volume with the mean. The exact result is: \ln 2 - \frac{1}{2}\approx0.1931\ldots — what is your relative error?

(Hints: use elementwise operations and broadcasting. You can make np.ogrid give a number of points in given range with np.ogrid[0:1:20j].)

Reminder Python functions:

def f(a, b, c):
    return some_result
Solution: Python source file

1.4.5.5. Mandelbrot set
../../_images/sphx_glr_plot_mandelbrot_001.png
Write a script that computes the Mandelbrot fractal. The Mandelbrot iteration:

N_max = 50
some_threshold = 50

c = x + 1j*y

z = 0
for j in range(N_max):
    z = z**2 + c
Point (x, y) belongs to the Mandelbrot set if |z| < some_threshold.

Do this computation by:

Construct a grid of c = x + 1j*y values in range [-2, 1] x [-1.5, 1.5]
Do the iteration
Form the 2-d boolean mask indicating which points are in the set
Save the result to an image with:
>>>
import matplotlib.pyplot as plt
plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5]) 

plt.gray()
plt.savefig('mandelbrot.png')
Solution: Python source file

1.4.5.6. Markov chain
../../_images/markov-chain.png
Markov chain transition matrix P, and probability distribution on the states p:

0 <= P[i,j] <= 1: probability to go from state i to state j
Transition rule: p_{new} = P^T p_{old}
all(sum(P, axis=1) == 1), p.sum() == 1: normalization
Write a script that works with 5 states, and:

Constructs a random matrix, and normalizes each row so that it is a transition matrix.
Starts from a random (normalized) probability distribution p and takes 50 steps => p_50
Computes the stationary distribution: the eigenvector of P.T with eigenvalue 1 (numerically: closest to 1) => p_stationary
Remember to normalize the eigenvector — I didn’t…

Checks if p_50 and p_stationary are equal to tolerance 1e-5
Toolbox: np.random.rand, .dot(), np.linalg.eig, reductions, abs(), argmin, comparisons, all, np.linalg.norm, etc.

Solution: Python source file

[Contenidos](../Contenidos.md) \| [Anterior (6 Complejidad de algoritmos)](06_Complejidad.md) \| [Próximo (8 Cierre)](08_Cierre.md)

