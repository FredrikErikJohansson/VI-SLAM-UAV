
BUILD_TYPE=Release
NUM_PROC=4

echo "Configuring and building Thirdparty/DBoW2 ..."

cd LDSO/thirdparty/DBoW3
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=$BUILD_TYPE ..
make -j$NUM_PROC
cd ../../g2o

echo "Configuring and building Thirdparty/g2o ..."

mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=$BUILD_TYPE ..
make -j$NUM_PROC
cd ../../../

echo "Configuring and building LDSO ..."

mkdir build
cd build
cmake ..
make -j$NUM_PROC

cd ../../pangolin

echo "Configuring and building Pangolin ..."

mkdir build
cd build
cmake ..
cmake --build .

cd ../../ORB_SLAM3

echo "Configuring and building Thirdparty/DBoW2 ..."

cd Thirdparty/DBoW2
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$NUM_PROC

cd ../../g2o

echo "Configuring and building Thirdparty/g2o ..."

mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$NUM_PROC

cd ../../../

echo "Uncompress vocabulary ..."

cd Vocabulary
tar -xf ORBvoc.txt.tar.gz
cd ..

echo "Configuring and building ORB_SLAM3 ..."

mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$NUM_PROC

cd ../../
