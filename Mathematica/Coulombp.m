(* ::Package:: *)

BeginPackage["CoulombPotential`"]
Clear[WaveF,WaveR,WaveA];
WaveF::usage="WaveF[Z_,r_,theta_,phi_,n_,l_,m_]"
WaveR::usage="WaveR[Z_,r_,n_,l_]"
WaveA::usage="WaveA[theta_,phi_,l_,m_]"
r::usage
n::usage
l::usage
m::usage
theta::usage
phi::usage
Begin["`Private`"]
WaveR[Z_,r_,n_,l_]:=Module[{unit,tmp},unit=(Sqrt[(n+l)!/(2 n (n-l-1)!)] ((2 Z)/n)^(l+3/2))/(2 l+1)!;tmp=unit r^l Exp[-((Z r)/n)] Hypergeometric1F1[l+1-n,2 l+2,(2 Z r)/n]]
WaveA[theta_,phi_,l_,m_]:=Module[{tmp},tmp=SphericalHarmonicY[l,m,theta,phi]]
WaveF[Z_,r_,theta_,phi_,n_,l_,m_]:=Module[{tmp},tmp=WaveR[Z,r,n,l] WaveA[theta,phi,l,m]]
End[]
EndPackage[]



