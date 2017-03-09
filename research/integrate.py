#!/usr/bin/env python
import ics
import os
import os.path
import rebound as reb
import uuid

if __name__ == '__main__':
    while True:
        sim = ics.draw_sim()

        fname = str(uuid.uuid4()) + '.bin'
        try:
            sim.initSimulationArchive(fname, interval=1000)

            escaped = False
            try:
                sim.integrate(10000, exact_finish_time=0)
            except reb.Escape:
                escaped = True

            if escaped:
                efile = os.path.join('unstable', fname)
                os.rename(fname, efile)
                print("Unstable")
            else:
                sfile = os.path.join('stable', fname)
                os.rename(fname, sfile)
                print("Stable")
        finally:
            if os.path.exists(fname):
                os.remove(fname)
                
