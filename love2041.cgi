<<<<<<< HEAD
#!/usr/bin/env python
import os
import cgitb
from lib.dataparser import DataParser
from lib.template import TEngine
from lib.config import HTML_HEADER
from lib.helper import make_walk_data_list
from lib.helper import make_person_content
from lib.helper import show_header

DATAINFO = make_walk_data_list()
cgitb.enable()
show_header()
print make_person_content(DATAINFO)
=======
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

>>>>>>> e66406e4a68e966674391e06fe81c45724a83450
