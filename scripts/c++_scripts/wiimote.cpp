
#include <xwiimote.h>
#include <iostream>
#include <cstring>

#include <ncurses.h>
#include <stdlib.h>
#include <unistd.h>


int main(){
    struct xwii_monitor* mon;
    char* path;
    
    mon = xwii_monitor_new(false, false);
    path = xwii_monitor_poll(mon);
    xwii_monitor_unref(mon);
    
    
    struct xwii_iface* iface;
    int ret = xwii_iface_new(&iface, path);
    std::free(path);
    ret = xwii_iface_open(iface, xwii_iface_available(iface) | XWII_IFACE_WRITABLE);
    ret = xwii_iface_watch(iface, true);
    
    
    initscr();
    cbreak();
    noecho();
    clear();
    
    
    while(true){
        struct xwii_event event;
        
        ret = xwii_iface_dispatch(iface, &event, sizeof(event));
        
        switch(event.type){
            case XWII_EVENT_KEY:
                if (event.v.key.state)
                    mvaddch(1,1,'B');
                else
                    mvaddch(1,1,'_');
                break;
            case XWII_EVENT_ACCEL:
                mvprintw(1,4,"%d", event.v.abs[0].x);
                mvprintw(1,13,"%d", event.v.abs[0].y);
                mvprintw(1,22,"%d", event.v.abs[0].z);
                break;
            case XWII_EVENT_MOTION_PLUS:
                mvprintw(2,4,"%d", event.v.abs[0].x);
                mvprintw(2,13,"%d", event.v.abs[0].y);
                mvprintw(2,22,"%d", event.v.abs[0].z);
                break;
            case XWII_EVENT_WATCH:
                //std::cout<<"watch\n";
                break;
            case XWII_EVENT_GONE:
                //std::cout<<"gone\n";
                break;
            
        }
        refresh();
        usleep(16700);
        
    }
    return 1;
    
}
