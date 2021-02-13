def step_info(t, yout):
    print(f"Max Amp: {max(yout)}")
    print("OS: %f%s" % ((yout.max() / yout[-1] - 1) * 100, '%'))
    print("Tr: %fs" % (t[next(i for i in range(0, len(yout) - 1) if yout[i] > yout[-1] * .90)] - t[0]))
    print("Ts: %fs" % (t[next(len(yout) - i for i in range(2, len(yout) - 1) if abs(yout[-i] / yout[-1]) > 1.02)] - t[0]))


def step_info_return(t, yout):
    max_amp = max(yout)
    overshoot = (yout.max() / yout[-1] - 1) * 100
    rise_time = t[next(i for i in range(0, len(yout) - 1) if yout[i] > yout[-1] * .90)] - t[0]
    settling_time = t[next(len(yout) - i for i in range(2, len(yout) - 1) if abs(yout[-i] / yout[-1]) > 1.02)] - t[0]
    return [max_amp, overshoot, rise_time, settling_time]
