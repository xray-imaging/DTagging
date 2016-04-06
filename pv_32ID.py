# -*- coding: utf-8 -*-
"""
Transmission X-ray Microscope process variables grouped by component

"""

from epics import PV

# User Status
user_name = PV('32idcTXM:UserName')
user_affiliation = PV('32idcTXM:UserInstitution')
user_badge = PV('32idcTXM:UserBadge')
user_email = PV('32idcTXM:UserEmail')
proposal_number = PV('32idcTXM:ProposalNumber')
proposal_title = PV('32idcTXM:ProposalTitle')
user_info_update_time= PV('32idcTXM:UserInfoUpdate')
file_name = PV('32idcPG3:HDF1:FileName')
file_path = PV('32idcPG3:HDF1:FilePath_RBV')

# Beamline Status
date_time = PV('S:IOC:timeOfDayISO8601')
current = PV('S:SRcurrentAI')
top_up_status = PV('S:TopUpStatus')
source_energy = PV('ID32ds:Energy.VAL')
source_gap = PV('ID32ds:Gap.VAL')
energy_dcm = PV('32ida:BraggEAO.VAL')
mirror_x  = PV('32idbMIR:m1.RBV')
mirror_y  = PV('32idbMIR:m2.RBV')

# Beam Monitor
beam_monitor_x = PV('32idcTXM:xps:c1:m2.VAL')
beam_monitor_y = PV('32idcTXM:nf:c0:m3.VAL')
beam_monitor_x_dial = PV('32idcTXM:xps:c1:m2.DVAL')
beam_monitor_y_dial = PV('32idcTXM:nf:c0:m3.DVAL')

# Filter
filter_x = PV('32idcTXM:xps:c2:m1.VAL')
filter_x_dial = PV('32idcTXM:xps:c2:m1.DVAL')

# microCT
table_x_upstream = PV('32idc02:m1.VAL')
table_y_upstream = PV('32idc02:m2.VAL')
table_y_downstream = PV('32idc02:m3.VAL')
table_x_downstream = PV('32idc02:m4.VAL')
table_x_upstream_dial = PV('32idc02:m1.DVAL')
table_y_upstream_dial = PV('32idc02:m2.DVAL')
table_y_downstream_dial = PV('32idc02:m3.DVAL')
table_x_downstream_dial = PV('32idc02:m4.DVAL')

# Sample microCT
sample_x_mct = PV('32idc02:m31.VAL')
sample_y_mct = PV('32idc02:m25.VAL')
sample_top_x_mct = PV('32idc01:m104.VAL')
sample_top_z_mct = PV('32idc01:m105.VAL')
sample_rotary_mct = PV('32idc02:m11.VAL')
sample_yaw_mct = PV('32idc02:m30.VAL')
sample_pitch_mct = PV('32idc02:m29.VAL')

sample_x_mct_dial = PV('32idc02:m31.DVAL')
sample_y_mct_dial = PV('32idc02:m25.DVAL')
sample_top_x_mct_dial = PV('32idc01:m104.DVAL')
sample_top_z_mct_dial = PV('32idc01:m105.DVAL')
sample_rotary_mct_dial = PV('32idc02:m11.DVAL')
sample_yaw_mct_dial = PV('32idc02:m30.DVAL')
sample_pitch_mct_dial = PV('32idc02:m29.DVAL')

# CCD camera
ccd_camera_z_mct = PV('32idc02:m20.VAL')
ccd_camera_z_mct_dial = PV('32idc02:m20.DVAL')
ccd_selector_mct =  PV('32idc02:m21.VAL')
ccd_selector_mct_dial =  PV('32idc02:m21.DVAL')
ccd_focus_mct =  PV('32idc02:m22.VAL')
ccd_focus_mct_dial =  PV('32idc02:m22.DVAL')

scintillator_x_mct = PV('32idc01:m101.VAL')
scintillator_y_mct = PV('32idc01:m102.VAL')
scintillator_x_mct_dial = PV('32idc01:m101.DAL')
scintillator_y_mct_dial = PV('32idc01:m102.DVAL')

# TXM
# Diffuser
diffuser = PV('32idcTXM:xps:c1:m6.VAL')
diffuser_dial = PV('32idcTXM:xps:c1:m6.DVAL')

# Beam Stop
beam_stop_x = PV('32idcTXM:xps:c1:m1.VAL')
beam_stop_y = PV('32idcTXM:nf:c0:m2.VAL')
beam_stop_x_dial = PV('32idcTXM:xps:c1:m1.DVAL')
beam_stop_y_dial = PV('32idcTXM:nf:c0:m2.DVAL')

