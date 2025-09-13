# {WIP} FMCW 
Explorations in FMCW Processing 

# What is FMCW?

Frequency Modulated Continuous Wave (FMCW) is a type of transmission system in which a "continuous" carrier is swept/chirped in frequency in a known manner(Though there is recent research in pseudo-random frequency sweeps!). This is typically used in ranging systems, but also opens the door to doppler processing, which gives a true measure of a target's velocity.  But this is largely in contrast to pulsed transmission systems in which the system would send out an impulse signal at known times, and measure the time of propogotation. 

Of course, there's a plethora of differences, which we will go into further detail below. 
--- 

(skip this section to get to the fun stuff below!)

To begin with, let us set a scene. Let's imagine we're standing in a park and would like to measure the distance between us and a stationary bird. Naturally, we would estimate this with our (human) vision first. If we had bat-like organs, we would be transmitting sonar signals towards the location of the bird, and looking for the time it takes for a signal to return back to us. This is the common Time-of-Flight(TOF) method.


The first step in constructing a frequency sweep, is understanding how a device can actually sweep the frequency of a signal. Remember that the derivative of the phase of a signal, gives you the frequency of that signal. So in nominal FMCW processing, where we want a *linear* frequency sweep(commonly referred to as a _chirp_), we will change the phase in a quadratic manner. I will skip over the device physics in this overview, but to keep it short, one can use a PLL to accurately control the phase of a signal. If you're like me, you may have always thought that PLLs were designed to simply keep a *constant* phase, but this isn't the case! If you'd like to learn more about how this is done in radar systems, see the `pll/` folder in this repo, where a similiar overview and code is provided. 

We can model a frequency sweep with simply as a signal with a quadratic changing phase. A nominal FMCW system will define a standard "carrier" frequency, from which it will sweep a relatively narrow bad of frequencies. This is referred to as the chirp. The rate at which this signal sweeps from the minimum to max frequency is referred to as the chirp rate, also commonly noted as `α` The rate at which these freu

<picture of sin wave with varying phase >

<picture of tx, rx, and both with nonlineariies >

how do we remove non-linearities 
<include images>



## References
[1] FMCW Processing: https://www.utwente.nl/en/eemcs/mcs/teaching/Thesis/peek.pdf
    - Primary reference used for analytical model of an FMCW Radar
    
[2] PLL Design for FMCW Radar Systems https://www2.eecs.berkeley.edu/Pubs/TechRpts/2024/EECS-2024-106.pdf
    - Primary reference for PLL Design