#!/usr/bin/perl
package Zentemplate;
use lib './';
use Config;
sub new
{
    
    my $params = @_;
    my $class = @_[0];
    my $self = {};
    self->{"_template_name"} = @_[1];
    $self->{"_template_context"} = @_[2];
    $self->{"config"} = {'template_dir' => './../template/'};#new Config;
    bless $self, $class;
    return $self;
}

sub get_template_name
{
    my ($self) = @_;
    return $self->{"_template_name"};
}
sub get_template_context
{
    my($self) = @_;
    return $self->{"_template_context"};
}

sub get_html
{
    
    my($self, $file) = @_;
    $line = "";
    if(open(MYFILE, "./index.html")){

        return "open";
    }else{

        return "close";
    }
}

sub render_to_html
{
    return "";
}

1;
