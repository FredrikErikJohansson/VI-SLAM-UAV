#!/bin/bash

#-------------------------------------------------------------
#-------------------------------------------------------------

# V101
for i in {1..10}
do
    echo "----------------------------------------"
    echo "Running on: ./Vicon_rooms_LDSO/V101_mono_LDSO_$i.ply"
    echo "----------------------------------------"
    python3 icp_reg_V101.py ./Vicon_rooms_LDSO/f_V101_mono_LDSO_$i.ply V1_Laser.ply
    python3 meanErrorLine.py SOURCE.ply TARGET.ply
    echo "----------------------------------------"
done

# V102
for i in {1..10}
do
    echo "----------------------------------------"
    echo "Running on: ./Vicon_rooms_LDSO/V102_mono_LDSO_$i.ply"
    echo "----------------------------------------"
    python3 icp_reg_V102.py ./Vicon_rooms_LDSO/f_V102_mono_LDSO_$i.ply V1_Laser.ply
    python3 meanErrorLine.py SOURCE.ply TARGET.ply
    echo "----------------------------------------"
done

# V103
for i in {1..10}
do
    echo "----------------------------------------"
    echo "Running on: ./Vicon_rooms_LDSO/V103_mono_LDSO_$i.ply"
    echo "----------------------------------------"
    python3 icp_reg_V103.py ./Vicon_rooms_LDSO/f_V103_mono_LDSO_$i.ply V1_Laser.ply
    python3 meanErrorLine.py SOURCE.ply TARGET.ply
    echo "----------------------------------------"
done

# V201
for i in {1..10}
do
    echo "----------------------------------------"
    echo "Running on: ./Vicon_rooms_LDSO/V201_mono_LDSO_$i.ply"
    echo "----------------------------------------"
    python3 icp_reg_V201.py ./Vicon_rooms_LDSO/f_V201_mono_LDSO_$i.ply V2_Laser.ply
    python3 meanErrorLine.py SOURCE.ply TARGET.ply
    echo "----------------------------------------"
done

# V203
for i in {1..10}
do
    echo "----------------------------------------"
    echo "Running on: ./Vicon_rooms_ORB/V203_mono_ORB_$i.ply"
    echo "----------------------------------------"
    python3 icp_reg_V203.py ./Vicon_rooms_ORB/V203_mono_ORB_$i.ply V2_Laser.ply
    python3 meanErrorLine.py SOURCE.ply TARGET.ply
    echo "----------------------------------------"
done

# Gistad
for i in {1..10}
do
    echo "----------------------------------------"
    echo "Running on: ./data_gistad/gistad_smooth_mono_ORB_$i.ply"
    echo "----------------------------------------"
    python3 icp_reg_gistad_smooth.py ./data_gistad/gistad_smooth_mono_ORB_$i.ply ./data_gistad/gt_pointcloud.ply
    python3 meanErrorLine.py SOURCE.ply TARGET.ply
    echo "----------------------------------------"
done

# Gistad Speed 3
for i in {1..10}
do
    echo "----------------------------------------"
    echo "Running on: ./data/Evaluations/gistad_speed1_mono_ORB_$i.ply"
    echo "----------------------------------------"
    python3 icp_reg_gistad_speed.py ./data/Evaluations/gistad_speed1_mono_ORB_$i.ply ./data/3ms_GT.ply
    python3 meanErrorLine.py SOURCE.ply TARGET.ply
    echo "----------------------------------------"
done

# Gistad Speed 5
for i in {1..10}
do
    echo "----------------------------------------"
    echo "Running on: ./data/Evaluations/gistad_speed3_mono_ORB_$i.ply"
    echo "----------------------------------------"
    python3 icp_reg_gistad_speed.py ./data/Evaluations/gistad_speed3_mono_ORB_$i.ply ./data/5ms_GT.ply
    python3 meanErrorLine.py SOURCE.ply TARGET.ply
    echo "----------------------------------------"
done

# Gistad Speed 7
for i in {1..10}
do
    echo "----------------------------------------"
    echo "Running on: ./data/Evaluations/gistad_speed5_mono_ORB_$i.ply"
    echo "----------------------------------------"
    python3 icp_reg_gistad_speed.py ./data/Evaluations/gistad_speed5_mono_ORB_$i.ply ./data/7ms_GT.ply
    python3 meanErrorLine.py SOURCE.ply TARGET.ply
    echo "----------------------------------------"
done

# Gistad Speed 9
for i in {1..10}
do
    echo "----------------------------------------"
    echo "Running on: ./data/Evaluations/gistad_speed7_mono_ORB_$i.ply"
    echo "----------------------------------------"
    python3 icp_reg_gistad_speed.py ./data/Evaluations/gistad_speed7_mono_ORB_$i.ply ./data/9ms_GT.ply
    python3 meanErrorLine.py SOURCE.ply TARGET.ply
    echo "----------------------------------------"
done

# Gistad Speed 11
for i in {1..10}
do
    echo "----------------------------------------"
    echo "Running on: ./data/Evaluations/gistad_speed9_mono_ORB_$i.ply"
    echo "----------------------------------------"
    python3 icp_reg_gistad_speed.py ./data/Evaluations/gistad_speed9_mono_ORB_$i.ply ./data/11ms_GT.ply
    python3 meanErrorLine.py SOURCE.ply TARGET.ply
    echo "----------------------------------------"
done

# Gistad Speed 13
for i in {1..10}
do
    echo "----------------------------------------"
    echo "Running on: ./data/Evaluations/gistad_speed12_mono_ORB_$i.ply"
    echo "----------------------------------------"
    python3 icp_reg_gistad_speed.py ./data/Evaluations/gistad_speed12_mono_ORB_$i.ply ./data/13ms_GT.ply
    python3 meanErrorLine.py SOURCE.ply TARGET.ply
    echo "----------------------------------------"
done












