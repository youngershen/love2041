#!/usr/bin/perl  

use CGI;
$request = CGI->new;

print $request->header,
    $request->start_html('hello world'),
    $request->h1("helloworld"),
    $request->end_html;

foreach(sort keys %ENV)
{
        print "<b>$_</b> : $ENV{$_} </br>";
}

1;
