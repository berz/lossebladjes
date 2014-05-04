#!/usr/bin/bash

in_dir='/home/berz_/temp/castrum/lossebladjes/scans/fulres_scans'
out_dir='/home/berz_/temp/castrum/lossebladjes/scans/optimized'

rm $out_dir/*

find $in_dir -type f | while read file; do
    filename="$(basename "$file")"

    if [[ "$filename" == _* ]]; then
        filename="${filename}_(discarded)"
        continue
    fi


    file_count=$(find $out_dir -name "$filename" | wc -l)
    if [[ $file_count -gt 0 ]]; then
        echo "skipped file, filename already present in output dir:"
        echo "    $file"
    else
        cp "$file" "${out_dir}/${filename}"
    fi
done
