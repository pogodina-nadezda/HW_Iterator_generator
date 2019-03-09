def tracefunc(frame, event, arg):
    if event == 'return' and frame.f_code.co_name != '_ag':
        print("function: ", frame.f_code.co_name, ", local vars: ", list(dict.keys(frame.f_locals)))
    return tracefunc

def tracefoo(function_to_trace):
    import sys
    sys.settrace(tracefunc)
    function_to_trace()
