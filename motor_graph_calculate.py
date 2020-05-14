# -*- coding: utf-8 -*-
import numpy as np

def uniform_linear_motion(v0, t0, t1, x0, steps, decimals=4):
    t = np.round( np.linspace(t0, t1, steps), decimals)
    t_tmp = np.round( np.linspace(0, t1-t0, steps), decimals)
    a = np.round( np.zeros(steps), decimals)
    v = np.round( np.full(steps, v0), decimals)
    x = np.round( v0 * t_tmp + x0, decimals)
    return t, a, v, x

def trapezoid_accelerated_motion(v0, t0, t1, x0, acceleration, steps, decimals=4):
    t = np.round( np.linspace(t0, t1, steps), decimals)
    t_tmp = t - t[0]

    # calculate acceleration
    a = np.round( np.full(steps, acceleration), decimals)

    # calculate velocity
    v1 = v0 + acceleration * (t1 - t0)
    v = np.round( np.linspace(v0, v1, steps), decimals)

    # calculate distance
    x = np.round( v0 * t_tmp + 0.5 * a * t_tmp ** 2 + x0, decimals)

    return t, a, v, x

def triangle_accelerated_motion(v0, t0, t1, x0, acceleration, steps, decimals=4):
    t = np.round( np.linspace(t0, t1, steps), decimals)
    t_shifted = np.insert(t[:-1], 0, t[0])
    dt = t - t_shifted

    split_index = int( len(dt) / 2 )
    if not len(dt) % 2 == 0:
        split_index += 1
    
    # calculate acceleration
    t_splited = t[ : split_index ] - t[0]
    a1 = t_splited * acceleration / t_splited[-1]
    a = np.round( np.concatenate( [ a1, a1[ ::-1 ][ split_index-int( len(dt) / 2 ): ] ] ), decimals)

    # calculate velocity
    a_shifted = np.insert(a[:-1], 0, a[0])
    v = dt * (a + a_shifted) / 2.0
    v = np.round( np.cumsum(v) + v0, decimals)

    # calculate distance
    v_shifted = np.insert(v[:-1], 0, v[0])
    x = dt * (v + v_shifted) / 2.0
    x = np.round( np.cumsum(x) + x0, decimals)

    return t, a, v, x

def triangle(acceleration, v_max, distance, step, decimals=4, v0=0):
    t_tmp = v_max / acceleration * 2.0
    x = t_tmp * v_max / 2.0

    if x > distance / 2.0:
        t_tmp = round( distance / v_max, decimals )
        
        # acceleration
        t1, a1, v1, x1 = triangle_accelerated_motion(0.0, 0.0, t_tmp, 0.0, acceleration, step, decimals)
        
        # deceleration
        t2, a2, v2, x2 = triangle_accelerated_motion(v1[-1], t1[-1], t1[-1] + t1[-1], x1[-1], -1.0*acceleration, step, decimals)

        t, a, v, x = [t1, t2], [a1, a2], [v1, v2], [x1, x2]

    else:
        # acceleration
        t1, a1, v1, x1 = triangle_accelerated_motion(0.0, 0.0, t_tmp, 0.0, acceleration, step, decimals)
        
        # constant velocity
        t1_tmp = round( (distance - x1[-1] * 2) / v_max + t1[-1], decimals )
        t2, a2, v2, x2 = uniform_linear_motion(v_max, t1[-1], t1_tmp, x1[-1], step)

        # deceleration
        t3, a3, v3, x3 = triangle_accelerated_motion(v_max, t2[-1], t2[-1] + t1[-1], x2[-1], -1.0*acceleration, step, decimals)

        t, a, v, x = [t1, t2, t3], [a1, a2, a3], [v1, v2, v3], [x1, x2, x3]
    
    return t, a, v, x

def trapezoid(acceleration, v_max, distance, step, decimals=4, v0=0):
    t_tmp = v_max / acceleration
    x = t_tmp * v_max / 2.0

    if x > distance / 2.0:
        v_tmp = (distance / acceleration) ** 0.5
        t_tmp = v_tmp / acceleration
        
        # acceleration
        t1, a1, v1, x1 = trapezoid_accelerated_motion(0.0, 0.0, t_tmp, 0.0, acceleration, step, decimals)
        
        # deceleration
        t2, a2, v2, x2 = trapezoid_accelerated_motion(v1[-1], t1[-1], t1[-1] + t1[-1], x1[-1], -1.0*acceleration, step, decimals)

        t, a, v, x = [t1, t2], [a1, a2], [v1, v2], [x1, x2]

    else:
        # acceleration
        t1, a1, v1, x1 = trapezoid_accelerated_motion(0.0, 0.0, t_tmp, 0.0, acceleration, step, decimals)
        
        # constant velocity
        t1_tmp = round( (distance - x1[-1] * 2) / v_max + t1[-1], decimals )
        t2, a2, v2, x2 = uniform_linear_motion(v_max, t1[-1], t1_tmp, x1[-1], step, decimals)

        # deceleration
        t3, a3, v3, x3 = trapezoid_accelerated_motion(v_max, t2[-1], t2[-1] + t1[-1], x2[-1], -1.0*acceleration, step, decimals)

        t, a, v, x = [t1, t2, t3], [a1, a2, a3], [v1, v2, v3], [x1, x2, x3]
    
    return t, a, v, x

def motor_graph_calculate(acceleration, v_max, distance, step, decimals=4, v0=0, acceleration_type='trapezoid'):

    if acceleration_type == 'trapezoid':
        return trapezoid(acceleration, v_max, distance, step, decimals, v0)
    elif acceleration_type == 'triangle':
        return triangle(acceleration, v_max, distance, step, decimals, v0)
    else:
        return trapezoid(acceleration, v_max, distance, step, decimals, v0)

def main():
    t, a, v, x = motor_graph_calculate(10.0, 1.0, 0.35, 10)
    
    print('t', t)
    print('a', a)
    print('v', v)
    print('x', x)

if __name__ == '__main__':
    main()