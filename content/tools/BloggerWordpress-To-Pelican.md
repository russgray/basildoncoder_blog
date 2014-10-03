Title: Blogger/Wordpress to Pelican
Date: 2014-10-03 13:38
Author: Russell Gray
Slug: blogger-wordpress-to-pelican
Tgas: pelican, blogging, linklint, formd, powershell, nginx

Like all the cool kids these days, I've migrated my blog to use a static site
generator. [Pelican][1], in my case. There are lots of tutorials about this
sort of thing, but I ran into a few things that needed additional tweaking so
I'm documenting it here. Note this isn't exhaustive - you can find the basics
of generating and publishing static blogs in the pelican docs.

## Importing

Pelican will convert Wordpress xml exports, but not Blogger. No problem -
there are Blogger to Wordpress converters available, so get your data into
Wordpress export format. I used [this one][2]. Save the XML file in an export
directory off the root of your directory layout, it can be a useful reference
later.

## Comments

I used [Brian St Pierre's][3] [comments plugin][4] to extract comments from my
Wordpress export. I had to patch it to work with pelican 3.4, but my patch has
now been pulled into the main code so it works fine.

## Links

When using markdown I prefer to use reference-style links (where all the
actual URLs are stored as footnotes at the end of the file). The initial
import process creates inline links though, so I wanted to fix that.

### Local links

Check your page interlinks to make sure the import process picked them up
correctly. If not, edit them yourself to the following format:

	[my link text][5]

Note the `{filename}` macro - that's what pelican will use to generate your
links in the final html.

### Converting to reflinks

There's a nifty project called [formd][6] that can convert markdown links to
inline or reference, or toggle between them.

	:::bash
	for FILE in $(find content -type f -not -path "content/comments/*" -iname '*.md')
	do 
		formd -r < "$FILE" | sponge "$FILE"
	done

Note the use of sponge to allow me to overwrite the original file with the
reformatted one without needing an intermediate file. Get it with `apt-get
install moreutils`.

This is so useful I made it a fabric task:

	:::python
	def reflinks(f):
    	local('formd -r < {0} | sponge {0}'.format(f))

Then I can reprocess any file quickly like so:

	:::bash
	fab reflinks:content/My-Blog-Post.md

### Validating

Somewhere in the process of converting content to markdown and links to
references, sometimes links get garbled. Especially if they have characters
that clash with markdown formatting, like parentheses and square brackets.
There is an excellent, ancient tool called linklint written in perl (see,
ancient) that can blast through your content, identify links, and hit them up
to make sure they exist. It even follows redirects.

	:::bash
	linklint -quiet -no_anchors -doc linkdoc -root output -net /@

This also verifies local links, so it double checks the work pelican has done.
It will generate a fairly spartan but very useful report in the linkdoc
directory.

## Redirects

Pelican will generate your output in a flat structure, rather than the
year/month/day URL structure used by other blogging software. All *your* links
will be correct, but incoming links from other sites will break which will
devastate your ranking.

Fortunately you can configure your webserver to issue permanent redirects to
keep those links alive.

First get a list of your old URLs from your export dump. I used powershell for
this because I love how it handles XML, but use any tool you like.

	:::powershell
	[xml] $content = get-content export/wordpress.xml
	$content.SelectNodes("//link") > export/oldurls.txt

Next, construct your redirect rules on your webserver. In my case, I was
moving everything from a subdomain to a directory, i.e.
`blog.basildoncoder.com` to `basildoncoder.com/blog`, as well as the
aforementioned URL change. So I have nginx rules like this:

	server {
		server_name blog.basildoncoder.com;
		return 301 $scheme://basildoncoder.com/blog$request_uri;
	}

That redirects all requests off of the blog subdomain. Then, in the main
server block for basildoncoder.com, I have this rule:

	location ~ "^/blog/((\d{2,4})/){1,3}" {
		rewrite "^/blog/((\d{2,4})/){1,3}(.*)$" /blog/$3 permanent;
	}

The regex there looks for between 1 and 3 occurrences of directories named
with between 2 and 4 numbers, and captures the rest of the URL after it. So
any of the following URLs will match, and capture the filename:

	/blog/2014/09/30/test.html
	/blog/2014/09/test.html
	/blog/2014/test.html

Each of these will be permanently rewritten to `/blog/test.html`.

Finally, bust out linklint again to check the old URLs all resolve correctly
once the pages are deployed and the server configured:

	:::bash
	linklint @@oldurls.txt

You'll get output like this:

	found  44 urls: ok
	-----  88 urls: moved permanently (301)

	Linklint checked 44 urls:
   		44 were ok, 0 failed. 88 urls moved.

(In this case there were twice as many moves as there are links because I
(redirect the subdomain then redirect the path.)


[1]: http://docs.getpelican.com/en/3.4.0/
[2]: http://blogger2wordpress.appspot.com
[3]: http://blog.bstpierre.org/
[4]: https://github.com/bstpierre/pelican-comments
[5]: {filename}/path/to/blog-post.md
[6]: https://drbunsen.github.io/formd/