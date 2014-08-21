post_id: Marshalling-a-Variable-Length-Array-From-Unmanaged-Code-In-C#
Author: Tratcher
Date: 2009-12-22 22:48:42
Author_Email: noreply@blogger.com
Author_IP: None

Very Helpfull, thanks.<br /><br />I will note that this:<br />ptr = new IntPtr(ptr.ToInt32() + sizeof (uint)); // move to first<br />should be:<br />ptr = new IntPtr(ptr.ToInt32() + IntPtr.Size); // move to first<br /><br />And PtrToStringAnsi should be PtrToStringAuto.<br /><br />This handles padding issues on 64bit OS&#39;s.
