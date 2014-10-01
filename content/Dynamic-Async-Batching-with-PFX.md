Title: Dynamic Async Batching with PFX
Date: 2008-08-08 17:41
Author: Russell Gray
Slug: Dynamic-Async-Batching-with-PFX

The [PFX Team blog][1] has been
posting some excellent articles recently on the subject of [task
batching][2]
using the June 2008 CTP release of the Task Parallel Library. It's
really cool to see some of these techniques abstracted properly in .Net,
and I hope it eventually becomes part of the core libraries.

I've been playing around a bit recently with the June CTP in the context
of batching up web service calls, as that's something I do quite a lot.
One particular problem that comes up occasionally is a two-stage series
of requests to download a complete set of paged data. I might do this if
I wanted to download an entire discussion thread, for instance, or a
large account statement from my online bank.

Typically in this situation the web service will limit the number of
records I can retrieve in one request, and allow me to specify start and
count parameters to the request. The response will also include a total
record count, so I know how much data there is.

The normal use case for this is to request the first page of data, and
use the total record count to display a list of page links that my user
can click on to navigate the data or jump to any page. In my case,
however, I want ALL the data as quickly as possible.

So, imagine a situation where I am using a service that lets me download
a maximum of 200 records per request. My first step is to request the
maximum 200 records starting from index 0, i.e. the first page of data.
In the response will be a total record count - if that number is equal
to the number of records I got back (i.e. <= 200) I've got everything in
one hit and can stop. But what if the total record count is, say, 1000?
I need to make four more requests (since I've already got records 1-200,
I have 800 more to get in batches of 200 each).

Naturally I want to do this asynchronously, using as few resources as I
can. This means all webservice calls should be using the APM pattern
(thus using IO completion ports, and not consuming worker threads from
the thread pool or creating my own threads) and, preferably, not
blocking anywhere except when I actually need some data before
continuing.

The two-stage process can be successfully captured asynchronously by
combining a future and a continuation. I encapsulate the initial request
in a Future object (which is a subclass of Task), and handle the
check-record-count-and-get-more-records-if-required logic in the
continuation. The code for this basically looks as follows:

    :::csharp
    public Future<List<Item>> GetAllItemsAsync()
    {
        var f = Create<GetItemsResponse>(
                ac => Service.BeginGetItems(0, ac, null),
                Service.EndGetItems);

        var start = 200;
        var resultFuture = f.ContinueWith(
            r => { /* Batch retrieval here... */});
        return resultFuture;
    }

In order to support the APM pattern neatly, I'm using the following
method [from the PFX
blog][3]:

    :::csharp
    private static Future<T> Create<T>(
            Action<AsyncCallback> beginFunc,
            Func<IAsyncResult, T> endFunc)
    {
        var f = Future<T>.Create();
        beginFunc(iar =>
            {
                try
                {
                    f.Value = endFunc(iar);
                }
                catch (Exception e)
                {
                    f.Exception = e;
                }
            });
        return f;
    }

This could be coded as an extension method, though I haven't bothered
yet as I'm hopeful this immensely useful snippet will be integrated into
the library itself.

Now I need to make a number of calls to get the rest of the data, so I
loop until I've made the required number of async service calls:

    :::csharp
    var resultFuture = f.ContinueWith(r =>
        {
            var items = new ConcurrentQueue<Item>();
            var handles = new List<WaitHandle>();

            while (start < r.Value.TotalRecordCount)
            {
                var asyncResult = Service.BeginGetItems(200,
                    ar => Service.EndGetItems(ar).Items
                        .ForEach(items.Enqueue), null);

                handles.Add(asyncResult.AsyncWaitHandle);
                start += 200;
            }

            handles.ForEach(h => h.WaitOne());
            return items.ToList();
        });

I'm about 85% happy with this as an approach. I'm not completely happy,
however, because of the WaitOne calls, which mean that I'm blocking on a
threadpool thread until all the calls complete. Given that this is all
wrapped up in a future, I may not actually need to access the data until
well after the calls have completed, in which case I am wastefully
consuming a threadpool thread for some period of time. So the $64,000
question is, how do I get rid of it? I'm sure there's a way to do it,
but my brain has gone on a protest march about all the time I'm forcing
it to spend thinking about this stuff.


[1]: http://blogs.msdn.com/pfxteam/default.aspx
[2]: http://blogs.msdn.com/pfxteam/archive/2008/08/05/8835612.aspx
[3]: http://blogs.msdn.com/pfxteam/archive/2008/03/16/8272833.aspx