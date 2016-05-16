Title: PostgreSQL, JDBC, and Client Certificates
Date: 2015-03-30T16:12:56+01:00
Author: Russell Gray
Slug: postgresql-jdbc-client-certificates
Tags: coding, java, postgres, security

There is a distressing lack of info out there about configuring the postgresql JDBC driver to present a client certificate to a database server when using SSL. It appears that checking the *server* certificate works out of the box, but not the client certificate.

In this post I am using the following software versions:

* PostgreSQL 8.1 (yes, old, I know)
* postgresql-9.4-1200-jdbc41

If you are using different versions then results may vary, but this should be fairly widely-applicable.

The postgres [JDBC docs][1] hint that a custom SSLSocketFactory is required in order to establish an SSLContext instance that uses your client cert, but rather unhelpfully goes on to say they don't know how to do it:

> The Java SSL API is not very well known to the JDBC driver developers and we
> would be interested in any interesting and generally useful extensions that
> you have implemented using this mechanism. Specifically it would be nice to
> be able to provide client certificates to be validated by the server

Yes, it would be nice. And indeed, someone already has - but it seems to be woefully undocumented. In the org.postgresql.ssl.jdbc4 package we find the [LibPQFactory][2] class, which handles everything we need - and, in what I personally consider a bonus, works with .crt files directly rather than mucking about with keystores and the perenially stupid keytool.

By default, this class looks in `~/.postgresql/` for the files it needs to work, though you can override the location. You need a `root.crt` containing the CA for the server certificate, plus your client certificate (`postgresql.crt`) and private key (`postgresql.pk8`). 

Assuming you are using the default locations, you can test the basic connection using psql:

    :::bash
    psql "sslmode=verify-full host=<hostname> dbname=postgres user=<username>"

If all is well, you will be prompted for your password and a connection will be established. If not, things to look at include your postgres config (is there a `hostssl` line in `pg_hba.config` for your client host?) and your firewall.

Although psql has no trouble, the JDBC driver has format restrictions. The private key must be PKCS8 and stored in DER format, whereas the certificate is fine in PEM format (because of course it is). If your key is in PEM format (i.e. starts with something like `-----BEGIN PRIVATE KEY-----`) you can convert it with openssl:

    :::bash
     openssl pkcs8 -topk8 -inform PEM -outform DER -in postgresql.key -out postgresql.pk8 -nocrypt

Note that this creates an unencrypted key file; leave off the `-nocrypt` parameter if you want it encrypted, and specify the password at runtime.

Then, finally, specify your connection string like so:

    jdbc:postgresql://<hostname>/postgres?ssl=true&sslfactory=org.postgresql.ssl.jdbc4.LibPQFactory&sslmode=verify-full

Note the `sslmode` parameter - this is one of a number of parameters that control behaviour of the factory. The full list is in the source; the interesting ones include `sslcert`, `sslkey`, and `sslrootcert` (overrides the location/name of `root.crt`, `postgresql.crt` and `postgresql.pk8`); and `sslpassword` (decryption password if you encrypted your private key).


[1]: https://jdbc.postgresql.org/documentation/81/ssl-factory.html
[2]: https://github.com/pgjdbc/pgjdbc/blob/master/org/postgresql/ssl/jdbc4/LibPQFactory.java