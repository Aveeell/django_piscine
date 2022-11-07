link=$1
if [ $link ]; then
curl -si $link | grep "Location:" | cut -d ' ' -f 2
fi