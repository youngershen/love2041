#!/usr/bin/perl
package Config;
sub new
{
    my $class;# = @_[0];
    my $self; #= {};
    
    #self->{"template_dir"} = "./../template/";
    bless $self, $class;
    return $self;
}
