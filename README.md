# VI-SLAM-UAV
Master thesis project that aims to evaluate and compare VI-SLAM methods for UAV-imagery at Maxar Technologies.

## 1. Install
```
git clone https://github.com/FredrikErikJohansson/VI-SLAM-UAV.git
cd VI-SLAM-UAV
git submodule update --init
```

## 2. Dependencies
```
sudo apt install libsuitesparse-dev \
    libeigen3-dev \
    libboost-all-dev \
    libopencv-dev \
    libgl1-mesa-dev \
    libglew-dev \
    cmake \
    pkg-config \
    zlib1g-dev \
    libpython2.7-dev
```

## 3. Build
```
chmod +x build.sh
./build.sh
```

## 4. Usage
### Datasets:
* [AGZ](http://rpg.ifi.uzh.ch/zurichmavdataset.html)
* [TUM-Mono](https://vision.in.tum.de/mono-dataset)
* [Kitti](http://www.cvlibs.net/datasets/kitti/eval_odometry.php)
* [EuRoC](https://projects.asl.ethz.ch/datasets/doku.php?id=kmavvisualinertialdatasets)
* [TUM-VI](https://vision.in.tum.de/data/datasets/visual-inertial-dataset)

### [4.1 LDSO](https://github.com/tum-vision/LDSO/)

LSDO provides examples for TUM-Mono, Kitti and EuRoC but the datasets can easily be extended in the `examples` folder.

#### TUM-Mono:
To run LDSO on TUM-Mono dataset sequence 34, execute:
```
./bin/run_dso_tum_mono \
    preset=0 \
    files=XXXXX/TUMmono/sequences/sequence_34/images.zip \
    vignette=XXXXX/TUMmono/sequences/sequence_34/vignette.png \
    calib=XXXXX/TUMmono/sequences/sequence_34/camera.txt \
    gamma=XXXXX/TUMmono/sequences/sequence_34/pcalib.txt
```

#### Kitti:
To run LDSO on Kitti dataset sequence 00, execute:
```
./bin/run_dso_kitti \
    preset=0 \
    files=XXXXX/Kitti/odometry/dataset/sequences/00/ \
    calib=./examples/Kitti/Kitti00-02.txt
```

#### EuRoC:
To run LDSO on EuRoC dataset sequence MH_01_easy, execute:
```
./bin/run_dso_euroc \
    preset=0 \
    files=XXXX/EuRoC/MH_01_easy/mav0/cam0/
```

### [4.2 ORB-SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3)

ORB-SLAM3 provides examples for the EuRoC and TUM-VI and we have extended it to include AGZ.

#### AGZ:
Open the script `AGZ_examples.sh` and change `pathDatasetAGZ` to point to the directory where the dataset has been uncompressed. Change which sequences to process (default is set to all). Execute the following script:

```
./AGZ_examples
```

#### EuRoC:
Open the script `euroc_examples.sh` and change `pathDatasetEuroc` to point to the directory where the dataset has been uncompressed. Change which sequences to process (default is set to all). Execute the following script:

```
./euroc_examples
```

Execute the following script to process sequences and compute the RMS ATE:

```
./euroc_eval_examples
```

#### TUM-VI
Open the script `tum_vi_examples.sh` and change `pathDatasetTUM_VI` to point to the directory where the dataset has been uncompressed. Change which sequences to process (default is set to all). Execute the following script:

```
./tum_vi_examples
```

Execute the following script to process sequences and compute the RMS ATE:
```
./tum_vi_eval_examples
```
