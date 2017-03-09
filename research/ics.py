from pylab import *
import rebound as reb

mtrapa = 0.0802  # MSun
mearth = 0.000003003  # MSun
days = 1.0/365.25 # yr
deg = np.pi/180.0 # radians
epoch = 7400.0 # Days.

def add_trappista(sim):
    sim.add(m=mtrapa)
def add_trappistp(sim, P0, dP0, T0, dT0, M0, dM0):
    e = abs(0.04*randn())
    i = 0.5*deg*randn()
    omega = 2*pi*rand()
    Omega = 2*pi*rand()
    
    P = abs(P0 + dP0*randn())
    T = abs(T0 + dT0*randn())
    M = abs(M0 + dM0*randn())
    
    pomega = omega + Omega 
    
    M_at_trans = - pomega
    dM = (T-epoch)/P*2*pi
    
    M_at_epoch = M_at_trans - dM
    
    a = (sim.G*mtrapa*P*P*days*days/(4.0*pi*pi))**(1.0/3.0)
    
    sim.add(m=M*mearth, a=a, M=M_at_epoch, omega=omega, Omega=Omega, e=e, inc=i)

def draw_sim():
    sim = reb.Simulation()
    sim.G = 4.0*pi*pi
    sim.exit_max_distance = 1 # Raise an exception if any body goes beyond 1 AU.
    sim.integrator = "whfast" # Hermes uses the Wisdom-Holman scheme with close encounters integrated by IAS15
    sim.ri_whfast.safe_mode = 0 # This and the next setting are much faster, but only OK if you don't access the particle array between steps
    sim.ri_whfast.corrector = 11 # Same
    sim.dt = 0.05*pi/3.0*1.51087081*days # Close to 5% of inner orbit period, but not commensurate

    add_trappista(sim)
    add_trappistp(sim, 1.51087081, 0.6e-6, 7322.51736, 0.00010, 0.85, 0.72)
    add_trappistp(sim, 2.4218233, 0.17e-5, 7282.80728, 0.00019, 1.38, 0.61)
    add_trappistp(sim, 4.049610, 0.63e-4, 7670.14165, 0.00035, 0.41, 0.27)
    add_trappistp(sim, 6.099615, 0.11e-4, 7660.37859, 0.00038, 0.62, 0.58)
    add_trappistp(sim, 9.206690, 0.15e-4, 7671.39767, 0.00023, 0.68, 0.18)
    add_trappistp(sim, 12.35294, 0.12e-3, 7665.34937, 0.00021, 0.94, 0.63)
    add_trappistp(sim, 20.0, 6.0, 7662.55463, 0.00056, 0.755**3, 3.0*0.755**2*0.034)

    sim.move_to_com()
    
    return sim

