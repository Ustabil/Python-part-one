# template for "Stopwatch: The Game"
import simplegui
# define global variables

interval = 100
stopwatch = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
	minutes = t % 600
    tenths = t % 10
    seconds = (t - (tenths)) / 10

    if seconds < 10 :
    	return minutes + ":0" + str(seconds) + "." + str(tenths)
    if seconds >= 10:
    	return minutes + ":" + str(seconds) + "." + str(tenths)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_handler():
	timer.start()
def stop_button_handler():
	timer.stop()
def reset_button_handler():
	global stopwatch
	timer.stop()
	stopwatch = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
	global stopwatch
	stopwatch += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(str(format(stopwatch)), (200, 220), 36, 'Red')
    
# create frame
frame = simplegui.create_frame('Stopwatch', 400, 400)

# register event handlers
timer = simplegui.create_timer(interval, timer_handler)
frame.set_draw_handler(draw_handler)
button1 = frame.add_button('Start', start_button_handler, 100)
button2 = frame.add_button('Stop', stop_button_handler, 100)
button3 = frame.add_button('Reset', reset_button_handler, 100)


# start frame
frame.start()

# Please remember to review the grading rubric
