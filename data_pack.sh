
# sequences=("500_w50ms" 
# "250_w2ms" "250_w4ms" "250_w8ms" "250_w20ms" "250_w50ms" )
sequences=("250_w2ms")
for seq in ${sequences[@]};
do
echo $seq
date
cd /media/data/yangchu/EventSOT/EventSOT500
# pwd
tar -czvf "$seq".tar.gz "$seq"
echo "done"
done