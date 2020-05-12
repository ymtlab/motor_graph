# -*- coding: utf-8 -*-
import numpy as np

def uniformly_accelerated_motion(v0, t0, t1, x0, acceleration, steps, decimals=4):
    t = np.round( np.linspace(t0, t1, steps), decimals)
    t_tmp = np.round( np.linspace(0, t1-t0, steps), decimals)
    a = np.round( np.full(steps, acceleration), decimals)
    v = np.round( v0 + a * t_tmp, decimals)
    x = np.round( v0 * t_tmp + 0.5 * a * t_tmp ** 2 + x0, decimals)
    return t, a, v, x

def uniform_linear_motion(v0, t0, t1, x0, steps, decimals=4):
    t = np.round( np.linspace(t0, t1, steps), decimals)
    t_tmp = np.round( np.linspace(0, t1-t0, steps), decimals)
    a = np.round( np.zeros(steps), decimals)
    v = np.round( np.full(steps, v0), decimals)
    x = np.round( v0 * t_tmp + x0, decimals)
    return t, a, v, x

def motor_graph_calculate(acceleration, v_max, distance, step, decimals=4, v0=0):

    # v**2 - v0**2 = 2as   ->   v**2 = 2as - v0**2   ->   v = (2as - v0**2) ** 0.5
    v_tmp = (2.0*acceleration*(distance / 2.0) - v0**2.0) ** 0.5

    if v_tmp <= v_max:
        # 三角駆動
        t_tmp = round( (v_tmp - v0) / acceleration, decimals )
        
        # 加速
        t1, a1, v1, x1 = uniformly_accelerated_motion(0.0, 0.0, t_tmp, 0.0, acceleration, step, decimals)
        
        # 減速
        t2, a2, v2, x2 = uniformly_accelerated_motion(v_tmp, t1[-1], t1[-1] + t1[-1], x1[-1], -1.0*acceleration, step, decimals)

        t = [ t1, t2 ]
        a = [ a1, a2 ]
        v = [ v1, v2 ]
        x = [ x1, x2 ]

    else:
        # 台形駆動
        t_tmp = round( (v_max - v0) / acceleration, decimals )

        # 加速
        t1, a1, v1, x1 = uniformly_accelerated_motion(
            v0=0.0, t0=0.0, t1=t_tmp, x0=0.0, acceleration=acceleration, steps=step
        )
        
        # 等速
        # x=at   ->   t=x/a   ->   (distance - x1[-1] * 2) / v_max
        t1_tmp = round( (distance - x1[-1] * 2) / v_max + t1[-1], decimals )
        t2, a2, v2, x2 = uniform_linear_motion(v0=v_max, t0=t1[-1], t1=t1_tmp, x0=x1[-1], steps=step)

        # 減速
        t3, a3, v3, x3 = uniformly_accelerated_motion(v_max, t2[-1], t2[-1] + t1[-1], x2[-1], -1.0*acceleration, step)

        t = [ t1, t2, t3 ]
        a = [ a1, a2, a3 ]
        v = [ v1, v2, v3 ]
        x = [ x1, x2, x3 ]
    
    return t, a, v, x

def main():
    t, a, v, x = motor_graph_calculate(10.0, 1.0, 0.35, 10)
    
    print('t', t)
    print('a', a)
    print('v', v)
    print('x', x)

if __name__ == '__main__':
    main()