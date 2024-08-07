# scpi controller
import easy_scpi as scpi

class PowerSupply( scpi.Instrument ):
    
    def __init__( self ):
        super().__init__( 
            port = None, 
            timeout = 5,
            read_termination = '\n', 
            write_termination = '\n' 
        )

        # other initialization code...

        
    #--- public methods ---

    
    @property        
    def voltage( self ):
        """
        Returns the voltage setting
        """
        return self.source.volt.level()
    
    
    @voltage.setter
    def voltage( self, volts ):
        """
        Sets the voltage of the instrument
        """
        self.source.volt.level( volts )
        
    
    @property
    def current( self ):
        """
        Returns the current setting in Amps
        """
        return self.source.current.level()
        
        
    @current.setter
    def current( self, amps ):
        """
        Set the current of the instrument
        """
        self.source.current.level( amps )
        
    
    def on( self ):
        """
        Turns the output on
        """
        self.output.state( 'on' )
        
        
    def off( self):
        """
        Turns the output off
        """
        self.output.state( 'off' )

