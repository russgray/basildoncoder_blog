post_id: Project-Euler-Problem-5
Author: Loocie
Date: 2008-07-02 06:58:48
Author_Email: noreply@blogger.com
Author_IP: None

Hi russ, thanks for your reply. Here is my login code:

    :::csharp
    BFGlobalService bfGlobal = new BFGlobalService();
    LoginReq request = new LoginReq();
    LoginResp resp;
    request.username = username;
    request.password = password;
    request.productId = 82;
    request.vendorSoftwareId = 0;
    request.locationId = 0;
    request.ipAddress = 0;
    resp = bfGlobal.login(request);

The object 'resp' has an attribute called 'header' and this is null. This
header object should contain a sessionToken. When using this code I can see
'Logon successfull' at betfair.com (under Account -> Security). Maybe you have
an idea. This code works when using in a dektop application, but not in
Windows Mobile 6.

All the best, Loocie
