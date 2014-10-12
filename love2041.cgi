#!/usr/bin/perl

use warnings;
use CGI;

use lib './libs';
use Zentemplate;

$query = new CGI;
@name = $query->param('name');
@age  = $query->param('age');
$template = new Zentemplate('index.html', { 'name' => 'younger', 'age' => '200'});
print $query->header();

print "my name is " . $template->get_template_name();

print "and i am " . $template->get_template_context()->{'age'}. "years old";

