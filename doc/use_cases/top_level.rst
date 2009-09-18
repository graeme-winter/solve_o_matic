================================
Solve-o-Matic Top-Level Use Case
================================

Version: 0.1 18/SEP/09

Introduction
============

The aim of this document is to provide the top-level use cases for
Solve-o-Matic, with the aim of putting the derived specifications in 
context.

Actors
======

- User: the user who will most likely be either at the beamline or operating
  the beamline remotely. In the first instance this will be targetted at the 
  needs of high-throughput users, namely industrial users and those from 
  large, well organised academic labs.

- ISPyB: the beamline information management system, which holds the sample
  information and should ideally be populated prior to the experiment with
  the sample metadata (projects, sequences, models, protein names and so on)
  and experimental metadata during the experiment.

- GDA: the generic data acquisition system, which is used to perform the 
  experiment, controls the experimental hardware and interacts with ISPyB.

- Cluster: this is the Sun Grid Engine managed compute cluster where the 
  necessary computation can be performed.

Before the Experiment / Visit
=============================

The user should populate ISPyB with the sample metadata for those samples
which will be analysed during the experiment. This may include the sample 
positions in the pucks if they are pre-mounted, and should include a
protein name, which will be used to associate the sample with the expected
content, either in the form of a protein sequence or model. For cases
where the sample has been modified to allow experimental phasing, the 
modifications should also be stored. 

If the putative spacegroup and cell constants are known before the experiment
it may be beneficial to assign them at this stage, as this information
may be used to inform decisions about the data reduction and phasing.

During the Experiment
=====================

During the experiment the sample information may be obtained to inform the 
correct procedures which should be performed at the end of each data collection
run. At the moment we have the cabability to launch a data reduction run
after each data collection: by interrogating ISPyB this could determine the
best route to take for postprocessing the measurements. The links to 
ISPyB will also be used to record the results of the data processing 
and downstream structure solution.

In addition to the automated-but-simple processing it may be desirable to 
have the user specify data reduction and structure solution tasks from the 
history tab in GDA: this will need to be specified externally.

The aim is that users may be able to obtain the results of the experiment
in the form of an electron density map rather than diffraction images or 
reduced data within a few minutes of the experiment. 

For remote users there is a secondary benefit: they may be able to take the 
reduced data or maps and perform analysis at home, without having to ship
the raw data. 

After the Experiment
====================

Once the experiment is complete the results of all of the data collection,
data reduction and structure solution should be available through ISPyB.
This will allow the users to have a permanent record of all of the 
results of the visit, which may inform the choices made during subsequent
visits.

