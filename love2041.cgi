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
use lib './libs';
use Config;


$configuration = Config::new;
$query = new CGI;
$template = new Zentemplate('index.html', { 'name' => 'younger', 'age' => '200'});
$html = $template->get_html();

print $query->header();

<<<<<<< HEAD
print $html;
=======
>>>>>>> e66406e4a68e966674391e06fe81c45724a83450
>>>>>>> cf45f2ae82974e4b6c53c893b6b08467b56e62ea
