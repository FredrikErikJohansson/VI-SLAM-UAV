echo "Configuring and building DSO ..."

cd dso
mkdir build
cd build
cmake ..
make -j4

cd ../../pangolin

echo "Configuring and building Pangolin ..."

mkdir build
cd build
cmake ..
cmake --build .

cd ../../