Grappling With C: Part 1 🏋️ 
####################################

:date: 2023-03-18 07:47
:modified: 2023-03-18 07:47 
:tags: c, language
:category: Rants
:slug: grappling-with-c
:authors: Ishaan Arora
:summary: The tales of my struggle with C

Context
****************
I want to learn C, for several reasons:

- it's the granddaddy of all languages
- I need a compiled language in my repertoire
- in the short time that I've used it, it feels really simple
- flexing rights

I am all too well aware of the new hotness - Rust/Go. I am sure both of these are excellent languages, each with its unique ecosystem of features, communities, and goals. But there's a *back to the roots* feeling with C.
Somewhere in my mind, I feel that C is still important if you want to know what the heck is going in your computer.

Progress until now
***********************
I've just started learning C **seriously**. By seriously, I mean I am reading a book about it...

I was surprised that there is a notion of an object in C! It's a somewhat different notion - it's **storage** that can represent a value.

.. code:: c

   int x = 5;

When I look at the above statement, in my mind ``x`` is a variable of type ``int``, that is assigned the value ``5``.
So, where is the object in this? ``x``, ``5``, ``int``, ``=``? (Ok, ``=`` couldn't have possibly been the answer, but just for completeness...)
If you're coming from an object oriented language, you might be inclined to give ``x`` as the answer. I don't blame you. This is somewhat confusing.

To give you a mental picture of this - ``x`` is the identifier, what you call a variable, that references some memory where ``5`` is stored. That memory - which stores that ``5`` - *is* the object.

::
    
             ┌─────┐
     x  -->  │  5  │ Some memory, say 4 bytes, say starting at 0x2affffff
     |       └─────┘
   ┌───┐        ^
   │int│        |
   └───┘    the object
    

This definition of an object seems to be artificial at first, not the thing you would think as the normal person. But believe me, this definition helps in understanding a few things that I am going to talk about below.

Thing #1 : Object = storage + type
----------------------------------------------------------------------------
Think of the memory in your computer as a sequence of raw bits, with no inherent meaning.

To expand on the above example [#endianness]_ :

::

             ┌────────────────────────────────┐
    x  -->   │00000000000000000000000000000101│
    |        └────────────────────────────────┘
  ┌───┐
  │int│
  └───┘
           Same memory view but a little zommed in

What gives meaning to these bits is the ``type`` of the object. And this type is not set in stone, it depends on the *variable* you are using to reference this object.

It's as if the variable *stamped* its type on the object:

::

             ┌────────────────────────────────┐
    x  -->   │00000000000000000000000000000101│
    |        └────────────────────────────────┘
  ┌───┐                    ∘---∘
  │int│                    |int|
  └───┘                    ∘---∘

Now, normally you wouldn't want to change the type of an object like I am going to do now. An ``int`` is supposed to be accessed as an ``int``.
C being the tool it is, allows you to shoot yourself in the foot and then let you drown in the shame of your incompetence. You can do this for example:


.. code:: c

   #include <stdio.h>

    int main(){
        long val = 478560413032L;
        char *c = &val;
        for (int i = 0; i < sizeof(long); i++, c++){
            printf("%c\n", *c);
        }
    }

The above code accessed an object that was supposed to be accessed as ``long int`` like a ``char`` array.

On my system [#endianness]_ [#architecture]_ this code prints (``↵`` indicates a newline):

::
    
    h↵
    e↵ 
    l↵ 
    l↵ 
    o↵ 
    ↵
    ↵
    ↵

You are accessing the same object - the same underlying storage - but you are interpreting it differently based on the type of the variable you are using to reference it.

This is different from a type cast:

.. code:: c

   #include <stdio.h>

    int main(){
        int x = 5;
        float f = x; // An implicit type cast
        printf("%d, %f\n", x, f);
    }

In this code, we are not sharing the same underlying object. For the ``float`` variable ``f``, c creates a new object whose internal representation is apt for that type. In this case *a copy* of ``5`` would be converted to the `IEEE 754 <https://en.wikipedia.org/wiki/IEEE_754>`_ format for floating-point and stored in a *new* object just for ``f``.

To drive home this fact, we go back to our earlier example:
::

             ┌────────────────────────────────┐
    x  -->   │00000000000000000000000000000101│ = 5
    |        └────────────────────────────────┘
  ┌───┐
  │int│
  └───┘

If we just copied the value as is and just slapped on the type `float` onto ``f``, the situation would look like:

::

             ┌────────────────────────────────┐
    f  -->   │00000000000000000000000000000101│ = 7.00649232162e-45 !!! Not what you want
    |        └────────────────────────────────┘
  ┌─────┐
  │float│
  └─────┘

This is wrong, very wrong ❌

The reason for this is that ``int`` s and ``float`` s are stored differently internally. 

What you actually want is this:
::

             ┌────────────────────────────────┐
    f  -->   │01000000101000000000000000000000│ = 5 ✅
    |        └────────────────────────────────┘
  ┌─────┐
  │float│
  └─────┘

You need that conversion from ``int`` to ``float``. c does that for you.



Sidenotes
**********
Here is the little Python program I used to generate the number ``478560413032``

.. code:: python

    message = "hello"
    _representation = reversed(list(f"{ord(char):08b}" for char in message)) # ['01101111', '01101100', '01101100', '01100101', '01101000']
    bits = ''.join(_representation) #'0110111101101100011011000110010101101000' 
    magic_number = int(bits, base=2)
    print(magic_number)


Also note that I've discounted a lot of what people refer to as *implementation details* in this post. For example, the sizes of various types - ``int``, ``float``, ``double`` are implementation defined.
You can find the maximum[and minimum] values representable for each of these types in one of the ``limits.h`` header file supplied by the implementation. From that you could calculate the sizes of these types.

Due to these differences, the examples here might give you different results, some might issue warnings, some might not even compile.

But! when has that ever stopped a precocious programmer. So go on and compile, ``c`` you again! 🏎️👪

..  rubric:: **Footnotes**
.. [#endianness] I won't go into the endianness issue in my representation. Depending on your architecture, it's quite possible that these 4 bytes (32 bits) are stored in the reverse order. `<http://david.carybros.com/html/endian_faq.html>`_ for more information on this.
.. [#architecture] 
   .. code :: sh
        
        $ gcc -v

        Using built-in specs.
        COLLECT_GCC=gcc
        COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/11/lto-wrapper
        OFFLOAD_TARGET_NAMES=nvptx-none:amdgcn-amdhsa
        OFFLOAD_TARGET_DEFAULT=1
        Target: x86_64-linux-gnu
        Configured with: ../src/configure -v --with-pkgversion='Ubuntu 11.3.0-1ubuntu1~22.04' --with-bugurl=file:///usr/share/doc/gcc-11/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++,m2 --prefix=/usr --with-gcc-major-version-only --program-suffix=-11 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --enable-bootstrap --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-plugin --enable-default-pie --with-system-zlib --enable-libphobos-checking=release --with-target-system-zlib=auto --enable-objc-gc=auto --enable-multiarch --disable-werror --enable-cet --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none=/build/gcc-11-xKiWfi/gcc-11-11.3.0/debian/tmp-nvptx/usr,amdgcn-amdhsa=/build/gcc-11-xKiWfi/gcc-11-11.3.0/debian/tmp-gcn/usr --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu --with-build-config=bootstrap-lto-lean --enable-link-serialization=2
        Thread model: posix
        Supported LTO compression algorithms: zlib zstd
        gcc version 11.3.0 (Ubuntu 11.3.0-1ubuntu1~22.04) 
