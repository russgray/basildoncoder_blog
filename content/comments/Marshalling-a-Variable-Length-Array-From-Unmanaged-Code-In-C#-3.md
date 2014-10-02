post_id: Marshalling-a-Variable-Length-Array-From-Unmanaged-Code-In-CSharp
Author: Tratcher
Date: 2009-12-22 22:48:42
Author_Email: noreply@blogger.com
Author_IP: None

Very Helpfull, thanks.

I will note that this:

    ptr = new IntPtr(ptr.ToInt32() + sizeof (uint)); // move to first

should be:

    ptr = new IntPtr(ptr.ToInt32() + IntPtr.Size); // move to first

And `PtrToStringAnsi` should be `PtrToStringAuto`.

This handles padding issues on 64bit OS's.
