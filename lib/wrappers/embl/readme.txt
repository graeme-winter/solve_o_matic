BEST command line options:

best -f pilatus6m -t 0.5 -M 0.067 -S 10.0 -w 0.1 -R 3.0 -i2s 2.0 -sh 1 -T 807.0 \
-mos bestfile.dat bestfile.par bestfile.hkl

These options are:

-f pilatus6m - detector configuration
-t 0.5       - exposure time for reference images
-M 0.067     - minimum exposure time
-S 10        - max rotation speed (deg/s)
-w 0.1       - min image width
-R 3.0       - min multiplicity
-i2s 2.0     - min I/sigI at edge
-sh 1        - shape factor, increase if large xtal in small beam
-T 807.0     - maximum total exposure time
-mos         - files from mosflm - must come at end

Extra options

-Trans       - transmission of screening images
-a           - anomalous scattering
-r           - target resolution
-asad        - 360 degree SAD collection, decide resolution
-su          - radiation sensitivity scale - > 1 more sensitive

Output

The output looks something like:


                                   Main Wedge
                                 ================
       Resolution limit is set by the initial image resolution
 Resolution limit =1.51 Angstrom   Transmission =    1.0%  Distance = 278.2mm
-----------------------------------------------------------------------------------------
           WEDGE PARAMETERS       ||                 INFORMATION
----------------------------------||-----------------------------------------------------
sub-| Phi  |Rot.  | Exposure| N.of||Over|sWedge|Exposure|Exposure| Dose  | Dose  |Comple-
 We-|start |width | /image  | ima-||-lap| width| /sWedge| total  |/sWedge| total |teness
 dge|degree|degree|     s   |  ges||    |degree|   s    |   s    | MGy   |  MGy  |  %
----------------------------------||-----------------------------------------------------
 1   128.00   0.15     0.067   534|| No   80.10     35.8     35.8   0.000   0.000  100.0
-----------------------------------------------------------------------------------------

 Phi_start - Phi_finish      : 128.00 - 208.10
 Total rotation range        : 80.10 degree
 Total N.of images           : 534
 Overall Completeness        : 100.0%
 Redundancy                  : 3.39
 R-factor (outer shell)      : 4.8% (   25.5%)
 I/Sigma (outer shell)       : 25.5 (   4.6)
 Total Exposure time         : 35.2 sec (0.010 hour)
 Total Data Collection time  : 43.3 sec (0.012 hour)
<!--SUMMARY_END--></FONT></B>

     Wedge Data Collection Statistics according to the Strategy
-------------------------------------------------------------------------
 Resolution  Compl.       Average      <I>/      <I/     R-fact  Overload
Lower Upper     %   Intensity  Sigma    <Sigma>   Sigma>     %        %
-------------------------------------------------------------------------
12.00  6.42    98.8     170.7     3.3    51.9      54.0     2.2     0.00
 6.42  4.90   100.0     131.3     2.8    47.5      49.3     2.5     0.00
 4.90  4.12   100.0     219.4     4.3    50.4      52.2     2.3     0.00
 4.12  3.62   100.0     194.3     3.9    49.4      50.5     2.5     0.00
 3.62  3.27   100.0     149.1     3.3    45.1      46.2     2.7     0.00
 3.27  3.00   100.0     101.6     2.6    39.8      40.7     3.1     0.00
 3.00  2.79   100.0      72.9     2.1    34.4      35.4     3.6     0.00
 2.79  2.62   100.0      56.3     1.8    30.5      31.4     4.0     0.00
 2.62  2.48   100.0      47.5     1.7    28.0      28.7     4.5     0.00
 2.48  2.36   100.0      41.9     1.6    25.5      26.4     4.8     0.00
 2.36  2.25   100.0      38.6     1.6    23.9      24.8     5.1     0.00
 2.25  2.16   100.0      35.0     1.6    22.3      23.0     5.6     0.00
 2.16  2.08   100.0      30.8     1.5    20.4      21.2     6.1     0.00
 2.08  2.00   100.0      25.7     1.4    18.3      18.9     6.8     0.00
 2.00  1.94   100.0      20.7     1.3    16.0      16.7     7.7     0.00
 1.94  1.88   100.0      16.1     1.2    13.8      14.3     9.1     0.00
 1.88  1.82   100.0      12.7     1.1    11.7      12.2    10.5     0.00
 1.82  1.77   100.0      10.2     1.0    10.1      10.5    12.2     0.00
 1.77  1.73   100.0       8.7     1.0     9.0       9.4    13.7     0.00
 1.73  1.68   100.0       7.4     0.9     7.9       8.2    15.7     0.00
 1.68  1.64   100.0       6.5     0.9     7.3       7.6    17.1     0.00
 1.64  1.61   100.0       5.8     0.9     6.5       6.8    18.7     0.00
 1.61  1.57   100.0       5.1     0.8     6.0       6.3    20.6     0.00
 1.57  1.54   100.0       4.6     0.8     5.4       5.7    22.3     0.00
 1.54  1.51   100.0       4.0     0.8     4.7       4.9    25.3     0.00
  All data    100.0      37.3     1.5    25.5      18.9     4.8     0.00
--------------------------------------------------------------------------
R-fact = SUM (ABS(I - <I>)) / SUM (I)


                  Additional information
                 =======================
Fraction of unique reflections in blind region:   0.0%

Scaling
 Relative scale       :    2.12
 Overall B-factor     :   9.70 Angstrom^2
 B-factor eigenvalues :   8.78  10.23  10.23 Angstrom^2
 Scaling error        :   6% at the resolution limit

Commentary

The time limit here makes essentially no difference - we are massively within the
time limit :)

The calculation of this took some 45s to perform...
