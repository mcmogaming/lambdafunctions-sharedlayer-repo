# remove old python files
rm -r ./build/python/messageLibrary/*
# copy new python files
cp layercode/* ./build/python/messageLibrary
# zip the python folder in build
cd ./build
zip -r messageLibrary.zip python/*
cp messageLibrary.zip ../messageLibrary.zip
rm ./messageLibrary.zip