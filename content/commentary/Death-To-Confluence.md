Title: Death To Confluence
Date: 2014-12-05T13:36:26
Author: Russell Gray
Slug: death-to-confluence
Tags: rants

Way back in 2011, Atlassian made the somewhat surprising decision not to let you edit wiki markup in their wiki product, Confluence. Allegedly this was because [people like 'sales and marketing' were too stupid to learn wiki syntax][1], and it was too hard to support both a rich text editor and a markup editor.

This might be tolerable if the rich text editor were any good, but 3 years after declaring "We know it's not perfect, *yet*" it's still in this weird mutant state where you can type markup syntax into the editor, but it is instantly and irretrievably converted and then [you can't edit it][2].

> **Note: You cannot edit content in wiki markup**. Confluence does not store page content in wiki markup. Although you can enter wiki markup into the editor, Confluence will convert it to the rich text editor format immediately. *You will not be able to edit the wiki markup after initial entry*.

Huh? So, when I'm writing up a page that e.g. refers to a sproc or class name I tend to mark it up as preformatted text, as is conventional to denote code. I can type this in as {{my_sproc_name}} and it correctly gets converted to `my_sproc_name`. But, it's immediately and permanently converted. If I do something so stupid as to finish a paragraph with preformatted text and later want to go back and add something to the end in normal text, Confluence 'helpfully' thinks I want to continue writing in the preformatted block and I have to jump through hoops by rewriting the line and applying formatting again afterwards, or starting a new line in normal body text then deleting the line-break, etc.

Who thought this was a good idea?


[1]: http://blogs.atlassian.com/2011/11/why-we-removed-wiki-markup-editor-in-confluence-4/
[2]: https://confluence.atlassian.com/display/DOC/Confluence+Wiki+Markup