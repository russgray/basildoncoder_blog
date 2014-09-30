Title: ConcurrentDictionary: GetOrAdd vs GetOrAdd - One Of These Things Is Not Like The Other
Date: 2014-01-13 18:00
Author: Russell Gray
Slug: ConcurrentDictionary-GetOrAdd-vs-GetOrAdd-One-Of-These-Things-Is-Not-Like-The-Other
Tags: .net, coding

Some recent performance profiling of a server application under load turned up
an interesting gotcha in .Net's ConcurrentDictionary that I think is well-
worth knowing about.

As you probably know, ConcurrentDictionary strives for performance in
concurrent environments by using more sophisticated locking strategies than
simply `lock(this)`. Briefly, it has a lock per bucket, which means that
parallel writes are possible where the updates are in different buckets. A few
operations acquire all locks, which obviously is a source of contention, but
typically these are operations like Count and IsEmpty that shouldn't be called
frequently. Finally, and of most relevance to this post, it supports lock-free
reads which are the holy grail for high-concurrency. Except when it doesn't.

ConcurrentDictionary has two overloads of the GetOrAdd method, an atomic
operation to get a value if it exists, or add it if not. In the case where the
value does not exist, you can either provide the new value directly, or pass a
factory delegate that ConcurrentDictionary will call if it needs the value.
The Remarks section in the [MSDN docs](http://msdn.microsoft.com/en-
us/library/dd287191(v=vs.110).aspx) warns that the factory delegate will be
called outside the lock, but otherwise the two overloads appear identical
functionally - in particular that "read operations on the dictionary are
performed in a lock-free manner".

This is not true, however, at least as of .Net 4.5. The factory delegate
overload will call the lockless TryGetValue and only attempt to do an Add
(thus acquiring a lock) if the read fails - this is sane and how I would
expect it to be implemented. The non-delegate overload of GetOrAdd, however,
does not call TryGetValue and will obtain the bucket lock *before* it attempts
to read the key, meaning that it is no longer a lockless read!

If you have lots of threads attempting to read from a ConcurrentDictionary
with a small number of keys, you'll get massive lock contention with this
method. Frankly I think this should be considered a bug since in a highly-
concurrent environment this is a fundamental difference in behaviour for two
methods which should be near-identical.

I won't post any code here because I don't want to get into any licencing
issues, but if you have Resharper or dotPeek you can easily decompile the
framework and verify this behaviour yourself.
