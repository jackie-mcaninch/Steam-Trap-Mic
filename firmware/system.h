#ifndef _SYSTEM_H_
#define _SYSTEM_H_
#include "common.h"

class CSystem
{
public:

    void    init();

    //  soft reboots the system
    void    reboot();

    // Places the interface mode in either manual mode or setpoint mode
    void    return_to_run_mode();

    // changes system orientation
    void    rotate();

    // set system-wide orientation
    void    set_orientation(bool orientation);


    // The most recently read frequency from the mic
    float   frequency;

    // Unique System ID
    uint8_t uid[8];

    // error byte that indicates errors with each bit. 0x00 indicates all systems are good
    uint8_t error_byte;
};

#endif
