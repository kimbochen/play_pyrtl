import pyrtl


a = pyrtl.Input(8, 'a')
b = pyrtl.Input(8, 'b')
q = pyrtl.Output(8, 'q')
gt5 = pyrtl.Output(1, 'gt5')

q <<= a + b
gt5 <<= (a + b > 5)

sim = pyrtl.Simulation()
sim.step_multiple({'a': list(range(5)), 'b': [2, 2, 3, 3, 4]})
sim.tracer.render_trace()
