# VI-SLAM-UAV
Master thesis project that aims to evaluate and compare VI-SLAM methods for UAV-imagery at Maxar Technologies.

## 1. Install
```
git clone https://github.com/FredrikErikJohansson/VI-SLAM-UAV.git
cd VI-SLAM_UAV
git submodule update --init
```

## 2. Dependencies
```
sudo apt install libsuitesparse-dev libeigen3-dev libboost-all-dev libopencv-dev libgl1-mesa-dev libglew-dev cmake pkg-config zlib1g-dev
```

## 3. Build
### 3.1 DSO
```
cd dso
mkdir build
cd build
cmake ..
make -j4
```
### 3.1 Pangolin
```
cd pangolin
mkdir build
cd build
cmake ..
cmake --build .
```
