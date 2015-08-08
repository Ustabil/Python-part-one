# template for "Stopwatch: The Game"
import simplegui
# define global variables

interval = 100

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"


# define event handler for timer with 0.1 sec interval
def timer_handler():
	print ".1 sec!"
# define draw handler

    
# create frame


# register event handlers
timer = simplegui.create_timer(interval, timer_handler)

# start frame
timer.start()

# Please remember to review the grading rubric
