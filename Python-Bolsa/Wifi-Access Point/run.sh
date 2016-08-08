hotspotd start

ifconfig wlan0 down
iwconfig wlan0 mode monitor
iwconfig wlan0 channel 6
ifconfig wlan0 up

tshark -i wlan0 -T fields -e frame.time_relative -e wlan.sa -e wlan.da -e radiotap.datarate -e wlan_mgt.ssid -e radiotap.vendor_data -e radiotap.vendor_namespace -e radiotap.vendor_oui -e radiotap.txpower > "wifi_`date +%Y%m%d_%H%M`.txt"


