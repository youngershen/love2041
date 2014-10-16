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

print $html;