# CRL
crl_x = PV('32idb:m32.VAL')
crl_y = PV('32idb:m28.VAL')
crl_pitch = PV('32idb:m26.VAL')
crl_yaw = PV('32idb:m27.VAL')
crl_x_dial = PV('32idb:m32.DVAL')
crl_y_dial = PV('32idb:m28.DVAL')
crl_pitch_dial = PV('32idb:m26.DVAL')
crl_yaw_dial = PV('32idb:m27.DVAL')

# Condenser
condenser_x = PV('32idcTXM:xps:c2:m8.VAL')
condenser_y = PV('32idcTXM:mxv:c1:m2.VAL')
condenser_z = PV('32idcTXM:mxv:c1:m5.VAL')
condenser_x_dial = PV('32idcTXM:xps:c2:m8.DVAL')
condenser_y_dial = PV('32idcTXM:mxv:c1:m2.DVAL')
condenser_z_dial = PV('32idcTXM:mxv:c1:m5.DVAL')

# Pin Hole
pin_hole_x = PV('32idcTXM:xps:c1:m3.VAL')
pin_hole_y = PV('32idcTXM:xps:c1:m4.VAL')
pin_hole_z = PV('32idcTXM:xps:c1:m5.VAL')
pin_hole_x_dial = PV('32idcTXM:xps:c1:m3.DVAL')
pin_hole_y_dial = PV('32idcTXM:xps:c1:m4.DVAL')
pin_hole_z_dial = PV('32idcTXM:xps:c1:m5.DVAL')

# Sample
sample_x = PV('32idcTXM:xps:c1:m8.VAL')
sample_y = PV('32idcTXM:mxv:c1:m1.VAL')
sample_rotary = PV('32idcTXM:hydra:c0:m1.VAL')
sample_x_dial = PV('32idcTXM:xps:c1:m8.DVAL')
sample_y_dial = PV('32idcTXM:mxv:c1:m1.DVAL')
sample_rotary_dial = PV('32idcTXM:hydra:c0:m1.DVAL')

sample_top_x = PV('32idcTXM:mcs:c1:m2.VAL')
sample_top_z = PV('32idcTXM:mcs:c1:m1.VAL')
sample_top_x_dial = PV('32idcTXM:mcs:c1:m2.DVAL')
sample_top_z_dial = PV('32idcTXM:mcs:c1:m1.DVAL')

# Zone Plate
zone_plate_x = PV('32idcTXM:mcs:c2:m2.VAL')
zone_plate_y = PV('32idc01:m110.VAL')
zone_plate_z = PV('32idcTXM:mcs:c2:m3.VAL')
zone_plate_x_dial = PV('32idcTXM:mcs:c2:m2.DVAL')
zone_plate_y_dial = PV('32idc01:m110.DVAL')
zone_plate_z_dial = PV('32idcTXM:mcs:c2:m3.DVAL')

# 2nd Zone Plate
zone_plate_2nd_x = PV('32idcTXM:mcs:c0:m3.VAL')
zone_plate_2nd_y = PV('32idcTXM:mcs:c0:m1.VAL')
zone_plate_2nd_z = PV('32idcTXM:mcs:c0:m2.VAL')
zone_plate_2nd_x_dial = PV('32idcTXM:mcs:c0:m3.DVAL')
zone_plate_2nd_y_dial = PV('32idcTXM:mcs:c0:m1.DVAL')
zone_plate_2nd_z_dial = PV('32idcTXM:mcs:c0:m2.DVAL')

# Bertrand Lens
bertrand_x = PV('32idcTXM:nf:c0:m4.VAL')
bertrand_y = PV('32idcTXM:nf:c0:m5.VAL')
bertrand_x_dial = PV('32idcTXM:nf:c0:m4.DVAL')
bertrand_y_dial = PV('32idcTXM:nf:c0:m5.DVAL')

# Flight Tube
flight_tube_z = PV('32idcTXM:mxv:c1:m8.VAL')
flight_tube_z_dial = PV('32idcTXM:mxv:c1:m8.DVAL')

# CCD camera
ccd_camera_x = PV('32idcTXM:mxv:c1:m3.VAL')
ccd_camera_y = PV('32idcTXM:mxv:c1:m4.VAL')
ccd_camera_z = PV('32idcTXM:mxv:c1:m6.VAL')
ccd_camera_x_dial = PV('32idcTXM:mxv:c1:m3.DVAL')
ccd_camera_y_dial = PV('32idcTXM:mxv:c1:m4.DVAL')
ccd_camera_z_dial = PV('32idcTXM:mxv:c1:m6.DVAL')

ccd_yaw = PV('32idcTXM:xps:c2:m7.VAL')
ccd_objective = PV('32idcTXM:xps:c2:m2.VAL')
ccd_yaw_dial = PV('32idcTXM:xps:c2:m7.DVAL')
ccd_objective_dial = PV('32idcTXM:xps:c2:m2.DVAL')

