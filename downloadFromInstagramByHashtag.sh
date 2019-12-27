#!/bin/bash

set -eu

HASHTAG=wabisabi
NUM2DL=30000
TARGET_DIR=dataset/$HASHTAG
TARGET_COLORSPACE=sRGB

# Check Dependency
which identify > /dev/null

# Create Directory
mkdir -p $TARGET_DIR

# Download
pip3 install instaLooter
python3 -m instalooter hashtag $HASHTAG $TARGET_DIR --template {id}_{width}x{height} --num-to-dl $NUM2DL

# Check Resolution
find $TARGET_DIR -type f -not -name "*_1080x1080.jpg" | xargs rm -f

# Check Colorspace
for jpg in $(find $TARGET_DIR -type f -name "*.jpg"); do
  colorspace=$(identify -format "%[colorspace]" $jpg)
  if [ $colorspace != $TARGET_COLORSPACE ]; then
    echo "NG: $jpg is $colorspace"
    rm -f $jpg
  fi
done

# Rename
DIGIT=100001
for jpg in $(find $TARGET_DIR -type f -name "*.jpg"); do
  basename=$(basename $jpg)
  mv $jpg $TARGET_DIR/${DIGIT:1}_$basename
  DIGIT=$((++DIGIT))
done

# Show Result
echo "Finally, ${DIGIT:1} JPGs remain."
