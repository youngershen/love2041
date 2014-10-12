#!/usr/bin/perl

package Zentemplate;
sub new
{
    
    #my $params = @_;
    #print $params;
    my $class = @_[0];
    my $self = {};
    $self->{"_template_name"} = @_[1];
    $self->{"_template_context"} = @_[2];
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

sub render_to_html
{
    
}

1;
